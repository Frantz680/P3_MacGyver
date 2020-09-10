import pygame
from pygame.locals import *

from constantes import *

pygame.init()

# Opening the Pygame and Title window
window = pygame.display.set_mode((window_length, window_height), RESIZABLE)

# Title
pygame.display.set_caption("Aidez MacGyver à s'échapper")

# Loading pictures
wall_picture = pygame.image.load("Mur.png").convert_alpha()
free_picture = pygame.image.load("libre.png").convert_alpha()
starting_picture = pygame.image.load("arriver.png").convert_alpha()
guardian_picture = pygame.image.load("gardien.png").convert_alpha()
needle_picture = pygame.image.load("aiguille.png").convert_alpha()
ether_picture = pygame.image.load("macgyver_ressources/ressource/ether.png").convert_alpha()
syringe_picture = pygame.image.load("macgyver_ressources/ressource/seringue.png").convert_alpha()
picture_win = pygame.image.load("gagnez.jpg").convert_alpha()
dead_picture = pygame.image.load("mort.png").convert_alpha()
hero_picture = pygame.image.load("macgyver.png").convert_alpha()
picture_reception = pygame.image.load("accueil.jpg").convert_alpha()

# Creation of pictures dimensions
wall_picture = pygame.transform.scale(wall_picture, (case_length, case_height))
guardian_picture = pygame.transform.scale(guardian_picture, (case_length, case_height))
starting_picture = pygame.transform.scale(starting_picture, (case_length, case_height))
free_picture = pygame.transform.scale(free_picture, (case_length, case_height))
ether_picture = pygame.transform.scale(ether_picture, (case_length, case_height))
needle_picture = pygame.transform.scale(needle_picture, (case_length, case_height))
syringe_picture = pygame.transform.scale(syringe_picture, (case_length, case_height))
hero_picture = pygame.transform.scale(hero_picture, (case_length, case_height))
picture_reception = pygame.transform.scale(picture_reception, (window_length, window_height))
picture_win = pygame.transform.scale(picture_win, (window_length, window_height))
dead_picture = pygame.transform.scale(dead_picture, (window_length, window_height))

# Screen refresh
pygame.display.flip()
pygame.key.set_repeat(400, 30)

# Loop speed limitation
pygame.time.Clock().tick(30)