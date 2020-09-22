import pygame
from pygame.locals import *

from constantes import *

pygame.init()

# Opening the Pygame and Title window
window = pygame.display.set_mode((WINDOW_LENGTH, WINDOW_HEIGHT), RESIZABLE)

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
wall_picture = pygame.transform.scale(wall_picture, (CASE_LENGTH, CASE_HEIGHT))
guardian_picture = pygame.transform.scale(guardian_picture, (CASE_LENGTH, CASE_HEIGHT))
starting_picture = pygame.transform.scale(starting_picture, (CASE_LENGTH, CASE_HEIGHT))
free_picture = pygame.transform.scale(free_picture, (CASE_LENGTH, CASE_HEIGHT))
ether_picture = pygame.transform.scale(ether_picture, (CASE_LENGTH, CASE_HEIGHT))
needle_picture = pygame.transform.scale(needle_picture, (CASE_LENGTH, CASE_HEIGHT))
syringe_picture = pygame.transform.scale(syringe_picture, (CASE_LENGTH, CASE_HEIGHT))
hero_picture = pygame.transform.scale(hero_picture, (CASE_LENGTH, CASE_HEIGHT))
picture_reception = pygame.transform.scale(picture_reception, (WINDOW_LENGTH, WINDOW_HEIGHT))
picture_win = pygame.transform.scale(picture_win, (WINDOW_LENGTH, WINDOW_HEIGHT))
dead_picture = pygame.transform.scale(dead_picture, (WINDOW_LENGTH, WINDOW_HEIGHT))

# Screen refresh
pygame.display.flip()
pygame.key.set_repeat(400, 30)

# Loop speed limitation
pygame.time.Clock().tick(30)