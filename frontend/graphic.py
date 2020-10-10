"""
This class allows you to place images and objects randomly
"""

from random import randint

from backend.init_pygame import pygame, window
from backend.constants import CASE_L, CASE_H, \
    WINDOW_L, WINDOW_H, POSITION_PIXEL_RECEPTION, WALL, \
    GUARDIAN, STARTING, NEEDLE, SYRINGE, ETHER, FREE, \
    POSITION_PIXEL_WIN, POSITION_PIXEL_DEAD

"""
Import from random library

Import different variables
"""


class Graphic:
    """This class is used to display
    the images and to open the file.
    """

    def __init__(self):
        """We build the constructor."""

        self.pixel_n = 0
        self.pixel_ether = 0
        self.pixel_s = 0

        # Loading pictures
        self.wall_picture = \
            pygame.image.load("pictures/Mur.png").convert_alpha()
        self.free_picture = \
            pygame.image.load("pictures/libre.png").convert_alpha()
        self.starting_picture = \
            pygame.image.load("pictures/arriver.png").convert_alpha()
        self.guardian_picture = \
            pygame.image.load("pictures/gardien.png").convert_alpha()
        self.needle_picture = \
            pygame.image.load("pictures/aiguille.png").convert_alpha()
        self.ether_picture = \
            pygame.image.load("pictures/ETHER.png").convert_alpha()
        self.syringe_picture = \
            pygame.image.load("pictures/seringue.png").convert_alpha()
        self.hero_picture = \
            pygame.image.load("pictures/macgyver.png").convert_alpha()
        self.dead_picture = \
            pygame.image.load("pictures/mort.png").convert_alpha()
        self.picture_win = \
            pygame.image.load("pictures/gagnez.jpg").convert_alpha()
        self.picture_home = \
            pygame.image.load("pictures/accueil.jpg").convert_alpha()

        # Creation of pictures dimensions
        self.wall_picture = \
            pygame.transform.scale(self.wall_picture, (CASE_L, CASE_H))
        self.guardian_picture = \
            pygame.transform.scale(self.guardian_picture, (CASE_L, CASE_H))
        self.starting_picture = \
            pygame.transform.scale(self.starting_picture, (CASE_L, CASE_H))
        self.free_picture = \
            pygame.transform.scale(self.free_picture, (CASE_L, CASE_H))
        self.ether_picture = \
            pygame.transform.scale(self.ether_picture, (CASE_L, CASE_H))
        self.needle_picture = \
            pygame.transform.scale(self.needle_picture, (CASE_L, CASE_H))
        self.syringe_picture = \
            pygame.transform.scale(self.syringe_picture, (CASE_L, CASE_H))
        self.hero_picture = \
            pygame.transform.scale(self.hero_picture, (CASE_L, CASE_H))
        self.dead_picture = \
            pygame.transform.scale(self.dead_picture, (WINDOW_L, WINDOW_H))
        self.picture_win = \
            pygame.transform.scale(self.picture_win, (WINDOW_L, WINDOW_H))
        self.picture_home = \
            pygame.transform.scale(self.picture_home, (WINDOW_L, WINDOW_H))

    def reception(self):
        """home screen display"""

        # Loading and viewing the home screen
        window.blit(self.picture_home, POSITION_PIXEL_RECEPTION)

        # Refreshment
        pygame.display.flip()

    def open_file(self, p_file):
        """We open the file,
        read it and copy it to a chain.
        """
        # We open the text file
        text_file = open(p_file, "r")  # r = we read the text
        print(text_file)

        local_map_game = []
        line_map = []
        counter = 0
        for lines in text_file:
            line_map = []
            # We read each character of the file
            for character in lines:
                if character != "\n":
                    line_map.append(character)
                    # print(line_map)
            local_map_game.append(line_map)
            # print("map_game",counter)
            # print(map_game)
            counter = counter + 1

        self.map_game = local_map_game

    def mapping(self):
        """We paste the images"""

        # We browse all the rows of the table to see the characters

        for pos_v in range(0, 15):
            for pos_h in range(0, 15):

                # to each character that corresponds we paste an image
                if self.map_game[pos_h][pos_v] == WALL:
                    pixel_wall = (CASE_L * pos_v, CASE_H * pos_h)
                    window.blit(self.wall_picture, pixel_wall)

                elif self.map_game[pos_h][pos_v] == GUARDIAN:
                    self.pixel_g = (CASE_L * pos_v, CASE_H * pos_h)
                    window.blit(self.free_picture, self.pixel_g)
                    window.blit(self.guardian_picture, self.pixel_g)

                elif self.map_game[pos_h][pos_v] == STARTING:
                    self.pixel_start = (CASE_L * pos_v, CASE_H * pos_h)
                    window.blit(self.starting_picture, self.pixel_start)

                elif self.map_game[pos_h][pos_v] == NEEDLE:
                    self.pixel_n = (CASE_L * pos_v, CASE_H * pos_h)
                    window.blit(self.needle_picture, self.pixel_n)

                elif self.map_game[pos_h][pos_v] == SYRINGE:
                    self.pixel_s = (CASE_L * pos_v, CASE_H * pos_h)
                    window.blit(self.syringe_picture, self.pixel_s)

                elif self.map_game[pos_h][pos_v] == ETHER:
                    self.pixel_ether = (CASE_L * pos_v, CASE_H * pos_h)
                    window.blit(self.ether_picture, self.pixel_ether)

                else:
                    pixel_free = (CASE_L*pos_v, CASE_H*pos_h)
                    window.blit(self.free_picture, pixel_free)

        window.blit(self.hero_picture, self.pixel_hero)

        # Refresh
        pygame.display.flip()

    def creation_hero(self):
        """Creation and positioning Macgyver"""

        # Loading and pasting the character
        self.pixel_hero = self.hero_picture.get_rect()

        # reset or initialization of character positions
        self.hero_picture.get_rect() == self.map_game[0][0]

    def hazard(self, char_picture):
        """Randomly placing objects"""

        # We initialize the case
        case_hazard = ""

        while case_hazard != FREE:

            random_picture_H = randint(0, 14)
            random_picture_V = randint(0, 14)
            case_hazard = self.map_game[random_picture_H][random_picture_V]

        # We say that the position is equal to the given character
        self.map_game[random_picture_H][random_picture_V] = char_picture

    def init_case(self, position_V, position_H):
        """We reset when an object has been found, we put a FREE case"""

        self.map_game[position_V][position_H] = FREE

    def win_or_dead(self, param_player):
        """Display of victory or death images"""

        if param_player.win_game:
            window.blit(self.picture_win, POSITION_PIXEL_WIN)
            pygame.display.flip()

        elif param_player.lost_game:
            window.blit(self.dead_picture, POSITION_PIXEL_DEAD)
            pygame.display.flip()
