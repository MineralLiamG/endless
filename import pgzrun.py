from pickle import FALSE, TRUE
import pgzrun
import random

WIDTH = 800
HEIGHT = 400

game_over = False

desertback1 = Actor('desertback')
desertback1.topleft = 0,0
desertback2 = Actor('desertback')
desertback2.topleft = 799,0

dino = Actor('idle1')
dino.images = ['run1','run2','run3','run4','run5','run6','run7','run8','dead8']
dino.fps = 10


    
def update():
    global game_over
    desertback1.x -=1
    desertback2.x -=1
    Kaktus.x -= 1
    if desertback1.x <= -400:
        desertback1.x = 1199
    elif desertback2.x <= -400:
        desertback2.x = 1199
    elif Kaktus.x <= -20:
        Kaktus.x = 818
   
    if dino.colliderect(Kaktus):
        dino.image = "dead8"
        game_over = TRUE

Kaktus = Actor('cactus')
Kaktus.y = 315
Kaktus.x = 700
dino.y = 300


       



def draw():
    screen.clear()
    desertback1.draw()
    desertback2.draw()
    Kaktus.draw()
    if game_over:
        screen.draw.text('Game Over', centerx=400, centery=270, color=(255,255,255), fontsize=60)
    else:
        dino.draw()
        


pgzrun.go()