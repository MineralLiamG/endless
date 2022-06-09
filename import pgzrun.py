import pgzrun
import random

WIDTH = 800
HEIGHT = 400

desertback1 = Actor('desertback')
desertback1.topleft = 0,0
desertback2 = Actor('desertback')
desertback2.topleft = 799,0

dinolaufen1 = Actor('run1')
dinolaufen2 = Actor('run2')
dinolaufen3 = Actor('run3')
dinolaufen4 = Actor('run4')
dinolaufen5 = Actor('run5')
dinolaufen6 = Actor('run6')
dinolaufen7 = Actor('run7')
dinolaufen8 = Actor('run8')

def update():
    desertback1.x -=1
    desertback2.x -=1
    Kaktus.x -= 1
    if desertback1.x <= -400:
        desertback1.x = 1199
    elif desertback2.x <= -400:
        desertback2.x = 1199
    elif Kaktus.x <= -20:
        Kaktus.x = 818

spielaktiv = True

Kaktus = Actor('cactus')
Kaktus.y = 315
Kaktus.x = 700


def draw():
    screen.clear()
    desertback1.draw()
    desertback2.draw()
    Kaktus.draw()
    dinolaufen1.draw()

while spielaktiv:
    


pgzrun.go()