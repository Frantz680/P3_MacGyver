"""
Initialization of the pygame library
"""

import pygame
from pygame.locals import *

from constants import *

pygame.init()

# Opening the pygame and Title window
window = pygame.display.set_mode((WINDOW_L, WINDOW_H), RESIZABLE)

# Title
pygame.display.set_caption("Aidez MacGyver à s'échapper")

# Screen refresh
pygame.display.flip()
pygame.key.set_repeat(400, 30)
