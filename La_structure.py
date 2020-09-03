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

def mapping():

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

def deplacement():

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

def recollage ():

    global position_pixel_mur
    global position_pixel_libre
    global position_pixel_depart
    global position_pixel_perso
    global position_pixel_mur
    global position_pixel_gardien
    global position_pixel_tube
    global position_pixel_ether
    global position_pixel_aiguille
    global position_pixel_gagnez
    global position_pixel_mort

    global position_V_map
    global position_H_map
    global longueur_case
    global hauteur_case

    global image_mur
    global image_libre
    global image_depart
    global image_perso
    global image_mur
    global image_gardien
    global image_tube
    global image_ether
    global image_aiguille
    global image_gagnez
    global image_mort


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
    if gagnez_jeu == True:
        fenetre.blit(image_gagnez, position_pixel_gagnez)
    if perdu_jeu == True:
        fenetre.blit(image_mort, position_pixel_mort)


"""
Le programme principale
"""

boucle_principale = 1

# Boucle principale
while boucle_principale:

    # Chargement et affichage de l'écran d'accueil
    image_accueil = pygame.image.load("accueil.jpg").convert_alpha()
    position_pixel_accueil = (0, 0)
    image_accueil = pygame.transform.scale(image_accueil, (longueur_fenetre, hauteur_fenetre))
    fenetre.blit(image_accueil, position_pixel_accueil)

    # Rafraichissement
    pygame.display.flip()

    # Renitilisation des variables pour quand le jeu ce lance et le recommencement
    trouver_tube = False
    trouver_ether = False
    trouver_aiguille = False
    gagnez_jeu = False
    perdu_jeu = False
    sortir_du_jeu = False

    continuer_accueil = 1
    continuer_jeu = 1

    # Boucle d'accueil
    while continuer_accueil:

        #Limitation de vitesse de la boucle
        pygame.time.Clock().tick(30)
        for event in pygame.event.get():

            if event.type == QUIT:
                continuer_accueil = 0
                continuer_jeu = 0
                boucle_principale = 0

            elif event.type == KEYDOWN:
                if event.key == K_F1:
                    continuer_accueil = 0

    mapping()

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
        print(nombre_aleatoire_ether_H, nombre_aleatoire_ether_V)
        print(nb_hasard_ether)

        # Une le nombre obtenu on colle l'image
        position_pixel_ether = (longueur_case * nombre_aleatoire_ether_H, hauteur_case * nombre_aleatoire_ether_V)
        fenetre.blit(image_ether, position_pixel_ether)

    # On dit que la position est egale au charactere donne
    map1[nombre_aleatoire_ether_V][nombre_aleatoire_ether_H] = position_ether
    print(position_ether)

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
        print(nombre_aleatoire_aiguille_H, nombre_aleatoire_aiguille_V)
        print(nb_hasard_aiguille)

        # Une le nombre obtenu on colle l'image
        position_pixel_aiguille = (longueur_case * nombre_aleatoire_aiguille_H, hauteur_case * nombre_aleatoire_aiguille_V)
        fenetre.blit(image_aiguille, position_pixel_aiguille)

    # On dit que la position est egale au charactere donne
    map1[nombre_aleatoire_aiguille_V][nombre_aleatoire_aiguille_H] = position_aiguille
    print(position_aiguille)

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
        print(nombre_aleatoire_tube_H, nombre_aleatoire_tube_V)
        print(nb_hasard_tube)

        # Une le nombre obtenu on colle l'image
        position_pixel_tube = (longueur_case * nombre_aleatoire_tube_H, hauteur_case * nombre_aleatoire_tube_V)
        fenetre.blit(image_tube, position_pixel_tube)

    # On dit que la position est egale au charactere donne
    map1[nombre_aleatoire_tube_V][nombre_aleatoire_tube_H] = position_tube
    print(position_tube)

    # Chargement et collage du personnage
    image_perso = pygame.image.load("macgyver.png").convert_alpha()
    image_perso = pygame.transform.scale(image_perso, (longueur_case, hauteur_case))
    position_pixel_perso = image_perso.get_rect()
    fenetre.blit(image_perso, position_pixel_perso)

    # (ré)initialisation des positions du perso
    position_perso_map_V = 0
    position_perso_map_V = 0
    image_perso.get_rect() == map1[0][0]

    # Boucle infinie
    while continuer_jeu:
        boucle_principale = 0
        for event in pygame.event.get(): # Attente des événements
            if event.type == QUIT:
                continuer_jeu = 0
                boucle_principale = 0
            elif event.type == KEYDOWN:
                deplacement()

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
                        position_pixel_gagnez = (0, 0)
                        image_gagnez = pygame.transform.scale(image_gagnez, (longueur_fenetre, hauteur_fenetre))
                        fenetre.blit(image_gagnez, position_pixel_gagnez)

                        # F1 pour recommencer
                        if event.key == K_F1:
                            sorir_du_jeu = True
                            continuer_accueil = 0
                            continuer_jeu = 0
                            boucle_principale = 1

                        # F2 pour quitter
                        elif event.key == K_F2:
                            sorir_du_jeu = True
                            continuer_jeu = 0
                            boucle_principale = 0

                    #Si il n'a pas trouver tous les objets il meurt
                    elif trouver_ether == False or trouver_aiguille == False or trouver_tube == False:
                        perdu_jeu = True
                        print("Vous etes mort")
                        position_pixel_mort = (0, 0)
                        image_mort = pygame.transform.scale(image_mort, (longueur_fenetre, hauteur_fenetre))
                        fenetre.blit(image_mort, position_pixel_mort)

                        #F1 pour recommencer
                        if event.key == K_F1:
                            sorir_du_jeu = True
                            continuer_accueil = 0
                            continuer_jeu = 0
                            boucle_principale = 1

                        #F2 pour quitter
                        elif event.key == K_F2:
                            sorir_du_jeu = True
                            continuer_jeu = 0
                            boucle_principale = 0


        recollage()

        # Rafraichissement
        pygame.display.flip()
