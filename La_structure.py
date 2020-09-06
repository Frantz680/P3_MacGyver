"""
Jeu Aidez MacGyver à s'échapper !
Jeu dans lequel on doit déplacer MacGyver à s'échapper du labyrinthe.
"""

import pygame
from random import *
from pygame.locals import *

from init_pygame import *
from constantes import *

"""
 Les differentes fonctions
"""
def ouvrir_fichier():

    global map1

    # On ouvre le ficher texte
    fichier_texte = open("Laby.txt", "r")  # r = on lit le texte
    print(fichier_texte)

    map1 = []
    ligne_map = []
    compteur = 0
    for lignes in fichier_texte:
        ligne_map = []
        # On lit chaque charactere du fichier
        for charactere in lignes:
            if charactere != "\n":
                ligne_map.append(charactere)
                # print(ligne_map)
        map1.append(ligne_map)
        # print("map1",compteur)
        # print(map1)
        compteur = compteur + 1

def mapping():

    global map1
    global position_pixel_depart
    global position_pixel_mur
    global position_pixel_gardien
    global position_pixel_libre

    # On parcours toute les lignes du tableau pour voir les caracteres
    for position_V_map in range(0, 15):
        for position_H_map in range(0, 15):

            # à chaque caractere qui correspond on colle une image
            if map1[position_H_map][position_V_map] == 'W':
                position_pixel_mur = (longueur_case * position_V_map, hauteur_case * position_H_map)
                fenetre.blit(image_mur, position_pixel_mur)

            elif map1[position_H_map][position_V_map] == 'G':
                position_pixel_gardien = (longueur_case * position_V_map, hauteur_case * position_H_map)
                fenetre.blit(image_gardien, position_pixel_gardien)

            elif map1[position_H_map][position_V_map] == 'S':
                position_pixel_depart = (longueur_case * position_V_map, hauteur_case * position_H_map)
                fenetre.blit(image_depart, position_pixel_depart)

            else:
                position_pixel_libre = (longueur_case * position_V_map, hauteur_case * position_H_map)
                fenetre.blit(image_libre, position_pixel_libre)

def hasard():

    global image_ether
    global position_pixel_ether
    global image_aiguille
    global position_pixel_aiguille
    global image_tube
    global position_pixel_tube

    # choisir un nombre aleatoire dans la map pour l'ether

    position_ether = 'E'
    nb_hasard_ether = 0
    nombre_aleatoire_ether_H = randint(0, 14)
    nombre_aleatoire_ether_V = randint(0, 14)

    # Tant que le nombre hasard est different des cases libres
    while nb_hasard_ether != 'F':
        nombre_aleatoire_ether_H = randint(0, 14)
        nombre_aleatoire_ether_V = randint(0, 14)
        nb_hasard_ether = map1[nombre_aleatoire_ether_V][nombre_aleatoire_ether_H]
        #print(nombre_aleatoire_ether_H, nombre_aleatoire_ether_V)
        #print(nb_hasard_ether)

        # Une le nombre obtenu on colle l'image
        position_pixel_ether = (longueur_case * nombre_aleatoire_ether_H, hauteur_case * nombre_aleatoire_ether_V)
        fenetre.blit(image_ether, position_pixel_ether)

    # On dit que la position est egale au charactere donne
    map1[nombre_aleatoire_ether_V][nombre_aleatoire_ether_H] = position_ether
    #print(position_ether)

    # choisir un nombre aleatoire dans la map pour l'aiguille

    position_aiguille = 'A'
    nb_hasard_aiguille = 0
    nombre_aleatoire_aiguille_H = randint(0, 14)
    nombre_aleatoire_aiguille_V = randint(0, 14)

    # Tant que le nombre hasard est different des cases libres
    while nb_hasard_aiguille != 'F' and nb_hasard_aiguille != 'A':
        nombre_aleatoire_aiguille_H = randint(0, 14)
        nombre_aleatoire_aiguille_V = randint(0, 14)
        nb_hasard_aiguille = map1[nombre_aleatoire_aiguille_V][nombre_aleatoire_aiguille_H]
        #print(nombre_aleatoire_aiguille_H, nombre_aleatoire_aiguille_V)
        #print(nb_hasard_aiguille)

        # Une le nombre obtenu on colle l'image
        position_pixel_aiguille = (longueur_case * nombre_aleatoire_aiguille_H, hauteur_case * nombre_aleatoire_aiguille_V)
        fenetre.blit(image_aiguille, position_pixel_aiguille)

    # On dit que la position est egale au charactere donne
    map1[nombre_aleatoire_aiguille_V][nombre_aleatoire_aiguille_H] = position_aiguille
    #print(position_aiguille)

    # choisir un nombre aleatoire dans la map pour le tube
    position_tube = 'T'
    nb_hasard_tube = 0
    nombre_aleatoire_tube_H = randint(0, 14)
    nombre_aleatoire_tube_V = randint(0, 14)

    # Tant que le nombre hasard ets different des cases libres
    while nb_hasard_tube != 'F' and nb_hasard_tube != 'A' and nb_hasard_tube != 'T':
        nombre_aleatoire_tube_H = randint(0, 14)
        nombre_aleatoire_tube_V = randint(0, 14)
        nb_hasard_tube = map1[nombre_aleatoire_tube_V][nombre_aleatoire_tube_H]
        #print(nombre_aleatoire_tube_H, nombre_aleatoire_tube_V)
        #print(nb_hasard_tube)

        # Une le nombre obtenu on colle l'image
        position_pixel_tube = (longueur_case * nombre_aleatoire_tube_H, hauteur_case * nombre_aleatoire_tube_V)
        fenetre.blit(image_tube, position_pixel_tube)

    # On dit que la position est egale au charactere donne
    map1[nombre_aleatoire_tube_V][nombre_aleatoire_tube_H] = position_tube
    #print(position_tube)

