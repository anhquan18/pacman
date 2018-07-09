import sys
import math
from parameter import *
import pygame
import stage


class Pacman(object):
    def animate(self):
        pygame.draw.circle(stage.game_dis,yellow,(self.x, self.y),pacman_size/2)

    class Mode(object):
        def __init__(self, string='normal'):
            self.name = string

    def __init__(self):
        self.reset_state()

    def terminate(self):
        pass

    def reset_state(self):
        self.x, self.y = [3*wall_size + wall_size/2, 9*wall_size + wall_size/2]
        self.old_x, self.old_y = self.x, self.y
        self.mode = self.Mode()
        self.direction = 'nothing'

    def move(self, self_dir):
        self.direction = self_dir
        self.old_x = self.x
        self.old_y = self.y
    
        if self.direction == 'left':
            self.x -= 5
        elif self.direction == 'right':
            self.x += 5
        elif self.direction == 'down':
            self.y += 5
        elif self.direction == 'up':
            self.y -= 5

        wall_direction = stage.check_wall(self.x, self.y)
        stage.move_easier(wall_direction)


class Ghost(object):
    class Animation(object):
        pass

    def __init__(self, color):
        self.color = color

    def terminate_pacman(self):
        pass

    def reborn(self):
        pass

    def terminate(self):
        pass

    def move(self):
        pass

pacman = Pacman()
ghost = Ghost(red)
