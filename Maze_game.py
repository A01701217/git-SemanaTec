from random import choice
from turtle import *

from freegames import floor, vector

state = {'score': 0} #Seguimiento puntuacion juego
path = Turtle(visible=False) #
writer = Turtle(visible=False)#Puntuacion del juego
aim = vector(5, 0) #Dirección inicial a la que se dirigira pacman
pacman = vector(-40, -80) #Posicion en la que inicia pacman

#Posicion inicial de los fantasmas y direccion a la que se dirigen
ghosts = [
    [vector(-180, 160), vector(5, 0)],
    [vector(-180, -160), vector(0, 5)],
    [vector(100, 160), vector(0, -5)],
    [vector(100, -160), vector(-5, 0)],
]
# fmt: off
#Tablero, indicandonos las partes que tendran vacio, puntos o pared
tiles = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
    0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
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
    path.color('blue') #Color del camino caminable

    for index in range(len(tiles)):
        tile = tiles[index]

        if tile > 0: #Condición para iluminar los cuadros del mundo segun su valor
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            square(x, y)

            if tile == 1: #Condición para poner los puntitos de comida
                path.up()
                path.goto(x + 10, y + 10)
                path.dot(5, 'white')


def move():
    """Move pacman and all ghosts."""
    writer.undo() #Se borra el estado anterior de la puntuación
    writer.write(state['score']) #Se actualiza la puntuación

    clear() #Refrescamiento de la pantalla

    if valid(pacman + aim): #Se verifica si la posicion a la que se intenta mover es valida
        pacman.move(aim) #Se mueve a pacman de posicion a donde se pretende

    index = offset(pacman) #Se ubica en donde se encuentra pacman y actualiza el estado

    if tiles[index] == 1: #Condicional para poder actualizar el estado del tile tras comerse una bolita
        tiles[index] = 2 #Se actualiza el valor del tile
        state['score'] += 1 #Se suma la puntuacion
        x = (index % 20) * 20 - 200 
        y = 180 - (index // 20) * 20
        square(x, y)

    up() #Dibujado de la esferita que representa a patman
    goto(pacman.x + 10, pacman.y + 10) #Posicion del centro de pacman
    dot(20, 'yellow') #tamaño y color de pacman

    for point, course in ghosts: #Accionar de cada uno de los fantasmas
        if valid(point + course): #Se verifica si el fantasma va a una posicion correcta
            point.move(course)
        else:
            options = [ #Movimientos de los fantasmas
                vector(15, 0),
                vector(-15, 0),
                vector(0, 15),
                vector(0, -15),
            ]
            dis = pacman- point
            if (dis.x>0 and dis.y>0) and (valid(point+vector(10, 0)) or valid(point+vector(0, 10))):
                options = [
                    vector(15, 0),
                    vector(0, 15),
                ] 
            plan = choice(options) #Se elige una de las distintas acciones para ejecutar
            course.x = plan.x
            course.y = plan.y

        up() #posicion y modelo de los fantasmas
        goto(point.x + 10, point.y + 10)
        dot(20, 'green')

    update() #Se refresca toda la pagina

    for point, course in ghosts:
        if abs(pacman - point) < 20: #Si pacman colisiona con un fantasma
            return #Un return que detiene el juego por completo 
            #print("uwu")

    ontimer(move, 100)


def change(x, y): #Cambio de direcciones de pacman
    """Change pacman aim if valid."""
    if valid(pacman + vector(x, y)): #Se revisa si es una casilla en la que puede estar
        aim.x = x #Direccion en x
        aim.y = y #Direccion en y


setup(420, 420, 370, 0) #Se dan los parametros de la figura
hideturtle() #No se muestra la tortuga en el canva
tracer(False) #Hace que todo se muestre automaticamente en lugar de tener que esperar a que se realice uno a uno
writer.goto(160, 160) #Posicion del score
writer.color('white') #Color del score
writer.write(state['score']) #que muestra el score
#Asignacion de teclas
listen() 
onkey(lambda: change(5, 0), 'Right')
onkey(lambda: change(-5, 0), 'Left')
onkey(lambda: change(0, 5), 'Up')
onkey(lambda: change(0, -5), 'Down')
world() #Dibujado del mundo
move() #Dibujado del movimiento
done() 