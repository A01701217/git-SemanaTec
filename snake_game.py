"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange
from turtle import *

from freegames import square, vector

import random

food = vector(0, 0) #Posicion inicial de la comida
snake = [vector(10, 0)] #Posicion inicial de la serpiente
aim = vector(0, -10) #Direccion inicial a la que se dirige la serpiente
count = vector(0,0) #Contador de movimientos para saber a donde se dirigira la comida

def change(x, y): #Funcion para poder cambiar la dirección de la serpiente
    """Change snake direction."""
    aim.x = x #Dirección en x
    aim.y = y #Dirección en y

def inside(head): #Función para saber si la serpiente esta dentro del mapa
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190

def cambiarcolor(): #Funcion para elegir un color aleatorio que tendra la serpiente al iniciar el juego
    numero_aleatorio = random.randint(1, 5) 
    #Los colores se eligen
    if numero_aleatorio == 1:
        colorserp = 'black'
    elif numero_aleatorio == 2:
        colorserp = 'pink'
    elif numero_aleatorio == 3:
        colorserp = 'blue'
    elif numero_aleatorio == 4:
        colorserp = 'lime'
    elif numero_aleatorio == 5:
        colorserp = 'purple'
    return colorserp

colores = cambiarcolor()  # Genera un color aleatorio único al comienzo del juego

def move():  #Funcion la cual indica el como se movera la serpiente
    head = snake[-1].copy()  #Representa una copia de la cabeza de la serpiente
    head.move(aim) #direccion a la cual se dirige la serpiente

    if not inside(head) or head in snake: #Condicion la cual checa si la serpiente esta en los limites o dentro de si misma, si se cumple pierdes.
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head) #Se unen las piezas de serpiente

    if head == food:#Condicion para saber si se comio comida y alargar la serpiente
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear() #Se reinicia la pantalla para un refresh
    if count.x % 2 == 0: #Movimiento de la comida en x
        if -200 < food.x < 190:
            food.x += randrange(-1, 2) * 10
        elif food.x == -200:
            food.x += 50
        elif food.x == 190:
            food.x -= 50

        if -200 < food.y < 190: #Movimiento de la comida en y
            food.y += randrange(-1, 2) * 10
        elif food.y == -200:
            food.y += 50
        elif food.y == 190:
            food.y -= 50


    for body in snake:
        square(body.x, body.y, 9, colores)  # Utiliza el color aleatorio generado
    square(food.x, food.y, 9, 'green') 
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0) #Canva
hideturtle() #No se muestra la tortuga
tracer(False) #no se muestra el como se dibuja
#Asignacion de teclas
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()