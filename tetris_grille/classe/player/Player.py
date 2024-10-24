
from cmath import rect
import os
import pygame
import math
import copy
import random

import classe.brique.brique as Brique


class Player(pygame.sprite.Sprite):
    def __init__(self, ligne_max: int, colonne_max: int, vitesse: int):
        pygame.sprite.Sprite.__init__(self)
        self.ligne = 1
        self.colonne = int(colonne_max/2)
        self.ligne_max = ligne_max
        self.colonne_max = colonne_max
        self.l_brique = []
        self.actif = True
        self.createPlayer()
        self.vitesse = vitesse
        self.color = (0,0,0,0)
        self.setColor()
        
        
    def createPlayer(self):
        self.l_brique.append(Brique.Brique(self.ligne, self.colonne, self.ligne_max, self.colonne_max))
    
    def tirage(self, min_val, max_val, precedent):
        while True:
            choix = random.randint(min_val, max_val)
            if choix != precedent:
                return choix
        
    def setColor(self):
        choix = random.randint(0, 3)
        
        if choix  == 0 :
            self.color = (204,0,0,150) #rouge
        if choix  == 1 :
            self.color = (0,70,0,110) #vert
        if choix  == 2 :
            self.color = (34,66,124,124) #bleu
        if choix  == 3 :
            self.color = (250,160,0,150) #jaune
            
    def getColor(self):
        return self.color
    
    def translation(self, sens: int): 
        for brique in self.l_brique:
            brique.translation(sens)
           
    def acceleration(self):
        for brique in self.l_brique:
                brique.acceleration()
        self.vitesse += 1    
        
    def descente(self):
        for brique in self.l_brique:
                brique.descente()

    def desactive(self):
        self.actif = False           

                
    def getPosActuelle(self):
        return copy.deepcopy(self.l_brique)
    
    def rotationGauche(self, l_brique):
         pass
    def rotationDroite(self, l_brique):
         pass
    
    def controleRotationGauche(self):
         return copy.deepcopy(self.l_brique)
    
    def controleRotationDroite(self):
         return copy.deepcopy(self.l_brique)
    
    def getVitesse(self) -> int:
        return self.vitesse


class Cube(Player):
     def __init__(self, ligne_max: int, colonne_max: int, vitesse: int):
        super().__init__(ligne_max, colonne_max, vitesse)
        self.type = 1
        
     def createPlayer(self):
        self.l_brique.append(Brique.Brique(self.ligne, self.colonne, self.ligne_max, self.colonne_max))
        self.l_brique.append(Brique.Brique(self.ligne, self.colonne+1, self.ligne_max, self.colonne_max))
        self.l_brique.append(Brique.Brique(self.ligne+1, self.colonne, self.ligne_max, self.colonne_max))
        self.l_brique.append(Brique.Brique(self.ligne+1, self.colonne+1, self.ligne_max, self.colonne_max))
        
    
     

class Barre(Player):
     def __init__(self, ligne_max: int, colonne_max: int, vitesse: int):
        super().__init__(ligne_max, colonne_max, vitesse)
        self.type = 2
        
     def createPlayer(self):
        i = 0
        while i < 4:
            self.l_brique.append(Brique.Brique(self.ligne, self.colonne + i, self.ligne_max, self.colonne_max))
            i += 1       
     
     def rotationGauche(self, l_brique):
         self.l_brique = copy.deepcopy(l_brique)
     
             
     def rotationDroite(self, l_brique):
         self.l_brique = copy.deepcopy(l_brique)
         
             
     def controleRotationGauche(self):
         l_futur_brique = copy.deepcopy(self.l_brique)
         
         ligneRotation = l_futur_brique[0].getLigne()
         colonneRotation = l_futur_brique[0].getColonne()
         colonne2 = l_futur_brique[1].getColonne()
         if colonneRotation < colonne2:
             for i, brique in enumerate(l_futur_brique):                 
                 brique.reposition(brique.getLigne() + i,brique.getColonne() - i) 
         else:
             for i, brique in enumerate(l_futur_brique):
                 brique.reposition(brique.getLigne() -i ,brique.getColonne() + i)
                 
         return l_futur_brique
     

     def controleRotationDroite(self):
         l_futur_brique = copy.deepcopy(self.l_brique)
         
         ligneRotation = l_futur_brique[-1].getLigne()
         colonneRotation = l_futur_brique[-1].getColonne()
         colonne2 = l_futur_brique[1].getColonne()
         if colonneRotation > colonne2:
             print('toto')
             for i, brique in enumerate(l_futur_brique):
                 print('i',i)
                 print('avant brique.getLigne() ', brique.getLigne())
                 brique.reposition(brique.getLigne() - i +1,brique.getColonne() + i -1 )
                 print('apres brique.getLigne() ', brique.getLigne())
         else:
             print('tata')
             for i, brique in enumerate(l_futur_brique):
                 print('i',i)
                 print('avant brique.getLigne() ', brique.getLigne())
                 brique.reposition(brique.getLigne() -i ,brique.getColonne() + i-4)
                 print('apres brique.getLigne() ', brique.getLigne())
                 
         return l_futur_brique        
     

