import pygame,sys
from pygame.locals import *

#color
white = (255,255,255)
black = (0,0,0)

pygame.init()
DISPLAY = pygame.display.set_mode((300, 400))
pygame.display.set_caption("First Game")

#image
img = pygame.image.load("4a38243e39c49e3878c9418f37ae07ce.jpg")
img = pygame.transform.scale(img,(30,30))
imgX = 10
imgY = 10
direction = "right"

#FPS, more frame faster
FPS = 30
fpClock = pygame.time.Clock()

DISPLAY.fill(white)
while True:
    DISPLAY.fill(white)
    if direction == "right":
        imgX += 10
        if imgX >= 250:
            direction = "down"
    elif direction == "down":
        imgY += 10
        if imgY >= 250:
            direction = "left"
    elif direction == "left":
        imgX -= 10
        if imgX <= 10:
            direction = "up"
    elif direction == "up":
        imgY -= 10
        if imgY <= 10:
            direction = "right"

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            print(event.key)
            if event.key == K_DOWN:
                direction = "down"
            elif event.key == K_UP:
                direction = "up"
            elif event.key == K_LEFT:
                direction = "left"
            elif event.key == K_RIGHT:
                direction = "right"


    DISPLAY.blit(img,(imgX,imgY))
    pygame.display.update()
    fpClock.tick(FPS)
