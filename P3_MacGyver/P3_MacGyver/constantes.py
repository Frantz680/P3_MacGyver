import pygame

#Labyrinthe

map =[[9, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
      [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1],
      [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
      [1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0],
      [1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
      [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
      [1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1],
      [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 15],
      [0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0],
      [1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1],
      [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
      [1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
      [4, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0],
      [0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0],
      [2, 1, 1, 1, 1, 0, 0, 0, 3, 1, 0, 0, 0, 0, 0]]


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

position_V=0
position_H=0

position_perso_map_V=0
position_perso_map_H=0