class L(Player):
     def __init__(self, ligne_max: int, colonne_max: int, vitesse: int):
        super().__init__(ligne_max, colonne_max, vitesse)
        self.type = 3
        
     def createPlayer(self):
        self.l_brique.append(Brique.Brique(self.ligne, self.colonne, self.ligne_max, self.colonne_max))
        self.l_brique.append(Brique.Brique(self.ligne, self.colonne+1, self.ligne_max, self.colonne_max))
        self.l_brique.append(Brique.Brique(self.ligne, self.colonne+2, self.ligne_max, self.colonne_max))
        self.l_brique.append(Brique.Brique(self.ligne+1, self.colonne, self.ligne_max, self.colonne_max))
             
     def rotationGauche(self, l_brique):
         self.l_brique = copy.deepcopy(l_brique)
     
     def rotationDroite(self, l_brique): 
         self.l_brique = copy.deepcopy(l_brique)
                
             
     def controleRotationGauche(self):
         l_futur_brique = copy.deepcopy(self.l_brique)
         
         ligneRotation = l_futur_brique[1].getLigne()
         colonneRotation = l_futur_brique[1].getColonne()
         colonneProtu = l_futur_brique[-1].getColonne()
         ligneProtu = l_futur_brique[-1].getLigne()
         
         if ligneProtu >  ligneRotation:
             if colonneProtu > colonneRotation:
                 for i, brique in enumerate(l_futur_brique):
                      if i < 3:
                          brique.reposition(brique.getLigne() + i - 1,brique.getColonne() + i - 1)
                      else:
                          brique.reposition(ligneProtu ,colonneProtu - 2)         
             else:
                 for i, brique in enumerate(l_futur_brique):
                     if i < 3:
                        brique.reposition(brique.getLigne() + i - 1,brique.getColonne()  + 1 - i)
                     else:
                        brique.reposition(ligneProtu - 2,colonneProtu)
         else: 
             if colonneProtu > colonneRotation:
                 for i, brique in enumerate(l_futur_brique):
                     if i < 3:
                        brique.reposition(brique.getLigne() + 1 - i  ,brique.getColonne() + i - 1 )
                     else:
                        brique.reposition(ligneProtu + 2,colonneProtu)
             else:
                 for i, brique in enumerate(l_futur_brique):
                      if i < 3:
                          brique.reposition(brique.getLigne() + 1 - i,brique.getColonne()  + 1 - i)
                      else:
                          brique.reposition(ligneProtu ,colonneProtu + 2)
                 
         return l_futur_brique
     

     def controleRotationDroite(self):
         l_futur_brique = self.controleRotationGauche()
                 
         return l_futur_brique        





