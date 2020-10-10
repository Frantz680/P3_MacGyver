"""
Game Help MacGyver escape!
Game in which we have to move MacGyver to escape the labyrinth.
"""

from pygame.locals import QUIT, KEYDOWN, K_F1, K_F2, K_F3, \
    K_DOWN, K_UP, K_LEFT, K_RIGHT

from frontend.graphic import Graphic, pygame
from backend.hero import Hero, NEEDLE, ETHER, SYRINGE

"""
Import different variables
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
        choice = ""

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
                        choice = "labyrinth/labyrinth_easy.txt"

                    elif event.key == K_F2:
                        loop_reception = 0
                        loop_restart = 1
                        choice = "labyrinth/labyrinth_intermediate.txt"

                    elif event.key == K_F3:
                        loop_reception = 0
                        loop_restart = 1
                        choice = "labyrinth/labyrinth_difficult.txt"

        while loop_restart:

            print("loop_restart")

            player = Hero()

            map.open_file(choice)
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
