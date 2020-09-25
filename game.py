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

    main_loop = 1

    # Main loop
    while main_loop:

        loop_reception = 1
        loop_start_over = 1

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
                    game_loop = 0
                    main_loop = 0
                    loop_start_over = 0

                elif event.type == KEYDOWN:
                    if event.key == K_F1:
                        loop_reception = 0
                        loop_start_over = 1
                        print("reception F1")
                        map = Graphic("laby.txt")

                    elif event.key == K_F2:
                        loop_reception = 0
                        loop_start_over = 1
                        map = Graphic("laby_moyen.txt")

                    elif event.key == K_F3:
                        loop_reception = 0
                        loop_start_over = 1
                        map = Graphic("laby_difficile.txt")

        while loop_start_over:

            print("loop_start_over")

            player = MoveHero()

            map.open_file()

            map.mapping()

            map.hazard()

            # Loading and pasting the character
            map.pixel_hero = hero_picture.get_rect()
            window.blit(hero_picture, map.pixel_hero)

            # reset or initialization of character positions
            hero_picture.get_rect() == map.map_game[0][0]

            game_loop = 1

            # Infinite loop
            while game_loop:
                for event in pygame.event.get():  # Waiting for events
                    if event.type == QUIT:
                        game_loop = 0
                        main_loop = 0
                        loop_start_over = 0

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
                            game_loop = 0
                            main_loop = 0
                            loop_start_over = 0
                            player.lost_game = False
                            player.win_game = False

                        elif event.type == KEYDOWN:
                            # F1 to start over
                            if event.key == K_F1:
                                game_loop = 0
                                loop_start_over = 1
                                player.lost_game = False
                                player.win_game = False
                                print("restart F1")

                            # F2 to quit
                            elif event.key == K_F2:
                                game_loop = 0
                                main_loop = 0
                                loop_start_over = 0
                                player.lost_game = False
                                player.win_game = False
                                print("quit F2")


def main():
    """
    Function
    """
    Game()


"""
The main program
"""

if __name__ == '__main__':

    game = Game()
    main()
