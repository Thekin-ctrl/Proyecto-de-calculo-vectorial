import tkinter as tk
from tkinter import messagebox  # Para mostrar ventanas emergentes con resultados y errores
import numpy as np  # Librería para realizar cálculos matemáticos
import matplotlib.pyplot as plt  # Librería para crear gráficos
from mpl_toolkits.mplot3d import Axes3D  # Para gráficos en 3D

# Definición de la función que se va a integrar.
# La función es una gaussiana 2D: f(x, y) = e^(-(x^2 + y^2)).
def f(x, y):
    return np.exp(-(x**2 + y**2))

# Función para calcular la integral utilizando la suma de Riemann.
# Argumentos:
# - a: Límite del dominio en ambas direcciones (en el rectángulo [-a, a] x [-a, a]).
# - n: Número de subintervalos en cada dimensión.
def suma_riemann(a, n):
    dx = dy = 2 * a / n  # Tamaño de los subintervalos en ambas direcciones
    suma_total = 0  # Inicializa la suma acumulada que almacenará el resultado

    # Iteración sobre los subintervalos para calcular los puntos medios
    for i in range(n):
        for j in range(n):
            x = -a + (i + 0.5) * dx  # Coordenada x del punto medio
            y = -a + (j + 0.5) * dy  # Coordenada y del punto medio
            suma_total += f(x, y) * dx * dy  # Agrega el área del rectángulo correspondiente

    return suma_total  # Devuelve el valor aproximado de la integral

# Función que se ejecuta al hacer clic en el botón de "Calcular"
def calcular():
    try:
        # Obtiene los valores de a y n de las entradas de texto
        a = float(entrada_a.get())
        n = int(entrada_n.get())

        # Verifica que los valores sean positivos
        if a <= 0 or n <= 0:
            raise ValueError("Los valores deben ser positivos.")
        
        # Calcula la integral utilizando la suma de Riemann
        resultado = suma_riemann(a, n)
        # Muestra el resultado en una ventana emergente
        messagebox.showinfo("Resultado", f"El valor aproximado de la integral es: {resultado}")

        # Generación de los datos para la gráfica 3D de la función
        x = np.linspace(-a, a, 100)  # Genera 100 puntos equidistantes para el eje x
        y = np.linspace(-a, a, 100)  # Genera 100 puntos equidistantes para el eje y
        X, Y = np.meshgrid(x, y)  # Crea una malla de puntos a partir de los valores de x e y
        Z = f(X, Y)  # Evalúa la función f(x, y) en cada punto de la malla

        # Configuración de la figura y el gráfico en 3D
        fig = plt.figure()  # Crea una figura para la gráfica
        ax = fig.add_subplot(111, projection='3d')  # Añade un subplot 3D al espacio de la figura
        ax.plot_surface(X, Y, Z, cmap='viridis')  # Dibuja la superficie en 3D con un mapa de colores
        ax.set_title('Superficie de la función f(x, y)')  # Título de la gráfica
        ax.set_xlabel('x')  # Etiqueta para el eje x
        ax.set_ylabel('y')  # Etiqueta para el eje y
        ax.set_zlabel('f(x, y)')  # Etiqueta para el eje z
        plt.show()  # Muestra la gráfica

    except ValueError as e:
        # Si hay un error en los valores ingresados (por ejemplo, un valor no numérico o negativo)
        messagebox.showerror("Error", f"Error: {e}")

# Configuración de la ventana principal de la aplicación Tkinter
ventana = tk.Tk()
ventana.title("Cálculo de la Integral")  # Título de la ventana

# Etiquetas y entradas para los parámetros 'a' y 'n'
tk.Label(ventana, text="Valor de a:").grid(row=0, column=0)  # Etiqueta para el valor de 'a'
entrada_a = tk.Entry(ventana)  # Entrada de texto para el valor de 'a'
entrada_a.grid(row=0, column=1)  # Ubica la entrada de 'a' en la ventana

tk.Label(ventana, text="Número de subintervalos:").grid(row=1, column=0)  # Etiqueta para 'n'
entrada_n = tk.Entry(ventana)  # Entrada de texto para el número de subintervalos 'n'
entrada_n.grid(row=1, column=1)  # Ubica la entrada de 'n' en la ventana

# Botón para realizar el cálculo
boton_calcular = tk.Button(ventana, text="Calcular", command=calcular)  # Al hacer clic en este botón, se ejecuta la función 'calcular'
boton_calcular.grid(row=2, columnspan=2)  # Coloca el botón en la ventana

# Inicia el ciclo principal de la interfaz gráfica
ventana.mainloop()