import secrets
import math
import random

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

HALL_DIRECTIONS = ['N', 'S', 'E', 'W']

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
        self.connections = random.sample(HALL_DIRECTIONS, random.randint(1, 4))

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

def find_path(start, destination, direction):
    first_spot = [0, 0]
    if direction[0] > 0 or direction[0] < 0:
        first_spot[1] = start.pos_y + secrets.randbelow(rm.height)
    elif direction[0] == 0 and direction[1] > 0:
        first_spot[1] = start.pos_y + start.height + 1
    elif direction[0] == 0 and direction[1] < 0:
        first_spot[1] = start.pos_y - 1
    
    if direction[1] > 0 or direction[0] < 0:
        first_spot[0] = start.pos_x + secrets.randbelow(rm.width)
    elif direction[0] > 0:
        first_spot[0] = start.pos_y + start.width + 1
    elif direction[0] < 0:
        first_spot[0] = start.pos_x - 1
    
    print(first_spot)
    
    Map[first_spot[0]][first_spot[1]] = 2
    

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
    for conn in rm.connections:
        connector = None
        conn_value = math.inf
        for other in Rooms:
            if other != rm:
                option = None
                if conn == 'N' and 'S' in other.connections and other.pos_y < rm.pos_y:
                    option = other
                    direction = [0, -1]
                elif conn == 'S' and 'N' in other.connections and other.pos_y > rm.pos_y:
                    option = other
                    direction = [0, 1]
                elif conn == 'E' and 'W' in other.connections and other.pos_x > rm.pos_x:
                    option = other
                    direction = [1, 0]
                elif conn == 'W' and 'E' in other.connections and other.pos_x < rm.pos_x:
                    option = other
                    direction = [-1, 0]
                if option == None: 
                    break
                diff = [option.pos_x - rm.pos_x, option.pos_y - rm.pos_y]
                magnitude = math.sqrt(diff[0]**2 + diff[1]**2)
                if magnitude < conn_value:
                    connector = option
                    conn_value = magnitude
        if connector == None:
                break
        else:
            find_path(rm, connector, direction)


        
        






def draw():
    for i in range(TILE_ACROSS):
        for j in range(TILE_DOWN):
            if Map[i][j] == 0:
                screen.blit(dirt_tile, (i*32, j*32))
            else:
                screen.blit(room_tile, (i*32, j*32))