import pygame
import random

# creating the data structure for pieces
# setting up global vars
# functions
# - create_grid
# - draw_grid
# - draw_window
# - rotating shape in main
# - setting up the main

"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
"""

pygame.font.init()

# GLOBALS VARS
s_width = 800
s_height = 700
play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 20 height per block
block_size = 30

top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height

# SHAPE FORMATS

S = [[\'.....\',
\'......\',
\'..00..\',
\'.00...\',
\'.....\'],
[\'.....\',
\'..0..\',
\'..00.\',
\'...0.\',
\'.....\']]

Z = [[\'.....\',
\'.....\',
\'.00..\',
\'..00.\',
\'.....\'],
[\'.....\',
\'..0..\',
\'.00..\',
\'.0...\',
\'.....\']]

I = [[\'..0..\',
\'..0..\',
\'..0..\',
\'..0..\',
\'.....\'],
[\'.....\',
\'0000.\',
\'.....\',
\'.....\',
\'.....\']]

O = [[\'.....\',
\'.....\',
\'.00..\',
\'.00..\',
\'.....\']]

J = [[\'.....\',
\'.0...\',
\'.000.\',
\'.....\',
\'.....\'],
[\'.....\',
\'..00.\',
\'..0..\',
\'..0..\',
\'.....\'],
[\'.....\',
\'.....\',
\'.000.\',
\'...0.\',
\'.....\'],
[\'.....\',
\'..0..\',
\'..0..\',
\'.00..\',
\'.....\']]

L = [[\'.....\',
\'...0.\',
\'.000.\',
\'.....\',
\'.....\'],
[\'.....\',
\'..0..\',
\'..0..\',
\'..00.\',
\'.....\'],
[\'.....\',
\'.....\',
\'.000.\',
\'.0...\',
\'.....\'],
[\'.....\',
\'.00..\',
\'..0..\',
\'..0..\',
\'.....\']]

T = [[\'.....\',
\'..0..\',
\'.000.\',
\'.....\',
\'.....\'],
[\'.....\',
\'..0..\',
\'..00.\',
\'..0..\',
\'.....\'],
[\'.....\',
\'.....\',
\'.000.\',
\'..0..\',
\'.....\'],
[\'.....\',
\'..0..\',
\'.00..\',
\'..0..\',
\'.....\']]

shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]
# index 0 - 6 represent shape


class Piece(object):
    def __init__(self,x,y,shape):
        self.x =x
        self.y= y
        self.shape =shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation=0


def create_grid(locked_positions={}):
    grid = [[(0,0,0) for _ in range(10)] for _ in range(20)]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j,i) in locked_pos:
                c= locked_pos[(j,i)]
                grid[i][j]=c
    return  grid


def convert_shape_format(shape):
    pass


def valid_space(shape, grid):
    pass


def check_lost(positions):
    pass


def get_shape():
    pass


def draw_text_middle(text, size, color, surface):
    pass


def draw_grid(surface, row, col):
    sx = top_left_x
    sy = top_left_y
    for i in range(row):
        pygame.draw.line(surface, (128,128,128), (sx, sy+ i*30), (sx + play_width, sy + i * 30))  # horizontal
        for j in range(col):
            pygame.draw.line(surface, (128,128,128), (sx + j * 30, sy), (sx + j * 30, sy + play_height))  # vertical



def clear_rows(grid, locked):


def draw_next_shape(shape, surface):


def draw_window(surface):
    pass


def main():
    pass


def main_menu():
    pass


main_menu()  # start game