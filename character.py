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

            if (pacman.x + pacman_size/2) > (fruit_pix_x + wall_size/2) > (pacman.x - pacman_size/2) and (pacman.y -pacman_size/2) < (fruit_pix_y + pacman_size/2) < (pacman.y + pacman_size/2):
                fruit_map[pacman_y][pacman_x] = no_fruit
        
        def animation(self, direction):
            if direction == 'up':
                angle_list = [(radians(135), radians(405)), (radians(120), radians(420)), (radians(105), radians(435))]
            elif direction == 'down':
                angle_list = [(radians(-45), radians(225)), (radians(-60), radians(240)), (radians(-75), radians(255))] 
            elif direction == 'right':
                angle_list =  [(radians(45), radians(315)), (radians(30), radians(330)), (radians(15), radians(345))]
            elif direction == 'left':
                angle_list = [(radians(-135), radians(135)), (radians(-150), radians(150)), (radians(-165), radians(165))]
            else:
                return

            angle_list.append((radians(0), radians(0)))
            
            for start_angle, end_angle in angle_list:
                pygame.draw.arc(stage.game_dis, yellow,(pacman.x -pacman_size/2, pacman.y -pacman_size/2, pacman_size, pacman_size), start_angle, end_angle, pacman_size/2)
                pygame.display.update()
                pygame.time.wait(15)

            angle_list.reverse()

            for start_angle, end_angle in angle_list:
                pygame.draw.arc(stage.game_dis, yellow,(pacman.x -pacman_size/2, pacman.y -pacman_size/2, pacman_size, pacman_size), start_angle, end_angle, pacman_size/2)
                pygame.display.update()
                pygame.time.wait(15)

    def __init__(self):
        self.state_initial()

    def update(self, fruit_map, direction):
        self.move(direction)
        self.eat_mode.eat(fruit_map)
        self.eat_mode.animation(self.direction)

    def terminate(self):
        pass

    def state_initial(self):
        self.x, self.y = [3*wall_size + wall_size/2, 9*wall_size + wall_size/2]
        self.old_x, self.old_y = self.x, self.y
        self.eat_mode = self.EatMode()
        self.direction = 'right'
        self.x_movement = 0
        self.y_movement = 0

    def move(self, self_dir):
        self.direction = self_dir
        self.old_x = self.x
        self.old_y = self.y
    
        if self.direction == 'left':
            self.x -= pacman_velo
        elif self.direction == 'right':
            self.x += pacman_velo
        elif self.direction == 'down':
            self.y += pacman_velo
        elif self.direction == 'up':
            self.y -= pacman_velo

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