class L_inv(Player):
     def __init__(self, ligne_max: int, colonne_max: int, vitesse: int):
        super().__init__(ligne_max, colonne_max, vitesse)
        self.type = 3
        
     def createPlayer(self):
        self.l_brique.append(Brique.Brique(self.ligne, self.colonne, self.ligne_max, self.colonne_max))
        self.l_brique.append(Brique.Brique(self.ligne, self.colonne+1, self.ligne_max, self.colonne_max))
        self.l_brique.append(Brique.Brique(self.ligne, self.colonne+2, self.ligne_max, self.colonne_max))
        self.l_brique.append(Brique.Brique(self.ligne+1, self.colonne+2, self.ligne_max, self.colonne_max))
             
     def rotationGauche(self, l_brique):
         self.l_brique = copy.deepcopy(l_brique)
     
     def rotationDroite(self, l_brique): 
         self.l_brique = copy.deepcopy(l_brique)
                
             
     def controleRotationGauche(self):
         l_futur_brique = copy.deepcopy(self.l_brique)
         
         ligneRotation = l_futur_brique[1].getLigne()
         colonneRotation = l_futur_brique[1].getColonne()
         colonneProtu = l_futur_brique[-1].getColonne()
         ligneProtu = l_futur_brique[-1].getLigne()
         
         if ligneProtu >  ligneRotation:
             if colonneProtu > colonneRotation:
                 for i, brique in enumerate(l_futur_brique): 
                      if i < 3:
                          brique.reposition(brique.getLigne() + i - 1,brique.getColonne() - i + 1)
                      else:
                          brique.reposition(ligneProtu ,colonneProtu - 2)   
             else:
                 for i, brique in enumerate(l_futur_brique):
                     if i < 3:
                        brique.reposition(brique.getLigne() + 1 -i,brique.getColonne() + 1 -i)
                     else:
                        brique.reposition(ligneProtu - 2,colonneProtu)
         else: 
             if colonneProtu > colonneRotation:
                 for i, brique in enumerate(l_futur_brique):
                     if i < 3:
                        brique.reposition(brique.getLigne() + i - 1,brique.getColonne()  + i - 1)
                     else:
                        brique.reposition(ligneProtu + 2,colonneProtu)
             else:
                 for i, brique in enumerate(l_futur_brique):
                      if i < 3:
                          brique.reposition(brique.getLigne() - i +  1,brique.getColonne()  + i - 1)
                      else:
                          brique.reposition(ligneProtu ,colonneProtu + 2)
                 
         return l_futur_brique
     

     def controleRotationDroite(self):
         l_futur_brique = self.controleRotationGauche()
                 
         return l_futur_brique   
     






class T(Player):
     def __init__(self, ligne_max: int, colonne_max: int, vitesse: int):
        super().__init__(ligne_max, colonne_max, vitesse)
        self.type = 4
        
     def createPlayer(self):
        self.l_brique.append(Brique.Brique(self.ligne, self.colonne, self.ligne_max, self.colonne_max))
        self.l_brique.append(Brique.Brique(self.ligne, self.colonne+1, self.ligne_max, self.colonne_max))
        self.l_brique.append(Brique.Brique(self.ligne, self.colonne+2, self.ligne_max, self.colonne_max))
        self.l_brique.append(Brique.Brique(self.ligne+1, self.colonne+1, self.ligne_max, self.colonne_max))           
     
     def rotationGauche(self, l_brique):
         self.l_brique = copy.deepcopy(l_brique)      

     def rotationDroite(self, l_brique):
         self.l_brique =  copy.deepcopy(l_brique)
         

     def controleRotationGauche(self):
         l_futur_brique = copy.deepcopy(self.l_brique)
         
         ligneRotation = l_futur_brique[1].getLigne()
         colonneRotation = l_futur_brique[1].getColonne()
         colonneProtu = l_futur_brique[-1].getColonne()
         ligneProtu = l_futur_brique[-1].getLigne()
         if ligneProtu >  ligneRotation:
                for i, brique in enumerate(l_futur_brique):
                    if i < 3:
                        brique.reposition(brique.getLigne() + i - 1,brique.getColonne()  + 1 - i)
                    else:
                        brique.reposition(ligneProtu - 1,colonneProtu - 1)       
         if colonneProtu > colonneRotation:
                 for i, brique in enumerate(l_futur_brique):
                     if i < 3:
                        brique.reposition(brique.getLigne() + i - 1,brique.getColonne()  + i - 1)
                     else:
                        brique.reposition(ligneProtu + 1,colonneProtu - 1)
         if ligneProtu <  ligneRotation:
                 for i, brique in enumerate(l_futur_brique):
                     if i < 3:
                        brique.reposition(brique.getLigne() + 1 - i,brique.getColonne() + i - 1  )
                     else:
                        brique.reposition(ligneProtu + 1,colonneProtu + 1)
                        
         if colonneProtu < colonneRotation:
                 for i, brique in enumerate(l_futur_brique):
                      if i < 3:
                          brique.reposition(brique.getLigne() + 1 - i,brique.getColonne()   + 1 - i)
                      else:
                          brique.reposition(ligneProtu - 1 ,colonneProtu + 1)
                 
         return l_futur_brique
     

     def controleRotationDroite(self):
         l_futur_brique = self.controleRotationGauche()
                 
         return l_futur_brique        
     






