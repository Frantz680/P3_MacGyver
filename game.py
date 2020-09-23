"""
Game Help MacGyver escape!
Game in which we have to move MacGyver to escape the labyrinth.
"""

from playability import *
from graphic import *

"""
The class
"""


class Game():

    # creation of the player object
    player = MoveHero()

    main_loop = 1

    # Main loop
    while main_loop:

        loop_reception = 1
        loop_start_over = 1

        # Loop reception
        while loop_reception:

            # Loading and viewing the home screen
            position_pixel_reception = (0, 0)
            window.blit(picture_reception, position_pixel_reception)

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
                        map_choix = Graphic("laby.txt")

                    elif event.key == K_F2:
                        loop_reception = 0
                        loop_start_over = 1
                        map_choix = Graphic("laby_moyen.txt")

                    elif event.key == K_F3:
                        loop_reception = 0
                        loop_start_over = 1
                        map_choix = Graphic("laby_difficile.txt")

        while loop_start_over:

            print("loop_start_over")

            player.init()

            map_choix.open_file()

            map_choix.mapping()

            map_choix.hazard()

            # Loading and pasting the character
            map_choix.position_pixel_perso = hero_picture.get_rect()
            window.blit(hero_picture, map_choix.position_pixel_perso)

            # reset or initialization of character positions
            hero_picture.get_rect() == map_choix.map_game[0][0]

            game_loop = 1

            # Infinite loop
            while game_loop:
                for event in pygame.event.get():  # Waiting for events
                    if event.type == QUIT:
                        game_loop = 0
                        main_loop = 0
                        loop_start_over = 0

                    elif event.type == KEYDOWN:
                        player.move(event.key, map_choix)
                        player.management_found_objects(map_choix)

                map_choix.again_glue(player.find_syringe, player.find_ether, player.find_needle)

                while player.lost_game == True or player.win_game == True:

                    if player.win_game == True:
                        window.blit(picture_win, POSITION_PIXEL_WIN)
                        pygame.display.flip()

                    elif player.lost_game == True:
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


"""
Function
"""


def main():

    Game()


"""
The main program
"""

if __name__ == '__main__':

    game = Game()
    main()
