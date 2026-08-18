"""
This is our main driver file. It will be responsible for handling user input and displaying the current GameState object. 
"""

import pygame as p
import ChessEngine

WIDTH = HEIGHT = 512 # 400 is another option
DIMENSION = 8 # dimensions of a chess board are 8x8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15 # for animations later on
IMAGES = {}

'''
Initialize a global dictionary of images. This will be called exactly once in the main
'''

def loadImages():
    IMAGES['wP'] = p.image.load("images/wP.png")