from random import choice
from turtle import *

from freegames import floor, vector

path = Turtle(visible=False) #
aim = vector(5, 0) #Dirección inicial a la que se dirigira pacman
pacman = vector(-120, -100) #Posicion en la que inicia pacman (Juego normal)
#pacman = vector(160, 80) #Posicion en la que inicia pacman (Juego normal) (Win automatica)

# fmt: off
#Tablero, indicandonos las partes que tendran vacio, puntos o pared
tiles = [
    #1 2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20
    1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0,
    0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0,
    0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0,
    0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0,
    0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 3, 1, 0,
    0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0,
    0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0,
    0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0,
    0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0,
    0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0,
    0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0,
    0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0,
    0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0,
    0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0,
    0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,

]
# fmt: on


def square(x, y): #Dibujado de las casillas
    """Draw square using path at (x, y)."""
    path.up() #No se dibuja
    path.goto(x, y) #Se dirige a la posicion en la que comienza el dibujo
    path.down() #Se habilita el dibujado
    path.begin_fill() #Se indica que la figura se rellenara

    for count in range(4): #Se dibuja un cuadro de 20x20 unidades
        path.forward(20)
        path.left(90)

    path.end_fill() #Se rellena la figura
  


def offset(point): #Se convierten coordenadas en un indice
    """Return offset of point in tiles."""
    x = (floor(point.x, 20) + 200) / 20 #Coordenada en x
    y = (180 - floor(point.y, 20)) / 20 #Coordenada en Y
    index = int(x + y * 20) #Se guarda el indice de la casilla
    return index


def valid(point): #Esta funcion nos indicara si la casilla es para poder estar en ella
    """Return True if point is valid in tiles."""
    index = offset(point) #Se revisa la validez de la casilla

   

    if tiles[index] == 0: #La casilla es una pared
        return False

    index = offset(point + 19) #Se extiende hasta la ultima parte de la casilla

    if tiles[index] == 0: #Se vuelve pared esa parte igualmente
        return False

    return point.x % 20 == 0 or point.y % 20 == 0


def world(): #Se ilustra como luciria el mundo pacman
    """Draw world using path."""
    bgcolor('black') #Color de fondo
    #path.color('blue') #Color del camino caminable

    for index in range(len(tiles)):
        tile = tiles[index]

        if tile > 0: #Condición para iluminar los cuadros del mundo segun su valor
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            square(x, y)
            if tile == 1:
              path.up()
              path.color('gray')
            elif tile == 3:
              path.up()
              path.color('green')


def move():
    """Move pacman."""

    clear() #Refrescamiento de la pantalla

    if valid(pacman + aim): #Se verifica si la posicion a la que se intenta mover es valida
        pacman.move(aim) #Se mueve a pacman de posicion a donde se pretende
    else:
        print("):  !!!!You lose!!! :(") #termina el juego si chocas contra la pared-
        return
    
    index = offset(pacman) #Se ubica en donde se encuentra pacman y actualiza el estado

    if tiles[index] == 3: #Condicional para terminar el juego si se llega a la meta
        print("(;  !!!!you won!!!!!! ;)")
        return
        

    

    up() #Dibujado de la esferita que representa a patman
    goto(pacman.x + 10, pacman.y + 10) #Posicion del centro de pacman
    dot(10, 'yellow') #tamaño y color de pacman



    ontimer(move, 100)


def change(x, y): #Cambio de direcciones de pacman
    """Change pacman aim if valid."""
    if valid(pacman + vector(x, y)): #Se revisa si es una casilla en la que puede estar
        aim.x = x #Direccion en x
        aim.y = y #Direccion en y


setup(420, 420, 370, 0) #Se dan los parametros de la figura
hideturtle() #No se muestra la tortuga en el canva
tracer(False) #Hace que todo se muestre automaticamente en lugar de tener que esperar a que se realice uno a uno

#Asignacion de teclas
listen() 
onkey(lambda: change(5, 0), 'Right')
onkey(lambda: change(-5, 0), 'Left')
onkey(lambda: change(0, 5), 'Up')
onkey(lambda: change(0, -5), 'Down')
world() #Dibujado del mundo
move() #Dibujado del movimiento
done() 