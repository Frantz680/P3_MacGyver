from random import *

from init_pygame import *
from constantes import *

"""This class is used to display 
the images and to open the file.
"""


class Graphic():

    """We build the constructor."""
    def __init__(self, p_file):
        self.file = p_file
        self.position_pixel_perso = [0][0]

    """We open the file, 
    read it and copy it to a chain."""
    def open_file(self):

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

    """We paste the images"""
    def mapping(self):

        # We browse all the rows of the table to see the characters
        for position_V_map in range(0, 15):
            for position_H_map in range(0, 15):

                # to each character that corresponds we paste an image
                if self.map_game[position_H_map][position_V_map] == 'W':
                    position_pixel_wall = (CASE_LENGTH * position_V_map, CASE_HEIGHT * position_H_map)
                    window.blit(wall_picture, position_pixel_wall)

                elif self.map_game[position_H_map][position_V_map] == 'G':
                    self.position_pixel_guardian = (CASE_LENGTH * position_V_map, CASE_HEIGHT * position_H_map)
                    window.blit(guardian_picture, self.position_pixel_guardian)

                elif self.map_game[position_H_map][position_V_map] == 'S':
                    self.position_pixel_starting = (CASE_LENGTH * position_V_map, CASE_HEIGHT * position_H_map)
                    window.blit(starting_picture, self.position_pixel_starting)

                else:
                    position_pixel_free = (CASE_LENGTH * position_V_map, CASE_HEIGHT * position_H_map)
                    window.blit(free_picture, position_pixel_free)

    """Randomly placing objects"""
    def hazard(self):

        # choose a random number in the map for ether
        position_ether = 'E'
        nb_hazard_ether = 0
        random_number_ether_H = randint(0, 14)
        random_number_ether_V = randint(0, 14)

        # As long as the random number is different from the free cells
        while nb_hazard_ether != 'F':
            random_number_ether_H = randint(0, 14)
            random_number_ether_V = randint(0, 14)
            nb_hazard_ether = self.map_game[random_number_ether_V][random_number_ether_H]

            # Once the number obtained we paste the image
            self.position_pixel_ether = (CASE_LENGTH * random_number_ether_H, CASE_HEIGHT * random_number_ether_V)
            window.blit(ether_picture, self.position_pixel_ether)

        # We say that the position is equal to the character given
        self.map_game[random_number_ether_V][random_number_ether_H] = position_ether

        # choose a random number in the map for the needle
        position_needle = 'A'
        nb_hazard_needle = 0
        random_number_needle_H = randint(0, 14)
        random_number_needle_V = randint(0, 14)

        # As long as the random number is different from the free cells
        while nb_hazard_needle != 'F' and nb_hazard_needle != 'A':
            random_number_needle_H = randint(0, 14)
            random_number_needle_V = randint(0, 14)
            nb_hazard_needle = self.map_game[random_number_needle_V][random_number_needle_H]

            # Once the number obtained we paste the image
            self.position_pixel_needle = (CASE_LENGTH * random_number_needle_H, CASE_HEIGHT * random_number_needle_V)
            window.blit(needle_picture, self.position_pixel_needle)

        # We say that the position is equal to the character given
        self.map_game[random_number_needle_V][random_number_needle_H] = position_needle

        # choose a random number in the map for the syringe
        position_syringe = 'T'
        nb_hazard_syringe = 0
        random_number_syringe_H = randint(0, 14)
        random_number_syringe_V = randint(0, 14)

        # As long as the random number is different from the free cells
        while nb_hazard_syringe != 'F' and nb_hazard_syringe != 'A' and nb_hazard_syringe != 'T':
            random_number_syringe_H = randint(0, 14)
            random_number_syringe_V = randint(0, 14)
            nb_hazard_syringe = self.map_game[random_number_syringe_V][random_number_syringe_H]

            # Once the number obtained we paste the image
            self.position_pixel_syringe = (CASE_LENGTH * random_number_syringe_H, CASE_HEIGHT * random_number_syringe_V)
            window.blit(syringe_picture, self.position_pixel_syringe)

        # We say that the position is equal to the given character
        self.map_game[random_number_syringe_V][random_number_syringe_H] = position_syringe

    """We glue the images again"""
    def again_glue(self,param_find_syringe,param_find_ether,param_find_needle):

        for position_V_map in range(0, 15):
            for position_H_map in range(0, 15):
                if self.map_game[position_H_map][position_V_map] == 'W':
                    position_pixel_wall = (CASE_LENGTH * position_V_map, CASE_HEIGHT * position_H_map)
                    window.blit(wall_picture, position_pixel_wall)
                else:
                    position_pixel_free = (CASE_LENGTH * position_V_map, CASE_HEIGHT * position_H_map)
                    window.blit(free_picture, position_pixel_free)

        window.blit(starting_picture, self.position_pixel_starting)
        window.blit(hero_picture, self.position_pixel_perso)
        window.blit(guardian_picture, self.position_pixel_guardian)

        if param_find_syringe == False:
            window.blit(syringe_picture, self.position_pixel_syringe)
        if param_find_ether == False:
            window.blit(ether_picture, self.position_pixel_ether)
        if param_find_needle == False:
            window.blit(needle_picture, self.position_pixel_needle)

        # Refresh
        pygame.display.flip()

