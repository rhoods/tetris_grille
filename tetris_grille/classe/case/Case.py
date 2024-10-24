
from cmath import rect
import os
import pygame
import math


class Case(pygame.sprite.Sprite):
    def __init__(self,posX,posY):
        pygame.sprite.Sprite.__init__(self)
        self.value = 0
        self.rect = pygame.Rect(posX,posY,50,50)
        self.image =  pygame.Surface((self.rect.width, self.rect.height))
        self.image.fill((120,135,150,0))
        self.contour = pygame.image.load((os.path.join('image/brique', 'contours_case_noir.png'))).convert_alpha()
        self.color = (120,135,150,0)
        self.rect.center = (posX,posY)      
     
    def getValue(self) -> int:
        return self.value
    
    def setValue(self, valeur: int):
        self.value = valeur
        
    def getColor(self) -> int:
        return self.color
    
    def setColor(self, color):
        self.color = color

    def colorChange(self, color: tuple):
       self.color = color
       if self.value == 0:
           self.image.fill((120,135,150,0)) #transparent
       else:
           self.image.fill(self.color)
