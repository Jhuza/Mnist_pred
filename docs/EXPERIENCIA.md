# Dígitos escritos a mano

Dibuja un dígito y observa cómo lo interpreta una red neuronal entrenada con MNIST.

Entrada: Un dígito del 0 al 9 dibujado sobre el tablero.

Salida: Dígito predicho, probabilidades y vista de la entrada reducida a 28 × 28 píxeles.

Uso: Dibuja un número blanco sobre el fondo negro y pulsa Predecir. Usa Limpiar para probar otro trazo.

Tecnología: MNIST · CNN · TensorFlow / Keras

Límites: Reconoce dígitos aislados, no palabras. La confianza es la puntuación del modelo y puede ser alta aunque se equivoque.

[Demo](https://mnistpred-hkkxpjbqcq3bsy8usncy5x.streamlit.app/) · [Código](https://github.com/Jhuza/Mnist_pred)
