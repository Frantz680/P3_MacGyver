"""
Initialization of the pygame library
"""

import pygame
from pygame.locals import *

from constantes import *

pygame.init()

# Opening the Pygame and Title window
window = pygame.display.set_mode((WINDOW_L, WINDOW_H), RESIZABLE)

# Title
pygame.display.set_caption("Aidez MacGyver à s'échapper")

# Loading pictures
wall_picture = pygame.image.load("Mur.png").convert_alpha()
free_picture = pygame.image.load("libre.png").convert_alpha()
starting_picture = pygame.image.load("arriver.png").convert_alpha()
guardian_picture = pygame.image.load("gardien.png").convert_alpha()
needle_picture = pygame.image.load("aiguille.png").convert_alpha()
ether_picture = pygame.image.load("ether.png").convert_alpha()
syringe_picture = pygame.image.load("seringue.png").convert_alpha()
picture_win = pygame.image.load("gagnez.jpg").convert_alpha()
dead_picture = pygame.image.load("mort.png").convert_alpha()
hero_picture = pygame.image.load("macgyver.png").convert_alpha()
picture_home = pygame.image.load("accueil.jpg").convert_alpha()

# Creation of pictures dimensions
wall_picture = pygame.transform.scale(wall_picture, (CASE_L, CASE_H))
guardian_picture = pygame.transform.scale(guardian_picture, (CASE_L, CASE_H))
starting_picture = pygame.transform.scale(starting_picture, (CASE_L, CASE_H))
free_picture = pygame.transform.scale(free_picture, (CASE_L, CASE_H))
ether_picture = pygame.transform.scale(ether_picture, (CASE_L, CASE_H))
needle_picture = pygame.transform.scale(needle_picture, (CASE_L, CASE_H))
syringe_picture = pygame.transform.scale(syringe_picture, (CASE_L, CASE_H))
hero_picture = pygame.transform.scale(hero_picture, (CASE_L, CASE_H))
picture_home = pygame.transform.scale(picture_home, (WINDOW_L, WINDOW_H))
picture_win = pygame.transform.scale(picture_win, (WINDOW_L, WINDOW_H))
dead_picture = pygame.transform.scale(dead_picture, (WINDOW_L, WINDOW_H))

# Screen refresh
pygame.display.flip()
pygame.key.set_repeat(400, 30)