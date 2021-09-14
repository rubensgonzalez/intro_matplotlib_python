# Matplotlib [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de matplotlib
import numpy as np
import matplotlib.pyplot as plt

def plot(x,y,y2):
  
   fig = plt.figure()
   fig.suptitle('Gráfico 1',c='g', fontsize=20)
   ax = fig.add_subplot()    
   ax.plot(x,y1,c='darkblue', label='Eje "X"')
   ax.plot(x,y2,c='darkblue', label='Eje "X"')
   ax.legend()
   ax.grid()
   plt.show()
   
   
   
   

   print("Fin Line Plot")

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    print("Line Plot")

    # NOTA: aproveche los ejemplos "multi_line_plot" de clase

    # Alumno: Se desea graficar varias funciones en un mismmo gráfico (axe)

    # Las funciones que se desean implementar y graficar son:
    # y1 = x**2
    # y2 = x**3

    # Su implementación es la siguiente:
    x = list(np.linspace(-4, 4, 20))

    y1 = []
    for i in x:
        y1.append(i**2)

    y2 = []
    for i in x:
        y2.append(i**3)

    # Realizar un gráfico que representen las dos funciones
    # Para ello se debe llamar dos veces a "plot" con el mismo "ax"
    fig = plt.figure()
    
    ax = fig.add_subplot()

    # Se debe colocar en la leyenda la función que representa
    # cada función
    # Cada función dibujarla con un color distinto
    # a su elección
    
    ax.plot(x, y1, c="r", label="y1 = x**2")
    ax.plot(x, y2, c="b", label="y2 = x**3")
     
    ax.legend()
   
    # Crear acá su gráfico

    plt.show()
    print("terminamos")
