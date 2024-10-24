
import os
import pygame
import math
import numpy
import random
import copy
#import clock

from pygame.locals import *

import classe.bouton.Bouton as Bouton
import classe.brique.brique as Brique
import classe.case.Case as Case
import classe.grille.Grille as Grille
import classe.player.Player as Player
#import classe.limite.Limite as Limite





def menuJeu():
    pygame.init()
    pygame.key.set_repeat(400,30)
    clock = pygame.time.Clock() #pour gener le frame rate

    fenetreMenu = pygame.display.set_mode((1000, 1000))
    fond = pygame.image.load((os.path.join('image/fond', 'fond.png'))).convert()
    
    boutonJeu = Bouton.Bouton("Jouer",(400,300))
    texteJeu = Bouton.TexteBouton("Jouer",boutonJeu.rect)
    boutonQuitter = Bouton.Bouton("Quitter",(400,450))
    texteQuitter = Bouton.TexteBouton("Quitter",boutonQuitter.rect)
    
    
    fenetreMenu.blit(fond,(0,0))

    jouer = 0
    quitter = 0
    continuer = True
    while continuer :
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get(): 
            if event.type == QUIT:     
                continuer = 0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if boutonJeu.check_click(event.pos):
                    jouer = 1
                    continuer = False
                if boutonQuitter.check_click(event.pos):
                    quitter = 1
                    continuer = False

        
        clock.tick(60) #limite a 60 fps
        #fenetreMenu.blit(fond,(0,0))
        fenetreMenu.blit(boutonJeu.image,boutonJeu.rect)
        fenetreMenu.blit(texteJeu.image,texteJeu.rect)
        fenetreMenu.blit(boutonQuitter.image,boutonQuitter.rect)
        fenetreMenu.blit(texteQuitter.image,texteQuitter.rect)

        pygame.display.update()
    
    if jouer == 1:
        pygame.quit()
        niveau1()
    else:
        pygame.quit()


def tirage(min_val, max_val, precedent):
    while True:
        choix = random.randint(min_val, max_val)
        if choix != precedent:
            return choix

def choixCouleur():
    choix = random.randint(0, 3)
    if choix  == 0 :
        couleur = 'rouge' #(204,0,0,150) #rouge
    if choix  == 1 :
        couleur = 'vert' #(0,70,0,110) #vert
    if choix  == 2 :
        couleur = 'bleu' #(34,66,124,124) #bleu
    if choix  == 3 :
        couleur = 'jaune' #(250,160,0,150) #jaune
    return couleur
    
