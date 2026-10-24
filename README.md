# Dígitos escritos a mano

Dibuja un dígito y observa cómo lo interpreta una red neuronal entrenada con MNIST.

Adaptación académica de Juan José Hoyos (Jhuza), a partir del ejercicio compartido por Carlos Mario Correa. Interfaz basada en [Aurora](docs/guia-visual-aurora.md).

[Abrir app](https://mnistpred-hkkxpjbqcq3bsy8usncy5x.streamlit.app/) · [Portafolio](https://jhginterfacesmultimodalesportfolio.streamlit.app/)

## Ejecutar

```sh
python -m pip install -r requirements.txt
python -m streamlit run Inicio.py
```

## Uso y alcance

Dibuja un número blanco sobre el fondo negro y pulsa Predecir. Usa Limpiar para probar otro trazo.

Reconoce dígitos aislados, no palabras. La confianza es la puntuación del modelo y puede ser alta aunque se equivoque.

Consulta la [ficha de la experiencia](docs/EXPERIENCIA.md). Las credenciales se introducen en la sesión; no deben guardarse en el código.

## Verificación

Las pruebas de `tests/` comprueban controles, entradas vacías y resultados con servicios o modelos simulados. No certifican una respuesta de un servicio externo. Ejecutar con `python -m pytest tests -q` después de instalar pytest y las dependencias de la app.
