
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
        self.image.fill((228,204,190,0))
        
        self.degrade = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
        self.degrade.fill((0,0,0,int(0.09 * posY)))
                                     
        self.degrade_lumiere = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
        coef_degrade = min(50,0.1*posY)
        self.degrade_lumiere.fill((255,255,150,int(50-coef_degrade)))
        
        self.contour = pygame.image.load((os.path.join('image/brique', 'brique_grise.png'))).convert_alpha()
        self.color = (228,204,190,0)
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
           self.image =  pygame.Surface((self.rect.width, self.rect.height))
           self.image.fill((228,204,190,0)) #transparent
           #self.degrade.fill((0,0,0,int(0.09 * self.rect.y)))
       else:
           if color == 'rouge':
                self.image = pygame.image.load((os.path.join('image/brique', 'brique_rouge.png'))).convert()
                #self.degrade.fill((102,0,0,int(0.2 * self.rect.y)))
           if color == 'vert':
                self.image = pygame.image.load((os.path.join('image/brique', 'brique_verte.png'))).convert()         
               # self.degrade.fill((0,35,0,int(0.2 * self.rect.y)))
           if color == 'bleu':
                self.image = pygame.image.load((os.path.join('image/brique', 'brique_bleu.png'))).convert()   
                #self.degrade.fill((17,33,62,int(0.2 * self.rect.y)))
           if color == 'jaune':   
                self.image = pygame.image.load((os.path.join('image/brique', 'brique_jaune.png'))).convert()
               # self.degrade.fill((125,80,0,int(0.2 * self.rect.y)))
                
          