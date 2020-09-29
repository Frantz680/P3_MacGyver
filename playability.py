"""
The class allows the player to move
"""

from init_pygame import *
from constants import *


class MoveHero():
    """
    This class serves to move the hero but also
    to place the objects.
    """

    def __init__(self):
        """
        We build the constructor.
        """
        self.find_s = False
        self.find_e = False
        self.find_n = False
        self.win_game = False
        self.lost_game = False
        self.map_hero_V = 0
        self.map_hero_H = 0

    def move(self, p_event, p_map):
        """
        We move the person.
        """

        if p_event == K_DOWN:  # If "down arrow"
            if self.map_hero_V != 14:
                if p_map.map_game[self.map_hero_V+1][self.map_hero_H] != 'W':

                    # We go down the hero GRAPHICALLY
                    p_map.pixel_hero = p_map.pixel_hero.move(0, CASE_H)

                    # We go down the hero PHYSICALLY
                    self.map_hero_V = self.map_hero_V + 1

                    print("position in map H : " + str(self.map_hero_H))
                    print("position in map V : " + str(self.map_hero_V))
                    print(p_map.map_game[self.map_hero_V][self.map_hero_H])

                else:
                    print("wall move down impossible")
                    print("position in map H : " + str(self.map_hero_H))
                    print("position in map V : " + str(self.map_hero_V))

        elif p_event == K_UP:  # If "up arrow"
            if self.map_hero_V != 0:
                if p_map.map_game[self.map_hero_V-1][self.map_hero_H] != 'W':

                    # We mount the hero GRAPHICALLY
                    p_map.pixel_hero = p_map.pixel_hero.move(0, -CASE_H)

                    # We mount the hero PHYSICALLY
                    self.map_hero_V = self.map_hero_V - 1

                    print("position in map H : " + str(self.map_hero_H))
                    print("position in map V : " + str(self.map_hero_V))
                    print(p_map.map_game[self.map_hero_V][self.map_hero_H])

                else:
                    print("wall moving up impossible")
                    print("position in map H : " + str(self.map_hero_H))
                    print("position in map V : " + str(self.map_hero_V))

        elif p_event == K_LEFT:  # If "left arrow"
            if self.map_hero_H != 0:
                if p_map.map_game[self.map_hero_V][self.map_hero_H-1] != 'W':

                    # The hero goes left GRAPHICALLY
                    p_map.pixel_hero = p_map.pixel_hero.move(-CASE_L, 0)

                    # The hero goes to the left PHYSICALLY
                    self.map_hero_H = self.map_hero_H - 1

                    print("position in map H : " + str(self.map_hero_H))
                    print("position in map V : " + str(self.map_hero_V))
                    print(p_map.map_game[self.map_hero_V][self.map_hero_H])

                else:
                    print("wall move to the left impossible")
                    print("position in map H : " + str(self.map_hero_H))
                    print("position in map V : " + str(self.map_hero_V))

        elif p_event == K_RIGHT:  # If "right arrow"
            if self.map_hero_H != 14:
                if p_map.map_game[self.map_hero_V][self.map_hero_H+1] != 'W':

                    # The hero goes right GRAPHICALLY
                    p_map.pixel_hero = p_map.pixel_hero.move(CASE_L, 0)

                    # The hero goes right PHYSICALLY
                    self.map_hero_H = self.map_hero_H + 1

                    print("position in map H : " + str(self.map_hero_H))
                    print("position in map V : " + str(self.map_hero_V))
                    print(p_map.map_game[self.map_hero_V][self.map_hero_H])

                else:
                    print("wall movement to the right not possible")
                    print("position in map H : " + str(self.map_hero_H))
                    print("position in map V : " + str(self.map_hero_V))

    def management_found_objects(self, p_map):
        """
        Randomly placing objects.
        """

        # If the hero goes on the object, the value becomes true
        if p_map.map_game[self.map_hero_V][self.map_hero_H] == 'E':
            print("You found the ether")
            self.find_e = True

        elif p_map.map_game[self.map_hero_V][self.map_hero_H] == 'T':
            print("You have found the syringe")
            self.find_s = True

        elif p_map.map_game[self.map_hero_V][self.map_hero_H] == 'A':
            print("You found the needle")
            self.find_n = True

        # If the hero is on the guardian
        elif p_map.map_game[self.map_hero_V][self.map_hero_H] == 'G':

            # If he finds all the objects he wins
            if self.find_e and self.find_n and self.find_s:
                self.win_game = True
                print("You have won")

            # If he doesn't find all the objects he dies
            elif not self.find_e or not self.find_n or not self.find_s:
                self.lost_game = True
                print("You are dead")
