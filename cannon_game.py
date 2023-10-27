"""Cannon, hitting targets with projectiles.

Exercises

1. Keep score by counting target hits.
2. Vary the effect of gravity.
3. Apply gravity to the targets.
4. Change the speed of the ball.
"""

from random import randrange
from turtle import *

from freegames import vector

ball = vector(-200, -200) #Posicion original de la pelota
speed = vector(0, 0) #Velocidad inicial de la pelota
targets = [] #Vector para la posicion de los objetivos


def tap(x, y):
    """Respond to screen tap."""
    if not inside(ball): #Se verifica si pelota esta fuera de la pantalla
        ball.x = -199 #Pelota en la esquina inferior izquierda
        ball.y = -199
        speed.x = (x + 200) / 10 #Aqui cambiamos la velocidad de los proyectiles antes se dividia entre 25 ahora entre 10
        speed.y = (y + 200) / 10#Aqui cambiamos la velocidad de los proyectiles


def inside(xy):
    """Return True if xy within screen."""
    return -200 < xy.x < 200 and -200 < xy.y < 200 #Verficar si esta dentro de los limites


def draw():
    """Draw ball and targets."""
    clear()

    for target in targets: #Se genera un nuevo target
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball): #Se genera la bolita proyectil
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()


def move():
    """Move ball and targets."""
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 3.5 #aqui cambiamos la velocidad de los targets.

    if inside(ball):
        speed.y -= .35
        ball.move(speed)

    dupe = targets.copy()  #copiar lista de targets
    targets.clear() #Se vacia la lista

    for target in dupe: #Distancia entre pelota y objetivo
        if abs(target - ball) > 13:
            targets.append(target) #Si la distancia es mayor a 13 el target se mantiene

    draw() #Se dibujan targets y pelotita

    for target in targets: #Si el target llega al final entonces se termina el juego
        if not inside(target):
            return

    ontimer(move, 50)


setup(420, 420, 370, 0) #Canva
hideturtle() #Ocultar la toruga
up()
tracer(False) #No se muestra el proceso de dibujo
onscreenclick(tap) #Control con el tap
move() #Movimiento
done()