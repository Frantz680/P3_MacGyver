"""
Game Help MacGyver escape!
Game in which we have to move MacGyver to escape the labyrinth.
"""

from front_end.graphic import *
from back_end.hero import *

"""
Import of entire file
"""


class Game:
    """
    This class is used for the operation of the games.
    """

    def game_lauch(self):
        """
        game launch
        """

        loop_reception = 1
        loop_restart = 1
        labyrinth_easy = False
        labyrinth_intermediate = False
        labyrinth_difficult = False

        map = Graphic()

        # Loop reception
        while loop_reception:

            map.reception()

            for event in pygame.event.get():

                if event.type == QUIT:
                    loop_reception = 0
                    loop_restart = 0

                elif event.type == KEYDOWN:
                    if event.key == K_F1:
                        loop_reception = 0
                        loop_restart = 1
                        print("reception F1")
                        labyrinth_easy = True

                    elif event.key == K_F2:
                        loop_reception = 0
                        loop_restart = 1
                        labyrinth_intermediate = True

                    elif event.key == K_F3:
                        loop_reception = 0
                        loop_restart = 1
                        labyrinth_difficult = True

        while loop_restart:

            print("loop_restart")

            player = Hero()
            if labyrinth_easy:
                map.open_file("labyrinth/labyrinth_easy.txt")
            elif labyrinth_intermediate:
                map.open_file("labyrinth/labyrinth_intermediate.txt")
            elif labyrinth_difficult:
                map.open_file("labyrinth/labyrinth_difficult.txt")
            map.creation_hero()
            map.mapping()
            map.hazard(NEEDLE)
            map.hazard(ETHER)
            map.hazard(SYRINGE)

            loop_game = 1

            while loop_game:
                for event in pygame.event.get():  # Waiting for events
                    if event.type == QUIT:
                        loop_game = 0
                        loop_restart = 0

                    elif event.type == KEYDOWN:
                        if event.key == K_DOWN:
                            player.move("down", map, 1, 0)

                        elif event.key == K_UP:
                            player.move("up", map, -1, 0)

                        elif event.key == K_LEFT:
                            player.move("left", map, 0, -1)

                        elif event.key == K_RIGHT:
                            player.move("right", map, 0, 1)

                player.management_found_objects(map)
                map.mapping()

                while player.lost_game or player.win_game:

                    map.win_or_dead(player)

                    for event in pygame.event.get():  # Waiting for events
                        if event.type == QUIT:
                            loop_game = 0
                            loop_restart = 0
                            player.lost_game = False
                            player.win_game = False

                        elif event.type == KEYDOWN:
                            # F1 to start over
                            if event.key == K_F1:
                                loop_game = 0
                                loop_restart = 1
                                player.lost_game = False
                                player.win_game = False
                                print("restart F1")

                            # F2 to quit
                            elif event.key == K_F2:
                                loop_game = 0
                                loop_restart = 0
                                player.lost_game = False
                                player.win_game = False
                                print("quit F2")


def main():
    """
    Function
    """
    game = Game()
    game.game_lauch()


"""
The main program
"""

if __name__ == '__main__':

    main()
