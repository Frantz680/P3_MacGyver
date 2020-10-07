"""
This class allows you to place images and objects randomly
"""

from random import *

from init_pygame import *
from constants import *

"""
Import from random library

Import of entire modules
"""


class Graphic:
    """This class is used to display
    the images and to open the file.
    """

    def __init__(self, p_file):
        """We build the constructor."""
        self.file = p_file

        self.pixel_n = 0
        self.pixel_ether = 0
        self.pixel_s = 0

        # Loading pictures
        self.wall_picture = pygame.image.load("pictures/Mur.png").convert_alpha()
        self.free_picture = pygame.image.load("pictures/libre.png").convert_alpha()
        self.starting_picture = pygame.image.load("pictures/arriver.png").convert_alpha()
        self.guardian_picture = pygame.image.load("pictures/gardien.png").convert_alpha()
        self.needle_picture = pygame.image.load("pictures/aiguille.png").convert_alpha()
        self.ether_picture = pygame.image.load("pictures/ether.png").convert_alpha()
        self.syringe_picture = pygame.image.load("pictures/seringue.png").convert_alpha()
        self.hero_picture = pygame.image.load("pictures/macgyver.png").convert_alpha()
        self.dead_picture = pygame.image.load("pictures/mort.png").convert_alpha()
        self.picture_win = pygame.image.load("pictures/gagnez.jpg").convert_alpha()

        # Creation of pictures dimensions
        self.wall_picture = pygame.transform.scale(self.wall_picture, (CASE_L, CASE_H))
        self.guardian_picture = pygame.transform.scale(self.guardian_picture, (CASE_L, CASE_H))
        self.starting_picture = pygame.transform.scale(self.starting_picture, (CASE_L, CASE_H))
        self.free_picture = pygame.transform.scale(self.free_picture, (CASE_L, CASE_H))
        self.ether_picture = pygame.transform.scale(self.ether_picture, (CASE_L, CASE_H))
        self.needle_picture = pygame.transform.scale(self.needle_picture, (CASE_L, CASE_H))
        self.syringe_picture = pygame.transform.scale(self.syringe_picture, (CASE_L, CASE_H))
        self.hero_picture = pygame.transform.scale(self.hero_picture, (CASE_L, CASE_H))
        self.dead_picture = pygame.transform.scale(self.dead_picture, (WINDOW_L, WINDOW_H))
        self.picture_win = pygame.transform.scale(self.picture_win, (WINDOW_L, WINDOW_H))

    def open_file(self):
        """We open the file,
        read it and copy it to a chain.
        """
        # We open the text file
        text_file = open(self.file, "r")  # r = we read the text
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

        for position_V in range(0, 15):
            for position_H in range(0, 15):

                # to each character that corresponds we paste an image
                if self.map_game[position_H][position_V] == wall:
                    pixel_wall = (CASE_L*position_V, CASE_H*position_H)
                    window.blit(self.wall_picture, pixel_wall)

                elif self.map_game[position_H][position_V] == guardian:
                    self.pixel_g = (CASE_L*position_V, CASE_H*position_H)
                    window.blit(self.free_picture, self.pixel_g)
                    window.blit(self.guardian_picture, self.pixel_g)

                elif self.map_game[position_H][position_V] == starting:
                    self.pixel_start = (CASE_L*position_V, CASE_H*position_H)
                    window.blit(self.starting_picture, self.pixel_start)

                elif self.map_game[position_H][position_V] == needle:
                    self.pixel_n = (CASE_L*position_V, CASE_H*position_H)
                    window.blit(self.needle_picture, self.pixel_n)

                elif self.map_game[position_H][position_V] == syringe:
                    self.pixel_s = (CASE_L*position_V, CASE_H*position_H)
                    window.blit(self.syringe_picture, self.pixel_s)

                elif self.map_game[position_H][position_V] == ether:
                    self.pixel_ether = (CASE_L*position_V, CASE_H*position_H)
                    window.blit(self.ether_picture, self.pixel_ether)

                else:
                    pixel_free = (CASE_L*position_V, CASE_H*position_H)
                    window.blit(self.free_picture, pixel_free)

        window.blit(self.hero_picture, self.pixel_hero)

        # Refresh
        pygame.display.flip()

    def hazard(self, charactere_picture):
        """Randomly placing objects"""

        #On initialise la case_hazard
        case_hazard = ""

        while case_hazard != free:

            random_picture_H = randint(0, 14)
            random_picture_V = randint(0, 14)
            case_hazard = self.map_game[random_picture_H][random_picture_V]

        # We say that the position is equal to the given character
        self.map_game[random_picture_H][random_picture_V] = charactere_picture

    def init_case(self, position_V, position_H):
        self.map_game[position_V][position_H] = free
