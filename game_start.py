import stage
import sys
import map
import character
import pygame
from pygame.locals import *

if __name__ == '__main__':
    pygame.init()
    game_fps = pygame.time.Clock()
    screen = stage.Screen()
    screen.display()
    direction = 'nothing'
    
    while True:
        screen.draw()
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    direction = 'up'
                elif event.key == K_DOWN:
                    direction = 'down'
                elif event.key == K_LEFT:
                    direction = 'left'
                elif event.key == K_RIGHT:
                    direction = 'right'
                elif event.key == K_r:
                   screen.reset_screen()
                   direction = 'left'

        character.pacman.update(stage.world_state.fruit_map, direction)

        game_fps.tick(40)
