# Importing modules
import secrets # Secrets is a crypto grade randomness library - in my opinion better than random for this.
import math # For the math
from collections import namedtuple # Named tuples will be used to store information about the rooms
from pygame import Rect # This will be used to check for collisions.


# Map variables
TILE_SIZE = 32 # Dimensions of the tiles - change if neccessary
TILE_ACROSS = 32 # Use the previous variables to set a tile width
TILE_DOWN = 24 # and tile height

# Pygame variables
# Setting the width and height of the pygame window
WIDTH = TILE_SIZE * TILE_ACROSS
HEIGHT = TILE_SIZE * TILE_DOWN

def create_map():
    Map = []
    Rooms = []

    for x in range(TILE_ACROSS):
        row = []
        for i in range(TILE_DOWN):
            row.append(0)
        Map.append(row)
    
    return Map



