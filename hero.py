"""
The class allows to create the hero
"""

from constants import *


class Hero:
    """
    This class is used to create the hero to move
    him but also if he picks up objects.
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

    def move(self, str_event, p_map, increment_V, increment_H):
        """
        We move the person.
        """

        print("position in map H : " + str(self.map_hero_H))
        print("position in map V : " + str(self.map_hero_V))

        if self.map_hero_V + increment_V == -1 or self.map_hero_V + increment_V == 15:
            print("debordement move " + str_event + " impossible")
            return # On sort de la methode

        if self.map_hero_H + increment_H == -1 or self.map_hero_H + increment_H == 15:
            print("debordement move " + str_event + " impossible")
            return

        if p_map.map_game[self.map_hero_V + increment_V][self.map_hero_H + increment_H] != wall:

            # We go down the hero GRAPHICALLY
            p_map.pixel_hero = p_map.pixel_hero.move(CASE_L * increment_H, CASE_H * increment_V)

            # We go down the hero PHYSICALLY
            self.map_hero_V = self.map_hero_V + increment_V
            self.map_hero_H = self.map_hero_H + increment_H
            print(p_map.map_game[self.map_hero_V][self.map_hero_H])

        else:
            print("wall move " + str_event + " impossible")

    def management_found_objects(self, p_map):
        """
        Randomly placing objects.
        """

        # If the hero goes on the object, the value becomes true
        if p_map.map_game[self.map_hero_V][self.map_hero_H] == ether:
            p_map.init_case(self.map_hero_V, self.map_hero_H) # Permet de mettre la case en libre
            print("You found the ether")
            self.find_e = True

        elif p_map.map_game[self.map_hero_V][self.map_hero_H] == syringe:
            p_map.init_case(self.map_hero_V, self.map_hero_H)
            print("You have found the syringe")
            self.find_s = True

        elif p_map.map_game[self.map_hero_V][self.map_hero_H] == needle:
            p_map.init_case(self.map_hero_V, self.map_hero_H)
            print("You found the needle")
            self.find_n = True

        # If the hero is on the guardian
        elif p_map.map_game[self.map_hero_V][self.map_hero_H] == guardian:

            # If he finds all the objects he wins
            if self.find_e and self.find_n and self.find_s:
                self.win_game = True
                print("You have won")

            # If he doesn't find all the objects he dies
            elif not self.find_e or not self.find_n or not self.find_s:
                self.lost_game = True
                print("You are dead")