#shoots off a color changing projectile at mouse click location

import pygame
from pygame.locals import *
from sys import exit
import math, random

clock = pygame.time.Clock()
global info, black, index
pygame.init()
info = pygame.display.Info()
screen = pygame.display.set_mode((info.current_w,info.current_h))
pygame.display.set_caption('Projectile')

class Proj:
    x = 0
    y = 0
    color = (255,255,255)
    rgb = 0
    size = 0
    
    def __init__(self, x, y, color, rgb, rgbState, size):
        self.x = x
        self.y = y
        self.color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        self.rgb = random.randint(0,2)
        self.rgbState = False
        self.size = info.current_h/100
        
    def shoot(self):
        self.x += self.size/3
        self.y += self.size/3
        colorL = list(self.color)
        if(colorL[self.rgb] < 5):
            self.rgbState = True
        if(colorL[self.rgb] > 250):
            self.rgbState = False
            
        if(self.rgbState == False):
            colorL[self.rgb] -= 5
        else:
            colorL[self.rgb] += 5
        self.color = tuple(colorL)
        pygame.draw.circle(screen, self.color, (self.x, self.y), 5)

screen.fill((255,255,255))
projs = []
black = False
index = 0

while True:
    for event in pygame.event.get():
        #print(event.type, QUIT)
        if event.type == QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.display.quit()
            pygame.quit()
            exit()
            
        if event.type == pygame.MOUSEBUTTONUP:
            x,y = pygame.mouse.get_pos()
            projs.append(Proj(x, y, (255,255,255), 0, False, 0))
            
        for proj in projs:
            proj.shoot()
            
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if black:
                screen.fill((255,255,255))
                black = False
            else:
                screen.fill((0,0,0))
                black = True
            projs.clear()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            pygame.image.save(screen, "screenshot" + str(index) + ".jpeg")
            if black:
                screen.fill((255,255,255))
                black = False
            else:
                screen.fill((0,0,0))
                black = True
            projs.clear()
            index += 1

    pygame.display.update()
    clock.tick(30)