class Z_inv(Player):
     def __init__(self, ligne_max: int, colonne_max: int, vitesse: int):
        super().__init__(ligne_max, colonne_max, vitesse)
        self.type = 4
        
     def createPlayer(self):
        self.l_brique.append(Brique.Brique(self.ligne, self.colonne, self.ligne_max, self.colonne_max))
        self.l_brique.append(Brique.Brique(self.ligne, self.colonne-1, self.ligne_max, self.colonne_max))
        self.l_brique.append(Brique.Brique(self.ligne+1, self.colonne-1, self.ligne_max, self.colonne_max))
        self.l_brique.append(Brique.Brique(self.ligne+1, self.colonne-2, self.ligne_max, self.colonne_max))           
     
     def rotationGauche(self, l_brique):
         self.l_brique = copy.deepcopy(l_brique)      

     def rotationDroite(self, l_brique):
         self.l_brique =  copy.deepcopy(l_brique)
         

     def controleRotationGauche(self):
         l_futur_brique = copy.deepcopy(self.l_brique)
         
         ligneRotation = l_futur_brique[1].getLigne()
         colonneRotation = l_futur_brique[1].getColonne()
         colonneProtu = l_futur_brique[-1].getColonne()
         ligneProtu = l_futur_brique[-1].getLigne()

         if colonneProtu > colonneRotation:
            for i, brique in enumerate(l_futur_brique):
                if i == 0:
                   brique.reposition(brique.getLigne() + 1,brique.getColonne() + 1)
                if i == 2:
                   brique.reposition(brique.getLigne() +1,brique.getColonne()  - 1)
                if i == 3:
                   brique.reposition(ligneProtu ,colonneProtu - 2)
              
         if colonneProtu < colonneRotation:
            for i, brique in enumerate(l_futur_brique):
                if i == 0:
                   brique.reposition(brique.getLigne()- 1,brique.getColonne() - 1)
                if i == 2:
                   brique.reposition(brique.getLigne() - 1,brique.getColonne() + 1)
                if i == 3:
                   brique.reposition(ligneProtu ,colonneProtu + 2)
                 
         return l_futur_brique
     

     def controleRotationDroite(self):
         l_futur_brique = self.controleRotationGauche()
                 
         return l_futur_brique        
     





class Z(Player):
     def __init__(self, ligne_max: int, colonne_max: int, vitesse: int):
        super().__init__(ligne_max, colonne_max, vitesse)
        self.type = 4
        
     def createPlayer(self):
        self.l_brique.append(Brique.Brique(self.ligne, self.colonne, self.ligne_max, self.colonne_max))
        self.l_brique.append(Brique.Brique(self.ligne, self.colonne+1, self.ligne_max, self.colonne_max))
        self.l_brique.append(Brique.Brique(self.ligne+1, self.colonne+1, self.ligne_max, self.colonne_max))
        self.l_brique.append(Brique.Brique(self.ligne+1, self.colonne+2, self.ligne_max, self.colonne_max))           
     
     def rotationGauche(self, l_brique):
         self.l_brique = copy.deepcopy(l_brique)      

     def rotationDroite(self, l_brique):
         self.l_brique =  copy.deepcopy(l_brique)
         

     def controleRotationGauche(self):
         l_futur_brique = copy.deepcopy(self.l_brique)
         
         ligneRotation = l_futur_brique[1].getLigne()
         colonneRotation = l_futur_brique[1].getColonne()
         colonneProtu = l_futur_brique[-1].getColonne()
         ligneProtu = l_futur_brique[-1].getLigne()

         if colonneProtu > colonneRotation:
            for i, brique in enumerate(l_futur_brique):
                if i == 0:
                   brique.reposition(brique.getLigne() - 1,brique.getColonne() + 1)
                if i == 2:
                   brique.reposition(brique.getLigne() - 1,brique.getColonne()  - 1)
                if i == 3:
                   brique.reposition(ligneProtu ,colonneProtu - 2)
              
         if colonneProtu < colonneRotation:
            for i, brique in enumerate(l_futur_brique):
                if i == 0:
                   brique.reposition(brique.getLigne() + 1,brique.getColonne() - 1)
                if i == 2:
                   brique.reposition(brique.getLigne() + 1,brique.getColonne() + 1)
                if i == 3:
                   brique.reposition(ligneProtu ,colonneProtu + 2)
                 
         return l_futur_brique
     

     def controleRotationDroite(self):
         l_futur_brique = self.controleRotationGauche()
                 
         return l_futur_brique        