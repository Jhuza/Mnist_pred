from pathlib import Path
from types import SimpleNamespace, ModuleType
from unittest.mock import patch
import os
import sys
import numpy as np
from streamlit.testing.v1 import AppTest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))


def test_blank_rgba_guard_preprocessing_prediction_and_clear():
    calls=[]
    class Model:
        def predict(self, image, verbose=0):
            calls.append(image)
            return np.array([[.01,.91,.01,.01,.01,.01,.01,.01,.01,.01]])
    tf=ModuleType('tensorflow')
    tf.__version__='test-double'
    tf.keras=SimpleNamespace(__version__='test-double',models=SimpleNamespace(load_model=lambda *a,**kw:Model()))
    pixels=np.zeros((320,320,4),dtype=np.uint8)
    pixels[:,:,3]=255
    canvas=SimpleNamespace(image_data=pixels,json_data={'objects':[]})
    old=os.getcwd()
    try:
        os.chdir(ROOT)
        with patch.dict(sys.modules,{'tensorflow':tf}), patch('streamlit_drawable_canvas.st_canvas',return_value=canvas) as component:
            app=AppTest.from_file(str(ROOT/'Inicio.py')).run(timeout=30)
            app.button[0].click().run()
            assert not app.exception and app.warning and not calls
            canvas.json_data['objects']=[{'type':'path'}]
            pixels[50:270,155:175,:3]=255
            app.run()
            app.button[0].click().run()
            assert not app.exception
            assert calls[0].shape==(1,28,28,1)
            assert calls[0].min()>=0 and calls[0].max()<=1
            assert app.metric[0].value=='1'
            app.button[1].click().run()
            assert app.session_state['mnist_canvas_id']==1
            assert component.call_args.kwargs['key']=='canvas_1'
    finally:
        os.chdir(old)
