"""
This class allows you to place images and objects randomly
"""

from random import *

from init_pygame import *
from constantes import *

"""
Import from random library

Import of entire modules
"""


class Graphic():
    """This class is used to display
    the images and to open the file.
    """

    def __init__(self, p_file):
        """We build the constructor."""
        self.file = p_file
        self.pixel_hero = [0][0]

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
                if self.map_game[position_H][position_V] == 'W':
                    pixel_wall = (CASE_L*position_V, CASE_H*position_H)
                    window.blit(wall_picture, pixel_wall)

                elif self.map_game[position_H][position_V] == 'G':
                    self.pixel_g = (CASE_L*position_V, CASE_H*position_H)
                    window.blit(guardian_picture, self.pixel_g)

                elif self.map_game[position_H][position_V] == 'S':
                    self.pixel_start = (CASE_L*position_V, CASE_H*position_H)
                    window.blit(starting_picture, self.pixel_start)

                else:
                    pixel_free = (CASE_L*position_V, CASE_H*position_H)
                    window.blit(free_picture, pixel_free)

    def hazard(self):
        """Randomly placing objects"""
        # choose a random number in the map for ether
        position_ether = 'E'
        nb_hazard_ether = 0
        random_ether_H = randint(0, 14)
        random_ether_V = randint(0, 14)

        # As long as the random number is different from the free cells
        while nb_hazard_ether != 'F':
            random_ether_H = randint(0, 14)
            random_ether_V = randint(0, 14)
            nb_hazard_ether = self.map_game[random_ether_V][random_ether_H]

            # Once the number obtained we paste the image
            self.pixel_ether = (CASE_L*random_ether_H, CASE_H*random_ether_V)
            window.blit(ether_picture, self.pixel_ether)

        # We say that the position is equal to the character given
        self.map_game[random_ether_V][random_ether_H] = position_ether

        # choose a random number in the map for the needle
        position_needle = 'A'
        nb_hazard_needle = 0
        random_needle_H = randint(0, 14)
        random_needle_V = randint(0, 14)

        # As long as the random number is different from the free cells
        while nb_hazard_needle != 'F' and nb_hazard_needle != 'A':
            random_needle_H = randint(0, 14)
            random_needle_V = randint(0, 14)
            nb_hazard_needle = self.map_game[random_needle_V][random_needle_H]

            # Once the number obtained we paste the image
            self.pixel_n = (CASE_L*random_needle_H, CASE_H*random_needle_V)
            window.blit(needle_picture, self.pixel_n)

        # We say that the position is equal to the character given
        self.map_game[random_needle_V][random_needle_H] = position_needle

        # choose a random number in the map for the syringe
        position_syringe = 'T'
        nb_hazard_s = 0
        random_syringe_H = randint(0, 14)
        random_syringe_V = randint(0, 14)

        # As long as the random number is different from the free cells
        while nb_hazard_s != 'F' and nb_hazard_s != 'A' and nb_hazard_s != 'T':
            random_syringe_H = randint(0, 14)
            random_syringe_V = randint(0, 14)
            nb_hazard_s = self.map_game[random_syringe_V][random_syringe_H]

            # Once the number obtained we paste the image
            self.pixel_s = (CASE_L*random_syringe_H, CASE_H*random_syringe_V)
            window.blit(syringe_picture, self.pixel_s)

        # We say that the position is equal to the given character
        self.map_game[random_syringe_V][random_syringe_H] = position_syringe

    def again_glue(self, p_find_s, p_find_e, p_find_n):
        """We glue the images again"""

        for position_V in range(0, 15):
            for position_H in range(0, 15):
                if self.map_game[position_H][position_V] == 'W':
                    pixel_wall = (CASE_L*position_V, CASE_H*position_H)
                    window.blit(wall_picture, pixel_wall)
                else:
                    pixel_free = (CASE_L*position_V, CASE_H*position_H)
                    window.blit(free_picture, pixel_free)

        window.blit(starting_picture, self.pixel_start)
        window.blit(hero_picture, self.pixel_hero)
        window.blit(guardian_picture, self.pixel_g)

        if not p_find_s:
            window.blit(syringe_picture, self.pixel_s)
        if not p_find_e:
            window.blit(ether_picture, self.pixel_ether)
        if not p_find_n:
            window.blit(needle_picture, self.pixel_n)

        # Refresh
        pygame.display.flip()
