''' This file contains a snake_game_pygame object and the driver code '''

from pygame import quit
from game import snake_game_pygame

if __name__ == '__main__':

    game = snake_game_pygame()    
    # game loop -> continues untill game over or keyboard interrupt
    while True:
        game_over, score = game.take_step()
        if game_over:
            break

    # game over   
    print('Sorry Game Over!! Final Score: ', score)  
    quit()

##########################################################    