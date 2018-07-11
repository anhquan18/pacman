import math
import sys
import pygame
import map
import character
from parameter import *


class Screen(object):
    def __init__(self):
        self.row = game_max_row
        self.col = game_max_col
        self.win_height = max_height
        self.win_width = max_width

    def display(self):
        global game_dis
        game_dis = pygame.display.set_mode((self.win_width, self.win_height))
        pygame.display.set_caption('PACMAN')

    def update(self, pacman_direction):
        for y in range(self.row):
            for x in range(self.col):
                if world_state.game_map[y][x] == have_wall:
                    color = wall_color
                else:
                    color = black
                pygame.draw.rect(game_dis, color, (x*wall_size,y*wall_size, wall_size, wall_size))
                if world_state.fruit_map[y][x] != no_fruit:
                    pygame.draw.circle(game_dis, yellow, (x*wall_size + (wall_size/2), y*wall_size + (wall_size/2)),8)

        character.pacman.update(world_state.fruit_map, pacman_direction)
        pygame.display.update()

    def reset_screen(self):
        world_state.reset_map()
        character.pacman.reset_state()
    
    def change_screen(self):
        pass


class WorldState(object):
    def __init__(self):
        self.reset_map()

    def reset_map(self):
        self.game_map = map.create_game_map()
        self.fruit_map = map.create_fruit_map()


class ReadyScreen(Screen):
    def __init__(self):
        pass


class EndScreen(Screen):
    def __init__(self):
        pass


class GameScreen(Screen):
    def __init__(self):
        pass

    def draw(self):
        pass

    def world_state(self):
        pass

    def update(self):
        pass


def convert_to_pixel(x, y):
    x_pixel = wall_size * x
    y_pixel = wall_size * y
    return x_pixel, y_pixel


def find_corrdinate(x, y):
    for y_cor in range(game_max_row):
        for x_cor in range(game_max_col):
            x_pixel, y_pixel = convert_to_pixel(x_cor, y_cor)
            check_box = pygame.Rect(x_pixel, y_pixel, wall_size, wall_size)
            if check_box.collidepoint(x, y):
                return x_cor, y_cor
    return None, None


def check_wall(x, y):
    x, y = find_corrdinate(x, y)
    wall = []

    if x == None or y == None or \
        x == game_min_col or x == (game_max_col -1) or \
        y == game_min_row or y == (game_max_row -1):
        return wall

    if world_state.game_map[y-1][x] == have_wall:
        wall.append('up')
    if world_state.game_map[y+1][x] == have_wall:
        wall.append('down')
    if world_state.game_map[y][x-1] == have_wall:
        wall.append('left')
    if world_state.game_map[y][x+1] == have_wall:
        wall.append('right')
    if world_state.game_map[x+1][y+1] == have_wall:
        wall.append('bottom_right')
    if world_state.game_map[x+1][y-1] == have_wall:
        wall.append('top_right')
    if world_state.game_map[x-1][y+1] == have_wall:
        wall.append('bottom_left')
    if world_state.game_map[x-1][y-1] == have_wall:
        wall.append('top_left')

    return wall


def move_easier(wall_direction):
    self_x, self_y = find_corrdinate(character.pacman.x, character.pacman.y)
    threshhold = 40

    if len(wall_direction) > 0: # create limitness in order not to go through the wall
        for direction in wall_direction:
            if direction == 'up':
                if (character.pacman.y - pacman_size/2) < convert_to_pixel(self_x, self_y)[1]:
                    character.pacman.y = character.pacman.old_y
            elif direction == 'down':
                if (character.pacman.y + pacman_size/2) > convert_to_pixel(self_x, self_y + 1)[1]:
                    character.pacman.y = character.pacman.old_y
            elif direction == 'left':
                if (character.pacman.x - pacman_size/2) < convert_to_pixel(self_x, self_y)[0]:
                    character.pacman.x = character.pacman.old_x
            elif direction == 'right':
                if (character.pacman.x + pacman_size/2) > convert_to_pixel(self_x + 1, self_y)[0]:
                    character.pacman.x = character.pacman.old_x
            elif direction == 'top_right':
                if (convert_to_pixel(self_x, self_y+1)[1] + threshhold) > character.pacman.y and \
                    character.pacman.y > (convert_to_pixel(self_x, self_y)[1] - threshhold):
                    if character.pacman.direction == 'right':
                        character.pacman.y = convert_to_pixel(self_x, self_y)[1] + pacman_size/2
                if (convert_to_pixel(self_x, self_y)[0] - threshhold) < character.pacman.x and \
                    character.pacman.x < (convert_to_pixel(self_x+1, self_y)[0] + threshhold):
                    if character.pacman.direction == 'up':
                        character.pacman.x = convert_to_pixel(self_x, self_y)[0] + pacman_size/2
            elif direction == 'top_left':
                if character.pacman.y > (convert_to_pixel(self_x, self_y)[1] - threshhold) and \
                    (character.pacman.y + pacman_size/2) < (convert_to_pixel(self_x, self_y+1)[1] + threshhold):
                    if character.pacman.direction == 'left':
                        character.pacman.y = convert_to_pixel(self_x, self_y)[1] + pacman_size/2
                if (convert_to_pixel(self_x+1, self_y)[0] + threshhold) > character.pacman.x and \
                        (character.pacman.x - pacman_size/2) > (convert_to_pixel(self_x, self_y)[0] - threshhold):
                    if character.pacman.direction == 'up':
                        character.pacman.x = convert_to_pixel(self_x, self_y)[0] + pacman_size/2
            elif direction == 'bottom_right':
                if (convert_to_pixel(self_x, self_y+1)[1] + threshhold) > character.pacman.y and \
                    character.pacman.y > (convert_to_pixel(self_x, self_y)[1] - threshhold):
                    if character.pacman.direction == 'right':
                        character.pacman.y = convert_to_pixel(self_x, self_y)[1] + pacman_size/2
                if (convert_to_pixel(self_x+1, self_y)[0] + threshhold) > character.pacman.x and \
                    character.pacman.x > (convert_to_pixel(self_x, self_y)[0] - threshhold):
                    if character.pacman.direction == 'down':
                        character.pacman.x = convert_to_pixel(self_x, self_y)[0] + pacman_size/2
            elif direction == 'bottom_left':
                if character.pacman.y > (convert_to_pixel(self_x, self_y)[1] - threshhold) and \
                    character.pacman.y < (convert_to_pixel(self_x, self_y+1)[1] + threshhold):
                    if character.pacman.direction == 'left':
                        character.pacman.y = convert_to_pixel(self_x, self_y)[1] + pacman_size/2
                if (convert_to_pixel(self_x+1, self_y)[0] + threshhold) > character.pacman.x and \
                    character.pacman.x  > (convert_to_pixel(self_x, self_y)[0] - threshhold):
                    if character.pacman.direction == 'down':
                        character.pacman.x = convert_to_pixel(self_x, self_y)[0] + pacman_size/2

    if (character.pacman.y - pacman_size/2) >= max_height:
        character.pacman.y = min_height - pacman_size/2
    elif (character.pacman.x - pacman_size/2) >= max_width:
        character.pacman.x = min_width - pacman_size/2
    elif (character.pacman.y + pacman_size/2) <= min_height:
        character.pacman.y = max_height + pacman_size/2
    elif (character.pacman.x + pacman_size/2) <= min_width:
        character.pacman.x = max_width + pacman_size/2


world_state = WorldState()
