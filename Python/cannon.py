"""Cannon, hitting targets with projectiles.

Exercises

1. Keep score by counting target hits.
2. Vary the effect of gravity.
3. Apply gravity to the targets.
4. Change the speed of the ball.

Author: Santiago Rodarte, Aquiles Ensminger, Rafael Ríos
"""

from random import randrange
from turtle import *
from freegames import vector
state={"score":0}
writer= Turtle(visible=False)
ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199

	#Changed values in the formulas to make speed greater (from 200 to 300)
        speed.x = (x + 300) / 25 
        speed.y = (y + 300) / 25

def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    "Draw ball and targets."
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'green')

    if inside(ball):
        goto(ball.x, ball.y)
	#Changed the color of the ball form red to black
        dot(6, 'black')

    update()

def move():
    "Move ball and targets."
    # Generate a new target at random times
    writer.undo()
    writer.write(state["score"]) 
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    # Move the existing targets
    for target in targets:
        target.x -= 0.8
        target.y -= 0.6
    # Move the cannon shot
    if inside(ball):
        speed.y -= 0.55
        ball.move(speed)

    # Make a copy of the existing target list before redrawing
    dupe = targets.copy()
    targets.clear()

    # Detect if the bullet hits a target
    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)
        if abs(target-ball)<=13:    
            state["score"]+=1

    draw()

    # Detect when a target reaches the left side
    for target in targets:
        if not inside(target):
            #targets.remove(target)
            return

    ontimer(move, 50)

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
