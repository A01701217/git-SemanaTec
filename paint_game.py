"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""

from turtle import *
from freegames import vector

# Funcion para dibujar una linea desde start hasta end
def line(start, end):
    up()              # No dibuja
    goto(start.x, start.y)  # Mover a la posición inicial
    down()            # Dibuja
    goto(end.x, end.y)      # Movera la posición final

#Funcion para dibujar un cuadrado de area (lado*4)
def square(start, end):
    """Draw square from start to end."""
    up() #No dibuja
    goto(start.x, start.y) #Mover a posicion inicial
    down() #dibuja
    begin_fill() #Se indica que una figura siendo dibujada se rellenara

    for count in range(4): #Se realiza una linea 4 veces volteando siempre a la izquierda para realizar el cuadrado
        forward(end.x - start.x)
        left(90)

    end_fill() #Rellena la figura dibujada


def circle(start, end):
    """Draw circle from start to end."""
    pass  # TODO


def rectangle(start, end):
    """Draw rectangle from start to end."""
    pass  # TODO


def triangle(start, end):
    """Draw triangle from start to end."""
    pass  # TODO

# Funcion para guardar punto de inicio e indicar la figura a dibujar
def tap(x, y):
    start = state['start']  # Obtiene el punto inicio

    if start is None:       # No existe punto incio
        state['start'] = vector(x, y)  # Almacena punto de inicio
    else:
        shape = state['shape']  # Figura a dibujar
        end = vector(x, y)      # Donde termina la figura
        shape(start, end)       # Dibuja la forma  punto inicio y punto final
        state['start'] = None  # Reinicia punto inicio

# Definir una función "store" para almacenar un valor en el estado con una clave
def store(key, value):
    state[key] = value  # Almacena el valor de estado

state = {'start': None, 'shape': line} # El estado inicial no existe y de default esta el dibujo con lineas

setup(420, 420, 370, 0) # Tamaño del canva

onscreenclick(tap) # Asocia "tap" con clicks en la pantalla

listen()

# Configura atajos de teclado para diferentes acciones
onkey(undo, 'u')                # Deshacer accion con u
onkey(lambda: color('black'), 'K')  # Cambia el color a negro con la tecla 'K'
onkey(lambda: color('white'), 'W')  # Cambia el color a blanco con la tecla 'W'
onkey(lambda: color('green'), 'G')  # Cambia el color a verde con la tecla 'G'
onkey(lambda: color('blue'), 'B')    # Cambia el color a azul con la tecla 'B'
onkey(lambda: color('red'), 'R')     # Cambia el color a rojo con la tecla 'R'
onkey(lambda: color('purple'), 'P')     # Cambia el color a morado con la tecla 'P'
onkey(lambda: color('lime'), 'L')     # Cambia el color a lima con la tecla 'L'
onkey(lambda: store('shape', line), 'l')        # Se indica que se dibujaran lineass
onkey(lambda: store('shape', square), 's')      # Se indica que se dibujaran cuadrados
onkey(lambda: store('shape', circle), 'c')      # Se indica que se dibujaran circulos
onkey(lambda: store('shape', rectangle), 'r')   # Se indica que se dibujaran rectangulos
onkey(lambda: store('shape', triangle), 't')    # Se indica que se dibujaran triangulos

done() #Se termina congiguración