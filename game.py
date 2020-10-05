"""
Game Help MacGyver escape!
Game in which we have to move MacGyver to escape the labyrinth.
"""

from playability import *
from graphic import *


class Game():
    """
    This class is used for the operation of the games.
    """

    def run(self):

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
                    loop_game = 0
                    loop_restart = 0

                elif event.type == KEYDOWN:
                    if event.key == K_F1:
                        loop_reception = 0
                        loop_restart = 1
                        print("reception F1")
                        map = Graphic("laby.txt")

                    elif event.key == K_F2:
                        loop_reception = 0
                        loop_restart = 1
                        map = Graphic("laby_moyen.txt")

                    elif event.key == K_F3:
                        loop_reception = 0
                        loop_restart = 1
                        map = Graphic("laby_difficile.txt")

        while loop_restart:

            print("loop_restart")

            player = MoveHero()

            map.open_file()

            map.mapping()

            map.hazard()

            # Loading and pasting the character
            map.pixel_hero = hero_picture.get_rect()
            window.blit(hero_picture, map.pixel_hero)

            # reset or initialization of character positions
            hero_picture.get_rect() == map.map_game[0][0]

            loop_game = 1

            while loop_game:
                for event in pygame.event.get():  # Waiting for events
                    if event.type == QUIT:
                        loop_game = 0
                        loop_restart = 0

                    elif event.type == KEYDOWN:
                        player.move(event.key, map)
                        player.management_found_objects(map)

                map.again_glue(player.find_s, player.find_e, player.find_n)

                while player.lost_game or player.win_game:

                    if player.win_game:
                        window.blit(picture_win, POSITION_PIXEL_WIN)
                        pygame.display.flip()

                    elif player.lost_game:
                        window.blit(dead_picture, POSITION_PIXEL_DEAD)
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
    game.run()


"""
The main program
"""

if __name__ == '__main__':

    main()
