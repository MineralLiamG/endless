import pgzrun
from pgzhelper import *
import random

WIDTH = 800
HEIGHT = 400

desertback1 = Actor('desertback')
desertback1.topleft = 0,0
desertback2 = Actor('desertback')
desertback2.topleft = 799,0

dino = Actor('idle1')
dino.images = ['run1','run2','run3','run4','run5','run6','run7','run8']
dino.fps = 10

def update():
    dino.animate()
    desertback1.x -=1
    desertback2.x -=1
    Kaktus.x -= 1
    if desertback1.x <= -400:
        desertback1.x = 1199
    elif desertback2.x <= -400:
        desertback2.x = 1199
    elif Kaktus.x <= -20:
        Kaktus.x = 818
        gameover

Kaktus = Actor('cactus')
Kaktus.y = 315
Kaktus.x = 700
dino.y = 315

def gameover():
    if dino.colliderect(Kaktus):
        dino.image = "dead8"
       
def draw():
    screen.clear()
    desertback1.draw()
    desertback2.draw()
    Kaktus.draw()
    dino.draw()

pgzrun.go()