def niveau1():
    
    pygame.init()
    pygame.key.set_repeat(400,30)
  
    pygame.mixer.init()
    pygame.mixer.music.load("sounds/son_music/son_music.mp3")
    pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.play(-1) #-1 pour jouer en boucle

    clock = pygame.time.Clock() #pour gener le frame rate
    fenetre = pygame.display.set_mode((1000, 1000))
    pygame.display.set_caption("Tetris")
    fond = pygame.Surface((1000, 1000), pygame.SRCALPHA)
    fond.fill((200,0,0,20))
    #fond_droit = pygame.image.load((os.path.join('image/fond', 'fond_droit_marron.png'))).convert()
    
    police_fond = pygame.font.Font(None, 39)
    police = pygame.font.Font(None, 36)
    score = 0
    texte_score_fond = police_fond.render(f"{score}", True, 'Black')
    texte_score = police.render(f"{score}", True, 'White')
    #fenetre.blit(texte_score, (1050, 100))  # Position en haut à gauche


    old_position_player = []
    position_player = []
    l_case = []
    l_pose_occupe = []
    pos_actuelle = []
    d_player = {}
    l_d_player = []
    grille = Grille.Grille()
    
    
    choix_player = random.randint(0, 6)
    choix_player_precedent = choix_player
    nb_ligne = grille.getNbLigne()
    nb_colonne = grille.getNbColonne()
    
    #on remplit une partie des blocs
    ligne = int(nb_ligne - 1)
    while ligne > 12: #nb_ligne/2:
        colonne_vide = random.randint(0, 19)
        for colonne in range(nb_colonne):
            if ligne == nb_ligne - 1: 
                if random.randint(0, int(ligne)) != 1 and colonne != colonne_vide:
                    grille.setCaseOccupe(ligne, colonne, 1)
                    grille.changeCaseValue(ligne, colonne, 1 )
                    grille.majColor(ligne, colonne, choixCouleur())
            else:
                if grille.getCaseOccupe(ligne + 1, colonne) == 1:
                    if random.randint(0, 8) != 1:
                        grille.setCaseOccupe(ligne, colonne, 1)
                        grille.changeCaseValue(ligne, colonne, 1 )
                        grille.majColor(ligne, colonne, choixCouleur())
        ligne -= 1
            
    vitesse_player = 1
    if choix_player == 0:
        player = Player.Cube(nb_ligne, nb_colonne, vitesse_player)
    if choix_player == 1:
        player = Player.Barre(nb_ligne, nb_colonne, vitesse_player)
    if choix_player == 2:
        player = Player.L(nb_ligne, nb_colonne, vitesse_player)
    if choix_player == 3:
        player = Player.T(nb_ligne, nb_colonne, vitesse_player)
    if choix_player == 4:
        player = Player.L_inv(nb_ligne, nb_colonne, vitesse_player)
    if choix_player == 5:
        player = Player.Z(nb_ligne, nb_colonne, vitesse_player)
    if choix_player == 6:
        player = Player.Z_inv(nb_ligne, nb_colonne, vitesse_player)
      
    position_player = player.getPosActuelle()
    
    for brique in position_player:
        f_ligne = int(brique.getLigne())
        f_colonne = int(brique.getColonne())        
        grille.changeCaseValue(f_ligne, f_colonne, 1 )
        grille.majColor(f_ligne, f_colonne, player.getColor())

    #fenetre.blit(fond_droit,(1000,0))
   
    for ligne in grille.l_cases:
        for case in ligne:
            
            fenetre.blits([(case.image,case.rect), (case.contour,case.rect), (case.degrade, case.rect), (case.degrade_lumiere, case.rect)])
            #fenetre.blits([(case.image,case.rect), (case.contour,case.rect), (case.degrade, case.rect)])
            
    fenetre.blit(texte_score_fond,(925, 20))    
    fenetre.blit(texte_score,(925, 20))                 
    
    temps_bloque = 0
    intervalle_decalage = 100
    intervalle_temps = 1000
    intervalle_bloque = 100
    action_bloque = pygame.time.get_ticks() + 100
    prochaine_descente = pygame.time.get_ticks()
    decalage_possible = pygame.time.get_ticks()
    continuer = True
    while continuer :
         maj_ecran = False
         save_player = False
         
                 
         if player.actif:
            pass
         else:
            if grille.verifPartiePerdu():
                continuer = False      
            old_position_player = []
            maj_ecran = True
            
            if score >= 500:
                 vitesse_player = 2
            if score >= 1000:
                 vitesse_player = 3
            if score >= 1500:
                 fond.fill((200,0,0,30)) 
                 vitesse_player = 4
            if score >= 2500:
                 fond.fill((200,0,0,45)) 
                 vitesse_player = 5

            choix_player = tirage(0, 6, choix_player_precedent)
            choix_player_precedent = choix_player 
            if choix_player == 0:
                player = Player.Cube(nb_ligne, nb_colonne, vitesse_player)
            if choix_player == 1:
                player = Player.Barre(nb_ligne, nb_colonne, vitesse_player)
            if choix_player == 2:
                player = Player.L(nb_ligne, nb_colonne, vitesse_player)
            if choix_player == 3:
                player = Player.T(nb_ligne, nb_colonne, vitesse_player)
            if choix_player == 4:
                player = Player.L_inv(nb_ligne, nb_colonne, vitesse_player)
            if choix_player == 5:
                player = Player.Z(nb_ligne, nb_colonne, vitesse_player)
            if choix_player == 6:
                player = Player.Z_inv(nb_ligne, nb_colonne, vitesse_player)
            position_player = player.getPosActuelle() 
            
         
         for event in pygame.event.get():
            if event.type == QUIT:
                continuer = False
         
               
            if event.type == KEYDOWN:
                maj_ecran = True
                dicKeys = pygame.key.get_pressed() 
                if dicKeys[K_LEFT] :
                    translation_possible = True
                    for brique in player.getPosActuelle(): 
                        colonne = int(brique.getColonne())
                        ligne = int(brique.getLigne()) 
                        if colonne == 0:
                            translation_possible = False
                            break
                        if grille.getCaseOccupe(ligne, colonne - 1) == 1:
                            translation_possible = False
                            break
                    if translation_possible:
                        player.translation(-1)
                         
                if dicKeys[K_RIGHT] :    
                    translation_possible = True
                    for brique in player.getPosActuelle(): 
                        colonne = int(brique.getColonne())
                        ligne = int(brique.getLigne()) 
                        
                        if colonne == grille.getNbColonne() - 1:
                            translation_possible = False
                            break
                        if grille.getCaseOccupe(ligne, colonne + 1) == 1:
                            translation_possible = False
                            break
                    if translation_possible:
                        player.translation(1)
                    
                if dicKeys[K_DOWN] : 
                    if player.l_brique[0].ligne > 2:
                        player.acceleration()
        
            if event.type == MOUSEBUTTONDOWN: 
                if pygame.time.get_ticks() - action_bloque >= intervalle_bloque:
                    action_bloque = pygame.time.get_ticks()
                    rotation_ok = 1
                    l_futur_pos = player.controleRotationGauche()
                    for brique in l_futur_pos:
                        futur_colonne = int(brique.getColonne())
                        futur_ligne = int(brique.getLigne())                      
                        if grille.getCaseOccupe(futur_ligne, futur_colonne) == 1:
                            rotation_ok = 0
                            break   
                        if futur_colonne < 0:
                            rotation_ok = 0
                            break  
                        if futur_colonne > 19:
                            rotation_ok = 0
                            break 
                        
                    if rotation_ok == 0 and player.type == 2:   #barre
                        rotation_ok = 2
                        l_futur_pos = player.controleRotationDroite()
                        for brique in l_futur_pos:
                            futur_colonne = int(brique.getColonne())
                            futur_ligne = int(brique.getLigne())
                            if grille.getCaseOccupe(futur_ligne, futur_colonne) == 1:
                                rotation_ok = 0    
                                break   
                            if futur_colonne < 0:
                                rotation_ok = 0
                                break   
                            if futur_colonne > 19:
                                rotation_ok = 0
                                break   
                    if rotation_ok  == 1:
                        player.rotationGauche(l_futur_pos)
                        maj_ecran = True
                    if rotation_ok  == 2:
                        player.rotationDroite(l_futur_pos)  
                        maj_ecran = True
                
         
         if pygame.time.get_ticks() - prochaine_descente >= (intervalle_temps/player.vitesse):
            prochaine_descente = pygame.time.get_ticks()
            player.descente()
            maj_ecran = True
         
         if maj_ecran:
             #enleve la couleur sur l'ancienne position du joueur si il en avait une
             old_position_player =  copy.deepcopy(position_player )
             for brique in old_position_player:    
                f_ligne = int(brique.getLigne())
                f_colonne = int(brique.getColonne())
                grille.changeCaseValue(f_ligne, f_colonne, 0 ) 
                grille.majColor(f_ligne, f_colonne, (120,135,150,0) )
               
             position_player = player.getPosActuelle()
             for brique in position_player:
                 f_ligne = int(brique.getLigne())
                 f_colonne = int(brique.getColonne())
                 grille.changeCaseValue(f_ligne, f_colonne, 1 )
                 grille.majColor(f_ligne, f_colonne, player.getColor())
               
             pose_actuelle = player.getPosActuelle()
             for brique in pose_actuelle: 
                 ligne = int(brique.getLigne())
                 colonne = int(brique.getColonne())
                 if ligne == 19:
                     player.desactive()
                     save_player = True
                     break
                 if grille.getCaseOccupe(ligne+1, colonne) == 1:
                     player.desactive()
                     save_player = True
                     break
             #print(player.actif)
             if not player.actif:                 
                 decalage_possible = pygame.time.get_ticks()
             
             if save_player:
                #nb_decalage = 0
                #while pygame.time.get_ticks() - decalage_possible <= intervalle_decalage:
                #  if nb_decalage == 0:    
                #      for event in pygame.event.get():  
                #          if event.type == KEYDOWN:
                #              dicKeys = pygame.key.get_pressed() 
                #              if dicKeys[K_LEFT] :
                #                  translation_possible = True
                #                  for brique in player.getPosActuelle(): 
                #                      colonne = int(brique.getColonne())
                #                      ligne = int(brique.getLigne()) 
                #                      if colonne == 0:
                #                          translation_possible = False
                #                          break
                #                      if grille.getCaseOccupe(ligne, colonne - 1) == 1:
                #                          translation_possible = False
                #                          break
                #                  if translation_possible:
                #                      player.translation(-1)
                #                      nb_decalage += 1
                #       
                #              if dicKeys[K_RIGHT] :    
                #                  translation_possible = True
                #                  for brique in player.getPosActuelle(): 
                #                      colonne = int(brique.getColonne())
                #                      ligne = int(brique.getLigne()) 
                #      
                #                      if colonne == grille.getNbColonne() - 1:
                #                          translation_possible = False
                #                          break
                #                      if grille.getCaseOccupe(ligne, colonne + 1) == 1:
                #                          translation_possible = False
                #                          break
                #                  if translation_possible:
                #                      player.translation(1)
                #                      nb_decalage += 1
                #  if nb_decalage == 1:
                #      old_position_player =  copy.deepcopy(position_player )
                #      for brique in old_position_player:    
                #         f_ligne = int(brique.getLigne())
                #         f_colonne = int(brique.getColonne())
                #         grille.changeCaseValue(f_ligne, f_colonne, 0 ) 
                #         grille.majColor(f_ligne, f_colonne, (120,135,150,0) )
                #
                #      position_player = player.getPosActuelle()
                #      for brique in position_player:
                #          f_ligne = int(brique.getLigne())
                #          f_colonne = int(brique.getColonne())
                #          grille.changeCaseValue(f_ligne, f_colonne, 1 )
                #          grille.majColor(f_ligne, f_colonne, player.getColor())


                 for brique in position_player: 
                     ligne = int(brique.getLigne())
                     colonne = int(brique.getColonne())
                     grille.setCaseOccupe(ligne,colonne, 1)
                 
                 ligne_complete = False
                 ligne_a_supprimer = []
                 ligne_complete, ligne_a_supprimer  = grille.getLigneComplete()
                 if ligne_complete:
                     for y in ligne_a_supprimer:
                        grille.suppLigneComplete(y)
                        score += 100
                        texte_score_fond = police_fond.render(f"{score}", True, 'Black')
                        texte_score = police.render(f"{score}", True, 'White')
                        fenetre.blit(fond,(0,0))
                        
                                 
             for ligne in grille.l_cases:
                 for case in ligne:
                     fenetre.blits([(case.image,case.rect), (case.contour,case.rect), (case.degrade, case.rect), (case.degrade_lumiere, case.rect)])
             if score >= 1000:
                 fenetre.blit(texte_score_fond,(923,21))    
                 fenetre.blit(fond,(0,0))
             else: 
                 fenetre.blit(texte_score_fond,(924,21))
             
             fenetre.blit(texte_score,(925, 20))    
             
         clock.tick(60) #limite a 60 fps
         pygame.display.update()
        
    menuJeu()





menuJeu()
pygame.quit()