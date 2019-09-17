import secrets
import math

WIDTH = 1024
HEIGHT = 768

room_tile = "sprite_00.png"
dirt_tile = "sprite_01.png"

TILE_SIZE = 32
TILE_ACROSS = int(WIDTH/TILE_SIZE)
TILE_DOWN = int(HEIGHT/TILE_SIZE)

MAX_ROOM_SIZE = 5
MIN_ROOM_SIZE = 3
ROOM_PADDING = 2

MAP_BORDER = 1

NUMBER_OF_ROOMS = 15

Map = []
Rooms = []

for x in range(TILE_ACROSS):
    row = []
    for i in range(TILE_DOWN):
        row.append(0)
    Map.append(row)

class Room():
    def __init__(self, width, height, pos_x, pos_y):
        self.width = width
        self.height = height
        self.pos_x = pos_x
        self.pos_y = pos_y

def generate_room():
    rm_width = MIN_ROOM_SIZE + secrets.randbelow(MAX_ROOM_SIZE - MIN_ROOM_SIZE + 1)
    rm_height = MIN_ROOM_SIZE + secrets.randbelow(MAX_ROOM_SIZE - MIN_ROOM_SIZE + 1)

    rm_pos_x = secrets.randbelow(TILE_ACROSS - rm_width - MAP_BORDER)
    if rm_pos_x < MAP_BORDER:
        rm_pos_x = MAP_BORDER
    rm_pos_y = secrets.randbelow(TILE_DOWN - rm_height - MAP_BORDER)
    if rm_pos_y < MAP_BORDER:
        rm_pos_y = MAP_BORDER

    return Room(rm_width, rm_height, rm_pos_x, rm_pos_y)

def generate_hall(rm_1, rm_2, direction):



for i in range(NUMBER_OF_ROOMS):
    intersect = True
    while intersect: 
        intersect = False
        rm = generate_room()
        for room in Rooms:
            padded_pos_x = rm.pos_x - 1
            padded_pos_y = rm.pos_y - 1
            padded_width = rm.width + 2
            padded_height = rm.height + 2
            rm_1 = Rect((room.pos_x*32, room.pos_y*32), (room.width*32, room.height*32))
            rm_2 = Rect((padded_pos_x*32, padded_pos_y*32), (padded_width*32, padded_height*32))
            if rm_1.colliderect(rm_2):
                intersect = True
    Rooms.append(rm)

for rm in Rooms:
    for i in range(rm.width):
            for j in range(rm.height):
                Map[rm.pos_x+i][rm.pos_y+j] = 1

def draw():
    for i in range(TILE_ACROSS):
        for j in range(TILE_DOWN):
            if Map[i][j] == 0:
                screen.blit(dirt_tile, (i*32, j*32))
            else:
                screen.blit(room_tile, (i*32, j*32))