def deplacement():

    global map1
    global position_perso_map_V
    global position_perso_map_H
    global position_pixel_perso

    if event.key == K_DOWN:  # Si "flèche bas"
        if position_perso_map_V != 14:
            if map1[position_perso_map_V + 1][position_perso_map_H] != 'W':

                # On descend le perso GRAPHIQUEMENT
                position_pixel_perso = position_pixel_perso.move(0, hauteur_case)

                # On descend le perso PHYSIQUEMENT
                position_perso_map_V = position_perso_map_V + 1

                print("position dans map a l'horizontal : " + str(position_perso_map_H))
                print("position dans map a l'horizontal : " + str(position_perso_map_V))
                print(map1[position_perso_map_V][position_perso_map_H])

            else:
                print("mur deplacement vers le bas impossible")
                print("position dans map a l'horizontal : " + str(position_perso_map_H))
                print("position dans map a la vertical : " + str(position_perso_map_V))


    elif event.key == K_UP:  # Si "flèche haut
        if position_perso_map_V != 0:
            if map1[position_perso_map_V - 1][position_perso_map_H] != 'W':

                # On monte le perso GRAPHIQUEMENT
                position_pixel_perso = position_pixel_perso.move(0, -hauteur_case)

                # On monte le perso PHYSIQUEMENT
                position_perso_map_V = position_perso_map_V - 1

                print("position dans map a l'horizontal : " + str(position_perso_map_H))
                print("position dans map a la vertical : " + str(position_perso_map_V))
                print(map1[position_perso_map_V][position_perso_map_H])

            else:
                print("mur deplacement vers le haut impossible")
                print("position dans map a l'horizontal : " + str(position_perso_map_H))
                print("position dans map a la vertical : " + str(position_perso_map_V))



    elif event.key == K_LEFT:  # Si "flèche gauche"
        if position_perso_map_H != 0:
            if map1[position_perso_map_V][position_perso_map_H - 1] != 'W':

                # Le perso va à gauche GRAPHIQUEMENT
                position_pixel_perso = position_pixel_perso.move(-longueur_case, 0)

                # Le perso va à gauche PHYSIQUEMENT
                position_perso_map_H = position_perso_map_H - 1

                print("position dans map a l'horizontal : " + str(position_perso_map_H))
                print("position dans map a la vertical : " + str(position_perso_map_V))
                print(map1[position_perso_map_V][position_perso_map_H])

            else:
                print("mur deplacement vers la gauche impossible")
                print("position dans map a l'horizontal : " + str(position_perso_map_H))
                print("position dans map a la vertical : " + str(position_perso_map_V))



    elif event.key == K_RIGHT:  # Si "flèche droite"
        if position_perso_map_H != 14:
            if map1[position_perso_map_V][position_perso_map_H + 1] != 'W':
                # Le perso va à droite GRAPHIQUEMENT
                position_pixel_perso = position_pixel_perso.move(longueur_case, 0)

                # Le perso va à droite PHYSIQUEMENT
                position_perso_map_H = position_perso_map_H + 1

                print("position dans map a l'horizontal : " + str(position_perso_map_H))
                print("position dans map a la vertical : " + str(position_perso_map_V))
                print(map1[position_perso_map_V][position_perso_map_H])

            else:
                print("mur deplacement vers la droite impossible")
                print("position dans map a l'horizontal : " + str(position_perso_map_H))
                print("position dans map a la vertical : " + str(position_perso_map_V))

