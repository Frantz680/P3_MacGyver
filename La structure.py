"""
Jeu Aidez MacGyver à s'échapper !
Jeu dans lequel on doit déplacer MacGyver à s'échapper du labyrinthe.
"""

import pygame
from random import *
from pygame.locals import *

from Map import *
from constantes import *
#Labyrinthe



map =[[9, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
      [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1],
      [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
      [1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0],
      [1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
      [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
      [1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1],
      [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1],
      [0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0],
      [1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1],
      [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
      [1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
      [4, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0],
      [0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0],
      [2, 1, 1, 1, 1, 0, 0, 0, 3, 1, 0, 0, 0, 0, 0]]


# On ouvre le ficher texte
#fichier_texte = open("Laby.txt", "r")# r = on lit le texte
#print(fichier_texte)

# On lit chaque ligne du fichier
#for lignes in fichier_texte:

#    print("ligne")
#    print(lignes)

    # On lit chaque charactere du fichier
#    for charactere in lignes:
#        print("char")
#        print(charactere)
#        map=[]
#        map=[charactere for charactere in fichier_texte]
#        print("map")
#        print(map)

# Nombre de ligne
nb_ligne=15
nb_collogne=15

# Dimention fenetre
longueur_fenetre = 600
hauteur_fenetre = 600


# Dimention case
longueur_case = longueur_fenetre // nb_ligne
hauteur_case = hauteur_fenetre // nb_collogne

position_mur = (0,0)
position_pixel_mort = (0,0)

position_V=0
position_H=0

position_perso_map_V=0
position_perso_map_H=0


pygame.init()

trouver_ether = False
trouver_aiguille = False
gagnez_jeu = False

# Ouverture de la fenêtre Pygame et tire
fenetre = pygame.display.set_mode((longueur_fenetre, hauteur_fenetre),RESIZABLE)

# Titre
pygame.display.set_caption("Aidez MacGyver à s'échapper")

# Chargement des images
image_mur = pygame.image.load("Mur.png").convert_alpha()
image_libre = pygame.image.load("libre.png").convert_alpha()
image_depart = pygame.image.load("arriver.png").convert_alpha()
image_gardien = pygame.image.load("gardien.png").convert_alpha()
image_aiguille = pygame.image.load("aiguille.png").convert_alpha()
image_ether = pygame.image.load("macgyver_ressources/ressource/ether.png").convert_alpha()
image_tube = pygame.image.load("macgyver_ressources/ressource/tube_plastique.png").convert_alpha()
image_gagnez = pygame.image.load("gagnez.jpg").convert_alpha()
image_mort = pygame.image.load("mort.png").convert_alpha()

# Rafraichissement de l'écran
pygame.display.flip()
pygame.key.set_repeat(400, 30)

continuer = 1


# Boucle principale
while continuer:

    # Chargement et affichage de l'écran d'accueil
    image_accueil = pygame.image.load("accueil.jpg").convert_alpha()
    position_pixel_accueil = (0, 0)
    image_accueil = pygame.transform.scale(image_accueil, (longueur_fenetre, hauteur_fenetre))
    fenetre.blit(image_accueil, position_pixel_accueil)

    # Rafraichissement
    pygame.display.flip()

    trouver_ether = False
    trouver_aiguille = False
    gagnez_jeu = False
    perdu_jeu = False

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
                continuer = 0

            elif event.type == KEYDOWN:
                if event.key == K_F1:
                    continuer_accueil = 0


    for position_V_map in range (0,15):
        for position_H_map in range (0,15):


            if map[position_H_map][position_V_map] == 0:
                position_pixel_mur = (longueur_case * position_V_map,hauteur_case * position_H_map)
                image_mur = pygame.transform.scale(image_mur,(longueur_case,hauteur_case))
                fenetre.blit(image_mur, position_pixel_mur)

            elif map[position_H_map][position_V_map] == 2:
                position_pixel_gardien = (longueur_case * position_V_map,hauteur_case*position_H_map)
                image_gardien = pygame.transform.scale(image_gardien,(longueur_case,hauteur_case))
                fenetre.blit(image_gardien, position_pixel_gardien)

            elif map[position_H_map][position_V_map] == 9:
                position_pixel_depart = (longueur_case * position_V_map, hauteur_case * position_H_map)
                image_depart = pygame.transform.scale(image_depart, (longueur_case, hauteur_case))
                fenetre.blit(image_depart, position_pixel_depart)

            elif map[position_H_map][position_V_map] == 3:
                position_pixel_aiguille = (longueur_case * position_V_map,hauteur_case * position_H_map)
                image_aiguille = pygame.transform.scale(image_aiguille,(longueur_case,hauteur_case))
                fenetre.blit(image_aiguille, position_pixel_aiguille)

            elif map[position_H_map][position_V_map] == 4:
                position_pixel_ether = (longueur_case * position_V_map, hauteur_case * position_H_map)
                image_ether = pygame.transform.scale(image_ether, (longueur_case, hauteur_case))
                fenetre.blit(image_ether, position_pixel_ether)

            #elif map[position_H_map][position_V_map] == nb_hasard1:
                #position_pixel_tube = (longueur_case * position_V_map, hauteur_case * position_H_map)
                #image_tube = pygame.transform.scale(image_tube, (longueur_case, hauteur_case))
                #fenetre.blit(image_tube, position_pixel_tube)

            else:
                position_pixel_libre = (longueur_case * position_V_map,hauteur_case * position_H_map)
                image_libre = pygame.transform.scale(image_libre,(longueur_case,hauteur_case))
                fenetre.blit(image_libre, position_pixel_libre)

    # Chargement et collage du personnage
    image_perso = pygame.image.load("macgyver.png").convert_alpha()
    image_perso = pygame.transform.scale(image_perso, (longueur_case, hauteur_case))
    position_pixel_perso = image_perso.get_rect()
    fenetre.blit(image_perso, position_pixel_perso)

    #choisir un nombre aleatoire dans une liste de map
    nb_hasard = choice(map)
    print(nb_hasard)
    #choisir un nombre aleatoire dans la liste 
    nb_hasard1 = 0
    while nb_hasard1 != 1:
        nb_hasard1 = choice(nb_hasard)
        print(nb_hasard1)

        position_pixel_tube = (longueur_case * position_V_map, hauteur_case * position_H_map)
        image_tube = pygame.transform.scale(image_tube, (longueur_case, hauteur_case))
        fenetre.blit(image_tube, position_pixel_tube)

    position_perso_map_V = 0
    position_perso_map_V = 0
    image_perso.get_rect() == map[0][0]

    # Boucle infinie
    while continuer_jeu:
        continuer = 0
        for event in pygame.event.get(): # Attente des événements
            if event.type == QUIT:
                continuer_jeu = 0
                continuer = 0
            elif event.type == KEYDOWN:
                if event.key == K_DOWN:  # Si "flèche bas"
                    if position_perso_map_V != 14:
                        if map[position_perso_map_V+1][position_perso_map_H] != 0:

                            # On descend le perso GRAPHIQUEMENT
                            position_pixel_perso = position_pixel_perso.move(0, hauteur_case)

                            # On descend le perso PHYSIQUEMENT
                            position_perso_map_V = position_perso_map_V+1

                            print("position dans map a l'horizontal : " + str(position_perso_map_H))
                            print("position dans map a l'horizontal : " + str(position_perso_map_V))
                            print(map[position_perso_map_V][position_perso_map_H])

                        else:
                            print("mur deplacement vers le bas impossible")
                            print("position dans map a l'horizontal : " + str(position_perso_map_H))
                            print("position dans map a la vertical : " + str(position_perso_map_V))


                elif event.key == K_UP:  # Si "flèche haut
                    if position_perso_map_V != 0:
                        if map[position_perso_map_V-1][position_perso_map_H] != 0:

                            # On monte le perso GRAPHIQUEMENT
                            position_pixel_perso = position_pixel_perso.move(0, -hauteur_case)

                            # On monte le perso PHYSIQUEMENT
                            position_perso_map_V = position_perso_map_V-1

                            print("position dans map a l'horizontal : " + str(position_perso_map_H))
                            print("position dans map a la vertical : " + str(position_perso_map_V))
                            print(map[position_perso_map_V][position_perso_map_H])

                        else:
                            print("mur deplacement vers le haut impossible")
                            print("position dans map a l'horizontal : " + str(position_perso_map_H))
                            print("position dans map a la vertical : " + str(position_perso_map_V))



                elif event.key == K_LEFT: #Si "flèche gauche"
                    if position_perso_map_H != 0:
                        if map[position_perso_map_V][position_perso_map_H-1] != 0:

                            # Le perso va à gauche GRAPHIQUEMENT
                            position_pixel_perso = position_pixel_perso.move(-longueur_case,0)

                            # Le perso va à gauche PHYSIQUEMENT
                            position_perso_map_H = position_perso_map_H-1

                            print("position dans map a l'horizontal : " + str(position_perso_map_H))
                            print("position dans map a la vertical : " + str(position_perso_map_V))
                            print(map[position_perso_map_V][position_perso_map_H])

                        else:
                            print("mur deplacement vers la gauche impossible")
                            print("position dans map a l'horizontal : " + str(position_perso_map_H))
                            print("position dans map a la vertical : " + str(position_perso_map_V))



                elif event.key == K_RIGHT: # Si "flèche droite"
                    if position_perso_map_H != 14:
                        if map[position_perso_map_V][position_perso_map_H+1] != 0:
                            # Le perso va à droite GRAPHIQUEMENT
                            position_pixel_perso = position_pixel_perso.move(longueur_case,0)

                            # Le perso va à droite PHYSIQUEMENT
                            position_perso_map_H = position_perso_map_H+1

                            print("position dans map a l'horizontal : " + str(position_perso_map_H))
                            print("position dans map a la vertical : " + str(position_perso_map_V))
                            print(map[position_perso_map_V][position_perso_map_H])

                        else:
                            print("mur deplacement vers la droite impossible")
                            print("position dans map a l'horizontal : " + str(position_perso_map_H))
                            print("position dans map a la vertical : " + str(position_perso_map_V))

            elif map[position_perso_map_V][position_perso_map_H] == 4:
                print("Vous avez trouvez l'ether")
                trouver_ether = True


            elif map[position_perso_map_V][position_perso_map_H] == 3:
                print("Vous avez trouvez l'aiguille")
                trouver_aiguille = True

            elif map[position_perso_map_V][position_perso_map_H] == 2:
                if trouver_ether == True and trouver_aiguille == True:
                    print("Vous avez gagnez")
                    gagnez_jeu = True
                    position_pixel_gagnez = (0, 0)
                    image_gagnez = pygame.transform.scale(image_gagnez, (longueur_fenetre, hauteur_fenetre))
                    fenetre.blit(image_gagnez, position_pixel_gagnez)

                    if gagnez_jeu == True:
                        if event.key == K_F1:
                            continuer_accueil = 0
                            continuer_jeu = 0
                            continuer = 1

                        elif event.key == K_F2:
                            continuer_jeu = 0
                            continuer = 0

                elif trouver_ether == False or trouver_aiguille == False :
                    perdu_jeu = True
                    print("Vous etes mort")
                    position_pixel_mort = (0, 0)
                    image_mort = pygame.transform.scale(image_mort, (longueur_fenetre, hauteur_fenetre))
                    fenetre.blit(image_mort, position_pixel_mort)

                    if perdu_jeu == True:
                        if event.key == K_F1:
                            continuer_accueil = 0
                            continuer_jeu = 0
                            continuer = 1

                        elif event.key == K_F2:
                            continuer_jeu = 0
                            continuer = 0

        # Re-collage

        for position_V_map in range (0,15):
            for position_H_map in range (0,15): 
                if map[position_H_map][position_V_map] == 0:
                        position_pixel_mur = (longueur_case*position_V_map,hauteur_case*position_H_map)
                        image_mur = pygame.transform.scale(image_mur,(longueur_case,hauteur_case))
                        fenetre.blit(image_mur, position_pixel_mur)
                else:
                    position_pixel_libre = (longueur_case * position_V_map, hauteur_case * position_H_map)
                    image_libre = pygame.transform.scale(image_libre, (longueur_case, hauteur_case))
                    fenetre.blit(image_libre, position_pixel_libre)
        fenetre.blit(image_depart, position_pixel_depart)
        fenetre.blit(image_perso, position_pixel_perso)
        fenetre.blit(image_mur, position_pixel_mur)
        fenetre.blit(image_gardien, position_pixel_gardien)
        if perdu_jeu == True:
            fenetre.blit(image_mort, position_pixel_mort)
        if trouver_aiguille == False:
            fenetre.blit(image_aiguille, position_pixel_aiguille)
        if trouver_ether == False:
            fenetre.blit(image_ether, position_pixel_ether)
        fenetre.blit(image_tube, position_pixel_tube)
        if gagnez_jeu == True:
            fenetre.blit(image_gagnez, position_pixel_gagnez)





        # Rafraichissement
        pygame.display.flip()


