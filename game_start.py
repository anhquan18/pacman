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
    pacman_direction = 'right'
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    pacman_direction = 'up'
                elif event.key == K_DOWN:
                    pacman_direction = 'down'
                elif event.key == K_LEFT:
                    pacman_direction = 'left'
                elif event.key == K_RIGHT:
                    pacman_direction = 'right'
                elif event.key == K_r:
                   screen.reset_screen()
                   pacman_direction = 'left'

        screen.update(pacman_direction)
        game_fps.tick(60)
