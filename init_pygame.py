import pygame
from pygame.locals import *
from constantes import *

pygame.init()

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

# Création de la dimentions des images
image_mur = pygame.transform.scale(image_mur, (longueur_case, hauteur_case))
image_gardien = pygame.transform.scale(image_gardien, (longueur_case, hauteur_case))
image_depart = pygame.transform.scale(image_depart, (longueur_case, hauteur_case))
image_libre = pygame.transform.scale(image_libre, (longueur_case, hauteur_case))
image_ether = pygame.transform.scale(image_ether, (longueur_case, hauteur_case))
image_aiguille = pygame.transform.scale(image_aiguille, (longueur_case, hauteur_case))
image_tube = pygame.transform.scale(image_tube, (longueur_case, hauteur_case))

# Rafraichissement de l'écran
pygame.display.flip()
pygame.key.set_repeat(400, 30)