def gestion_objets_trouve ():

    global map1
    global trouver_ether
    global trouver_tube
    global trouver_aiguille
    global gagnez_jeu
    global perdu_jeu

    # Si la perso va sur l'objet, le valeur devient vrai
    if map1[position_perso_map_V][position_perso_map_H] == 'E':
        print("Vous avez trouvez l'ether")
        trouver_ether = True

    elif map1[position_perso_map_V][position_perso_map_H] == 'T':
        print("Vous avez trouvez le tube")
        trouver_tube = True

    elif map1[position_perso_map_V][position_perso_map_H] == 'A':
        print("Vous avez trouvez l'aiguille")
        trouver_aiguille = True

    # Si le perso est sur le gardien
    elif map1[position_perso_map_V][position_perso_map_H] == 'G':

        #Si il a trouver tous les objets il gagne
        if trouver_ether == True and trouver_aiguille == True and trouver_tube == True:
            gagnez_jeu = True
            print("Vous avez gagnez")

        #Si il n'a pas trouver tous les objets il meurt
        elif trouver_ether == False or trouver_aiguille == False or trouver_tube == False:
            perdu_jeu = True
            print("Vous etes mort")

def recollage ():

    global map1

    for position_V_map in range(0, 15):
        for position_H_map in range(0, 15):
            if map1[position_H_map][position_V_map] == 'W':
                position_pixel_mur = (longueur_case * position_V_map, hauteur_case * position_H_map)
                fenetre.blit(image_mur, position_pixel_mur)
            else:
                position_pixel_libre = (longueur_case * position_V_map, hauteur_case * position_H_map)
                fenetre.blit(image_libre, position_pixel_libre)
    fenetre.blit(image_depart, position_pixel_depart)
    fenetre.blit(image_perso, position_pixel_perso)
    fenetre.blit(image_mur, position_pixel_mur)
    fenetre.blit(image_gardien, position_pixel_gardien)
    if trouver_tube == False:
        fenetre.blit(image_tube, position_pixel_tube)
    if trouver_ether == False:
        fenetre.blit(image_ether, position_pixel_ether)
    if trouver_aiguille == False:
        fenetre.blit(image_aiguille, position_pixel_aiguille)
    
    # Rafraichissement
    pygame.display.flip()
 

"""
Le programme principale
"""
ouvrir_fichier()
boucle_principale = 1

# Boucle principale
while boucle_principale:

    boucle_accueil = 1
    boucle_recommencer = 1

    # Boucle d'accueil
    while boucle_accueil:

        # Chargement et affichage de l'écran d'accueil
        position_pixel_accueil = (0, 0)
        fenetre.blit(image_accueil, position_pixel_accueil)

        # Rafraichissement
        pygame.display.flip()


        for event in pygame.event.get():

            if event.type == QUIT:
                boucle_accueil = 0
                boucle_jeu = 0
                boucle_principale = 0
                boucle_recommencer = 0

            elif event.type == KEYDOWN:
                if event.key == K_F1:
                    boucle_accueil = 0
                    boucle_recommencer = 1
                    print("acceuil F1")

    while boucle_recommencer:

        print("boucle_recommencer")
        # Renitilisation des variables pour quand le jeu ce lance et le recommencement
        trouver_tube = False
        trouver_ether = False
        trouver_aiguille = False
        gagnez_jeu = False
        perdu_jeu = False
        boucle_jeu = 1

        mapping()
        hasard()

        # Chargement et collage du personnage
        position_pixel_perso = image_perso.get_rect()
        fenetre.blit(image_perso, position_pixel_perso)

        # (ré)initialisation des positions du perso
        position_perso_map_V = 0
        position_perso_map_V = 0
        image_perso.get_rect() == map1[0][0]

        # Boucle infinie
        while boucle_jeu:
            for event in pygame.event.get(): # Attente des événements
                if event.type == QUIT:
                    boucle_jeu = 0
                    boucle_principale = 0
                    boucle_recommencer = 0
                elif event.type == KEYDOWN:
                    deplacement()
                    gestion_objets_trouve()
            recollage()

            while perdu_jeu == True or gagnez_jeu == True :
                
                if gagnez_jeu == True:
                    fenetre.blit(image_gagnez, position_pixel_gagnez)
                    pygame.display.flip()

                elif perdu_jeu == True:
                    fenetre.blit(image_mort, position_pixel_mort)
                    pygame.display.flip()
                    
                for event in pygame.event.get(): # Attente des événements
                    if event.type == QUIT:
                        boucle_jeu = 0
                        boucle_principale = 0
                        boucle_recommencer = 0
                        perdu_jeu = False
                        gagnez_jeu = False

                    elif event.type == KEYDOWN:
                        # F1 pour recommencer
                        if event.key == K_F1:
                            boucle_jeu = 0
                            boucle_recommencer = 1
                            perdu_jeu = False
                            gagnez_jeu = False
                            print("recommencer F1")
                            ouvrir_fichier()

                        # F2 pour quitter
                        elif event.key == K_F2:
                            boucle_jeu = 0
                            boucle_principale = 0
                            boucle_recommencer = 0
                            perdu_jeu = False
                            gagnez_jeu = False
                            print("quitter F2")
                

