import pygame
from time import sleep
from random import randint


pygame.init()

xEdge,yEdge = 800,800

screen = pygame.display.set_mode((xEdge,yEdge))
logo = 'logo.png'

myimage = pygame.image.load(logo)
imagerect = myimage.get_rect()

#start pos
x = 100
y = 100
speedX = randint(1,5)#first randomed then get new random values
speedY = randint(1,5) 
sizeX,sizeY =  200,200
def logic():
    global x,y,startEdge,endEdge,sizeX,sizeY,speedX,speedY
    
    screen.blit(myimage,(x,y))

    x+=speedX
    y+=speedY
    
    #speedX and Y random values
    randomValue = randint(1,5)

    if x > xEdge-sizeX:
        speedX = -randomValue
    if x < 0:
        speedX = randomValue
    if y > yEdge-sizeY:
        speedY = -randomValue
    if y < 0:
        speedY = randomValue

    print("X: ",x,"Y: ",y,"SpeedX: ",speedX,"SpeedY: ",speedY)

#gameloop
while True:
    sleep(1/30)#30 fps
    screen.fill((0,0,0))
    logic()
    pygame.display.flip()




