
from ast import Try
from cmath import rect
import os
from symbol import try_stmt
from winreg import SetValue
import pygame
import math
import numpy as np
import copy

import classe.case.Case as Case

class Grille(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(0,0,1000,1000)
        self.image =  pygame.Surface((self.rect.width, self.rect.height))
        hauteur_case = 50
        largeur_case = 50
        self.nb_case_hauteur = int(self.rect.height / hauteur_case)
        self.nb_case_largeur = int(self.rect.width / hauteur_case)
        
        #liste contenant les infos du cases de la grille
        self.l_cases = np.full((self.nb_case_hauteur, self.nb_case_largeur), None, dtype=object) #sert a l affichage
        self.l_cases_occupe = np.full((self.nb_case_hauteur, self.nb_case_largeur), None, dtype=object) #sert a la detection des cases occupees #aurait peut pu etre eviter si on donne au case "player actuel" la valeur 2 et non 1 car avec 1 il se bloque tt seul comme compose de plusieurs briques
        
        #initialisation des cases de la grille
        y = 0
        for y in range(self.nb_case_hauteur):
            x = 0
            for colonne in range(self.nb_case_largeur):
                case_x = 25 + 50*x
                case_y = 25 + 50*y
                self.l_cases[y][x] = Case.Case(case_x, case_y)
                self.l_cases_occupe[y][x] = Case.Case(case_x, case_y)
                x += 1
            y += 1

    def getLigneComplete(self) -> int:
        l_ligne = []
        y = 0
        for ligne in self.l_cases_occupe:
            ligne_complete = True
            for colonne in ligne:
                if colonne.getValue() == 0:
                    ligne_complete = False
                    break
            if ligne_complete:
                l_ligne.append(y)
            y += 1
            
        if len(l_ligne) > 0:
            ligne_complete = True   
        return ligne_complete, l_ligne.copy()
    

    def suppLigneComplete(self, ligne): 
        y = ligne 
        while y > 0 :
            x = 0
            while x < self.nb_case_largeur:
                self.l_cases_occupe[y][x].setValue(self.l_cases_occupe[y-1][x].getValue()) 
                self.l_cases_occupe[y][x].setColor(self.l_cases_occupe[y-1][x].getColor())
                self.l_cases[y][x].setValue(self.l_cases[y-1][x].getValue()) 
                self.l_cases[y][x].setColor(self.l_cases[y-1][x].getColor())
                self.l_cases[y][x].colorChange(self.l_cases[y][x].getColor())                    
                x += 1
            y -= 1
                      

    def getNbLigne(self) -> int:
        return self.nb_case_hauteur
    
    def getNbColonne(self) -> int:
        return self.nb_case_largeur
    
    def getCaseOccupe(self, ligne: int, colonne: int) -> int:
        ligne = int(ligne)
        colonne = int(colonne)
        try:
            return self.l_cases_occupe[ligne][colonne].getValue()
        except:
            return 1
      
    
    def setCaseOccupe(self, ligne: int, colonne: int, valeur: int) -> int:
        ligne = int(ligne)
        colonne = int(colonne)
        self.l_cases_occupe[ligne][colonne].setValue(valeur)
        
    
    def changeCaseValue(self, ligne: int, colonne: int, valeur: int):
        ligne = int(ligne)
        colonne = int(colonne)
        self.l_cases[ligne][colonne].setValue(valeur)
    
    def majColor(self, ligne: int, colonne: int, color):
        self.l_cases[ligne][colonne].colorChange(color)
                
    def verifPartiePerdu(self):
        if self.getCaseOccupe(1,10) > 0:
            return True
        return False