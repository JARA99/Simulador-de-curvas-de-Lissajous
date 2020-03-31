# Simulador-de-curvas-de-Lissajous
Simple generador de gifs de curvas de Lissajous para Linux programado en Python y GnuPlot.


Este es un pequeño código de python para generar tablas de datos con las coordenadas de los puntos que se forman al tener un movimiento armónico con una cierta frecuencia en el eje x y uno distinto en el eje y. Esto forma las conocidas figuras de Lissajus. 

Para utilizarlo, si se tiene linux, ejecuta el "Execute.sh" de una de las dos carpetas "MuchosPuntos" o "PocosPuntos". En lo que se diferencian estas dos, es en el tiempo que lleva compilar el gif, ya que al principio se abrirá una terminal donde se pedirá la frecuencia de cada uno de los ejes, y la cantidad de puntos a dibujar, el tiempo de compilación depende del procesador, sin embargo, es útil utilizar el código de "MuchosPuntos" cuando se excede una cantidad muy grande, ya que en el código "PocosPuntos" cada punto es una imagen adjunta al gif, lo que hace que cuando tengas más de 10000 puntos (por ejemplo) el gif sea muy pesado.

Una vez ejecutado el "Execute.sh", se te preguntará la frecuencia de los ejes. Realmente no importa la unidad de medida de la frecuencia, ya que lo que realmete importa aquí es la relación entre las dos frecuencias; de este modo, la figura formada por las frecuencias 1:3 es la misma que la formada por las frecuencias 2:6. 

![Ejemplo de terminal](/Screenshots/TerminalScreenshot2.png?raw=true "Terminal Execute")

![Ejemplo de salida](/GIFs/Ejemplos/PocosPuntosConLineas.gif)

Al cerrar el gif, la terminal preguntará si quieres guardarlo, a lo que puedes responder "s" (si) o "n" (no). Una vez guardado puedes encontrarlo en la carpeta de GIFs con el nombre de L-n-m-p.gif o S-n-m-p.gif, donde L o S dicen si es con o sin líneas, n la frecuencia 1, m la frecuencia 2 y p la cantidad de puntos.

![Ejemplo de terminal](/Screenshots/TerminalScreenshot3.png?raw=true "Terminal Execute")


## Dependencias ##

Si presenta algun error, es posible que no tengas instaladas todas las dependencias, en una terminal corre el siguiente comando:

```python
sudo pip install math, decimal, tqdm, time, os, subprocess
```