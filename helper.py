''' This file contains helper classes '''

import pygame
from collections import namedtuple

class Direction:
    def __init__(self):
        ''' initialization -> encodes direction '''
        self.right = 1
        self.left = 2
        self.up = 3
        self.down = 4

class Color:
    def __init__(self):
        ''' initialization -> colors used: white, red, black, 2 blue variants '''
        self.white = (255, 255, 255)
        self.red = (200,0,0)
        self.blue1 = (0, 0, 255)
        self.blue2 = (0, 100, 255)
        self.black = (0,0,0)

class Args:
    def __init__(self, block_size=20, speed=10):
        ''' initialization -> initial setup '''
        self.block_size = block_size
        self.speed = speed
    
Point = namedtuple('Point', 'x, y')

######################################################