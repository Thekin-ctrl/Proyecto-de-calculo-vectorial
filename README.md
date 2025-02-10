# Cálculo de la Integral Usando Suma de Riemann
Este proyecto calcula el valor aproximado de la integral de una función gaussiana 2D \(f(x, y) = e^{-(x^2 + y^2)}\) utilizando la suma de Riemann. Además, genera una visualización 3D de la función para mostrar cómo se distribuyen los valores de la función sobre el dominio seleccionado. El programa está implementado en Python y utiliza la librería Tkinter para la interfaz gráfica y Matplotlib para las visualizaciones.

## Instalación

Para ejecutar este proyecto, necesitas tener Python 3.x instalado. Además, debes instalar las siguientes librerías:

- `numpy`
- `matplotlib`
- `tkinter` (generalmente preinstalada con Python)

Puedes instalar las dependencias necesarias ejecutando el siguiente comando:
pip install numpy y pip install matplotlib

**Nota**: En algunas distribuciones de Python, `tkinter` ya viene instalado, pero si no lo tienes, sigue las instrucciones de [Tkinter](https://tkdocs.com/tutorial/) para tu sistema operativo.

## Uso

1. Ejecuta el script de Python `Proyecto.py`.
2. Se abrirá una ventana de interfaz gráfica donde podrás ingresar los siguientes parámetros:
   - **a**: el límite del dominio en ambas direcciones (por ejemplo, \(a = 2\)).
   - **n**: el número de subintervalos para la suma de Riemann (por ejemplo, \(n = 100\)).

3. Al hacer clic en el botón **Calcular**, el programa mostrará el valor aproximado de la integral y generará una visualización 3D de la función.

## Ejemplo de salida

Cuando ingreses \(a = 2\) y \(n = 100\), el programa te mostrará algo como:
El valor aproximado de la integral es: 3.14159265358979

Además, se mostrará una visualización 3D de la función gaussiana.

