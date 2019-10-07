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

# Room variables
MAX_ROOM_SIZE = 7 # Rooms should be no more than 7 tiles wide or high
MIN_ROOM_SIZE = 3 # Or any less than 3 on either side

MAP_BORDER = 1 # There should be a border of 1 tile around the map

# Using a names tuple to store information about the rooms - so I can do things like room.x or room.width
Room = namedtuple('Room', ['width', 'height', 'pos_x', 'pos_y'])

def generate_room():
    rm_width = MIN_ROOM_SIZE + secrets.randbelow(MAX_ROOM_SIZE - MIN_ROOM_SIZE + 1)
    rm_height = MIN_ROOM_SIZE + secrets.randbelow(MAX_ROOM_SIZE - MIN_ROOM_SIZE + 1)

    rm_pos_x = secrets.randbelow(TILE_ACROSS - rm_width)
    if rm_pos_x < MAP_BORDER:
        rm_pos_x = MAP_BORDER
    rm_pos_y = secrets.randbelow(TILE_DOWN - rm_height)
    if rm_pos_y < MAP_BORDER:
        rm_pos_y = MAP_BORDER

    return Room(rm_width, rm_height, rm_pos_x, rm_pos_y)

ROOM_PADDING = 2

NUMBER_OF_ROOMS = 12

def create_rooms():
    Rooms = []
    for i in range(NUMBER_OF_ROOMS):
        intersect = True
        while intersect: 
            intersect = False
            rm = generate_room()
            for other in Rooms:
                room = other[0]
                padded_pos_x = rm.pos_x - 1
                padded_pos_y = rm.pos_y - 1
                padded_width = rm.width + 3
                padded_height = rm.height + 3
                rm_1 = Rect((room.pos_x*32, room.pos_y*32),
                                 (room.width*32, room.height*32))
                rm_2 = Rect((padded_pos_x*32, padded_pos_y*32),
                                 (padded_width*32, padded_height*32))
                if rm_1.colliderect(rm_2):
                    intersect = True
        Rooms.append([rm, {"NORTH": None, "SOUTH": None, "EAST": None, "WEST": None}])
    return Rooms

def create_map():
    Map = []
    for x in range(TILE_ACROSS):
        row = []
        for i in range(TILE_DOWN):
            row.append(0)
        Map.append(row)
    Rooms = create_rooms()
    for rm in Rooms:
        for i in range(rm[0].width):
            for j in range(rm[0].height):
                Map[rm[0].pos_x+i][rm[0].pos_y+j] = 1
    return Map



