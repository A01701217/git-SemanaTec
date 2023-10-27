"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

from random import *
from turtle import *

from freegames import path
from freegames import square, vector

car = path('car.gif') #Imagen del coche
tiles = list(range(32)) * 2 #Cada numero se asocia con un par de numeros
state = {'mark': None} #Para mantener el numero asociado al tile
hide = [True] * 64 #Cuadritos ocultados
count= vector(0,0) #Contador par el numero de taps.
WINNER = [False] # esto nos va a indicar si ya gano el jugador 


def square(x, y): #Dibuja un cuadro blanco de borde negro
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y): #Se guarda la posicion de cada cuadrito en sus componentes cardenales
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):  #Convierte  indice de una ficha en coordenadas en el canva
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y): #Deteccion de cuando se da click en la pantalla
    """Update mark and hidden tiles based on tap."""
    spot = index(x, y) #indice del lugar donde se clickeo
    mark = state['mark'] #numero representativo

    if mark is None or mark == spot or tiles[mark] != tiles[spot]: #se confirma si el par es correcto
        state['mark'] = spot
    else: #se confirma que el par es incorrecto
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

    # se agrega una al contador y se muestra para ver las veces que se piico el programa
    count.x += 1
    print("number of taps: " + str(count.x))


def draw():
    """Draw image and tiles."""
    clear() #Reinicio del canva
    goto(0, 0) #Se posiciona en el centro del canva
    shape(car) #Se inserta el dibujo del carro
    stamp() #se pega fijamente el carro

    for count in range(64): #Se oculta el carro detras de 64 tiles
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark'] #Numero del cuadro

    if mark is not None and hide[mark]: #Al abrir un cuadrito se displayea el juego
        x, y = xy(mark)
        up()
        goto(x+10, y)  # Agrega un desplazamiento para centrar el número
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))
        if not any(hide): #if para checar la condicion de si gano el jugador 
            if not WINNER[0]:
                print("You WON the game in " + str(count.x) + "taps")
                WINNER[0] = True

    update() #refrescamiento de pantalla
    ontimer(draw, 100)


shuffle(tiles) #Se combinan los numeros
setup(420, 420, 370, 0) #canva
addshape(car) #dibujo carro
hideturtle() #se oculta la tortuga
tracer(False) #se dibuja al instante
onscreenclick(tap) #control de click
draw() #dibujo
done()