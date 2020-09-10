from graphic import *

class move_hero():
    def __init__(self):
        self.find_ether = False
        self.find_syringe = False
        self.find_needle = False
        self.lost_game = False
        self.win_game = False

    def move(self,param_event,param_map):

        global position_perso_map_V
        global position_perso_map_H

        if param_event == K_DOWN:  # Si "flèche bas"
            if position_perso_map_V != 14:
                if param_map.map_game[position_perso_map_V + 1][position_perso_map_H] != 'W':

                    # We go down the hero GRAPHICALLY
                    param_map.position_pixel_perso = param_map.position_pixel_perso.move(0, case_height)

                    # We go down the hero PHYSICALLY
                    position_perso_map_V = position_perso_map_V + 1

                    print("position in map horizontally : " + str(position_perso_map_H))
                    print("position in map vertically : " + str(position_perso_map_V))
                    print(param_map.map_game[position_perso_map_V][position_perso_map_H])

                else:
                    print("wall move down impossible")
                    print("position in map horizontally : " + str(position_perso_map_H))
                    print("position in map vertically : " + str(position_perso_map_V))


        elif param_event == K_UP:  # If "up arrow"
            if position_perso_map_V != 0:
                if param_map.map_game[position_perso_map_V - 1][position_perso_map_H] != 'W':

                    # We mount the hero GRAPHICALLY
                    param_map.position_pixel_perso = param_map.position_pixel_perso.move(0, -case_height)

                    # We mount the hero PHYSICALLY
                    position_perso_map_V = position_perso_map_V - 1

                    print("position in map horizontally : " + str(position_perso_map_H))
                    print("position in map vertically : " + str(position_perso_map_V))
                    print(param_map.map_game[position_perso_map_V][position_perso_map_H])

                else:
                    print("wall moving up impossible")
                    print("position in map horizontally : " + str(position_perso_map_H))
                    print("position in map vertically : " + str(position_perso_map_V))


        elif param_event == K_LEFT:  # If "left arrow"
            if position_perso_map_H != 0:
                if param_map.map_game[position_perso_map_V][position_perso_map_H - 1] != 'W':

                    # The hero goes left GRAPHICALLY
                    param_map.position_pixel_perso = param_map.position_pixel_perso.move(-case_length, 0)

                    # The hero goes to the left PHYSICALLY
                    position_perso_map_H = position_perso_map_H - 1

                    print("position in map horizontally : " + str(position_perso_map_H))
                    print("position in map vertically : " + str(position_perso_map_V))
                    print(param_map.map_game[position_perso_map_V][position_perso_map_H])

                else:
                    print("wall move to the left impossible")
                    print("position in map horizontally : " + str(position_perso_map_H))
                    print("position in map vertically : " + str(position_perso_map_V))


        elif param_event == K_RIGHT:  # If "right arrow"
            if position_perso_map_H != 14:
                if param_map.map_game[position_perso_map_V][position_perso_map_H + 1] != 'W':

                    # The hero goes right GRAPHICALLY
                    param_map.position_pixel_perso = param_map.position_pixel_perso.move(case_length, 0)

                    # The hero goes right PHYSICALLY
                    position_perso_map_H = position_perso_map_H + 1

                    print("position in map horizontally : " + str(position_perso_map_H))
                    print("position in map vertically : " + str(position_perso_map_V))
                    print(param_map.map_game[position_perso_map_V][position_perso_map_H])

                else:
                    print("wall movement to the right not possible")
                    print("position in map horizontally : " + str(position_perso_map_H))
                    print("position in map vertically : " + str(position_perso_map_V))


    def management_found_objects(self, param_map):


        # If the hero goes on the object, the value becomes true
        if param_map.map_game[position_perso_map_V][position_perso_map_H] == 'E':
            print("You found the ether")
            self.find_ether = True

        elif param_map.map_game[position_perso_map_V][position_perso_map_H] == 'T':
            print("You have found the syringe")
            self.find_syringe = True

        elif param_map.map_game[position_perso_map_V][position_perso_map_H] == 'A':
            print("You found the needle")
            self.find_needle = True

        # If the hero is on the guardian
        elif param_map.map_game[position_perso_map_V][position_perso_map_H] == 'G':

            # If he finds all the objects he wins
            if self.find_ether == True and self.find_needle == True and self.find_syringe == True:
                self.win_game = True
                print("You have won")

            # If he doesn't find all the objects he dies
            elif self.find_ether == False or self.find_needle == False or self.find_syringe == False:
                self.lost_game = True
                print("You are dead")