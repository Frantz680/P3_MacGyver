"""
Game Help MacGyver escape!
Game in which we have to move MacGyver to escape the labyrinth.
"""

from movehero import *
from graphic import *


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

        # Loop reception
        while loop_reception:

            # Loading and viewing the home screen
            position_pixel_reception = (0, 0)
            window.blit(picture_home, position_pixel_reception)

            # Refreshment
            pygame.display.flip()

            for event in pygame.event.get():

                if event.type == QUIT:
                    loop_reception = 0
                    loop_restart = 0

                elif event.type == KEYDOWN:
                    if event.key == K_F1:
                        loop_reception = 0
                        loop_restart = 1
                        print("reception F1")
                        map = Graphic("labyrinth/laby.txt")

                    elif event.key == K_F2:
                        loop_reception = 0
                        loop_restart = 1
                        map = Graphic("labyrinth/laby_moyen.txt")

                    elif event.key == K_F3:
                        loop_reception = 0
                        loop_restart = 1
                        map = Graphic("labyrinth/laby_difficile.txt")

        while loop_restart:

            print("loop_restart")

            player = MoveHero()

            map.open_file()

            map.hazard("N")
            map.hazard("E")
            map.hazard("P")

            # Loading and pasting the character
            map.pixel_hero = map.hero_picture.get_rect()
            window.blit(map.hero_picture, map.pixel_hero)

            # reset or initialization of character positions
            map.hero_picture.get_rect() == map.map_game[0][0]

            map.mapping()
            loop_game = 1

            while loop_game:
                for event in pygame.event.get():  # Waiting for events
                    if event.type == QUIT:
                        loop_game = 0
                        loop_restart = 0

                    elif event.type == KEYDOWN:
                        player.move(event.key, map)
                        player.management_found_objects(map)

                map.mapping()

                while player.lost_game or player.win_game:

                    if player.win_game:
                        window.blit(map.picture_win, POSITION_PIXEL_WIN)
                        pygame.display.flip()

                    elif player.lost_game:
                        window.blit(map.dead_picture, POSITION_PIXEL_DEAD)
                        pygame.display.flip()

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
