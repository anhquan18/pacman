import sys
from math import radians
from parameter import *
import pygame
import stage


class Pacman(object):
    class EatMode():
        def __init__(self, string='normal'):
            self.name = string
        
        def eat(self, fruit_map):
            pacman_x, pacman_y = stage.find_corrdinate(pacman.x, pacman.y) 

            if pacman_x == None or pacman_y == None:
                return

            fruit_pix_x, fruit_pix_y = stage.convert_to_pixel(pacman_x, pacman_y)

            if (pacman.x + pacman_size) > (fruit_pix_x + wall_size/2) > (pacman.x - pacman_size) and (pacman.y -pacman_size) < (fruit_pix_y + pacman_size) < (pacman.y + pacman_size):
                fruit_map[pacman_y][pacman_x] = no_fruit
        
        def animation(self, direction):
            if direction == 'up':
                angle_list = [(radians(45), radians(135)), (radians(60), radians(120)), (radians(75), radians(105))]
            elif direction == 'down':
                angle_list = [(radians(225), radians(315)), (radians(240), radians(300)), (radians(255), radians(285))] 
            elif direction == 'right':
                angle_list =  [(radians(-45), radians(45)), (radians(-30), radians(30)), (radians(-15), radians(15))]
            elif direction == 'left':
                angle_list = [(radians(135), radians(225)), (radians(150), radians(210)), (radians(165), radians(195))]
            else:
                return
            
            for start_angle, end_angle in angle_list:
                pygame.draw.arc(stage.game_dis, black,(pacman.x -pacman_size/2, pacman.y -pacman_size/2, pacman_size, pacman_size), start_angle, end_angle, pacman_size/2)
                #pygame.time.wait()

    def __init__(self):
        self.reset_state()

    def animate(self):
        pygame.draw.circle(stage.game_dis,yellow,(self.x, self.y),pacman_size/2)
        self.eat_mode.animation(self.direction)

    def update(self, fruit_map, direction):
        self.move(direction)
        self.eat_mode.eat(fruit_map)

    def terminate(self):
        pass

    def reset_state(self):
        self.x, self.y = [3*wall_size + wall_size/2, 9*wall_size + wall_size/2]
        self.old_x, self.old_y = self.x, self.y
        self.eat_mode = self.EatMode()
        self.direction = 'right'

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
