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

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
count = vector(0,0)

def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y

def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190

def cambiarcolor():
    numero_aleatorio = random.randint(1, 5) #Generamos un numero aleatorio que representara un color
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

def move():
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()
    if count.x % 2 == 0:
        if -200 < food.x < 190:
            food.x += randrange(-1, 2) * 10
        elif food.x == -200:
            food.x += 50
        elif food.x == 190:
            food.x -= 50

        if -200 < food.y < 190:
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

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()