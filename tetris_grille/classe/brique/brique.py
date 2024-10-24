
from cmath import rect
import os
import pygame
import math


class Brique(pygame.sprite.Sprite):
    def __init__(self,ligne: int,colonne: int, ligne_max: int, colonne_max: int):
        pygame.sprite.Sprite.__init__(self)
        self.ligne = ligne
        self.colonne = colonne
        self.ligne_max = ligne_max
        self.colonne_max = colonne_max
        self.vitesse = 1
     
    def acceleration(self):
        self.vitesse += 1
        
    def descente(self):
        self.ligne += 1
        
    def translation(self, sens: int):
        self.colonne +=  sens   
        
    def reposition(self, ligne: int, colonne: int):
        self.ligne = ligne
        self.colonne = colonne
            
    def getColonne(self) -> int:
        return self.colonne
    
    def getLigne(self) -> int:
        return self.ligne