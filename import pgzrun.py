import pgzrun
import random

WIDTH = 800
HEIGHT = 400

desertback1 = Actor('desertback')
desertback1.topleft = 0,0
desertback2 = Actor('desertback')
desertback2.topleft = 800,0

def update():
    desertback1.x -=1
    desertback2.x +=1
    Kaktus.x -= 1
    if desertback1.x <= -400:
        desertback1.x = 1200
    elif desertback2.x <= -400:
        desertback2.x = 1200

Kaktus = Actor('cactus')
Kaktus.y = 315
Kaktus.x = 700

def draw():
    screen.clear()
    desertback1.draw()
    desertback2.draw()
    Kaktus.draw()




pgzrun.go()