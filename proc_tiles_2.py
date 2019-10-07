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
        self.connections = {"NORTH": None, "SOUTH": None, "EAST": None, "WEST": None}

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

def check_path_finished(destination, current_spot):
    result = False
    if current_spot[0] < destination.pos_x or current_spot[0] > destination.pos_x + destination.width - 1:
        result = True
    if current_spot[1] < destination.pos_y or current_spot[1] > destination.pos_y + destination.height - 1:
        result = True
    return result
    

def find_path(start, destination, direction):


    print("Path Finished")


for i in range(NUMBER_OF_ROOMS):
    intersect = True
    while intersect: 
        intersect = False
        rm = generate_room()
        for room in Rooms:
            padded_pos_x = rm.pos_x - 1
            padded_pos_y = rm.pos_y - 1
            padded_width = rm.width + 3
            padded_height = rm.height + 3
            rm_1 = Rect((room.pos_x*32, room.pos_y*32), (room.width*32, room.height*32))
            rm_2 = Rect((padded_pos_x*32, padded_pos_y*32), (padded_width*32, padded_height*32))
            if rm_1.colliderect(rm_2):
                intersect = True
    Rooms.append(rm)
    for i in range(rm.width):
        for j in range(rm.height):
            Map[rm.pos_x+i][rm.pos_y+j] = 1

for rm in Rooms:
    candidates = {"NORTH": None, "SOUTH": None, "EAST": None, "WEST": None}
    print(rm.connections)
    for other in Rooms:
        if other != rm:
            left_marker = max(rm.pos_x, other.pos_x)
            right_marker = min(rm.pos_x + rm.width, other.pos_x + other.width)
            horizontal_overlap = list(range(left_marker, right_marker))
            if len(horizontal_overlap) > 0:
                print("Overlap Found")
                if rm.y > other.y and other.connections["SOUTH"] == None and rm.connections["NORTH"] != 0:
                    connector = candidates["NORTH"]
                    if connector == None:
                        candidates["NORTH"] = (other, horizontal_overlap)
                        other.connections["SOUTH"] = 0
                    else:
                        if other.pos_y + other.height > connector[0].pos_y + connector[0].height:
                            connector[0].connections["SOUTH"] = None
                            candidates["NORTH"] = (other, horizontal_overlap)
                            other.connections["SOUTH"] = 0
                if rm.y < other.y and other.connections["NORTH"] == None and rm.connections["SOUTH"] != 0:
                    connector = candidates["SOUTH"]
                    if connector == None:
                        candidates["SOUTH"] = (other, horizontal_overlap)
                        other.connections["NORTH"] = 0
                    else:
                        if other.pos_y < connector[0].pos_y:
                            connector[0].connections["NORTH"] = None
                            candidates["SOUTH"] = (other, horizontal_overlap)
                            other.connections["NORTH"] = 0
            top_marker = max(rm.pos_y, other.pos_y)
            bottom_marker = min(rm.pos_y + rm.height, other.pos_y + other.height)
            vertical_overlap = list(range(top_marker, bottom_marker))
            if len(vertical_overlap) > 0:
                print("Overlap Found")
                if rm.x > other.x and other.connections["EAST"] == None and rm.connections["WEST"] != 0:
                    connector = candidates["WEST"]
                    if connector == None:
                        candidates["WEST"] = (other, vertical_overlap)
                        other.connections["EAST"] = 0
                    else:
                        if other.pos_x < connector[0].pos_x:
                            connector[0].connections["EAST"] = None
                            candidates["WEST"] = (other, vertical_overlap)
                            other.connections["EAST"] = 0
                if rm.x < other.x and other.connections["WEST"] == None and rm.connections["EAST"] != 0:
                    connector = candidates["EAST"]
                    if connector == None:
                        candidates["EAST"] = (other, vertical_overlap)
                        other.connections["WEST"] = 0
                    else:
                        if other.pos_x + other.width < connector[0].pos_x + connector[0].width:
                            connector[0].connections["WEST"] = None
                            candidates["EAST"] = (other, vertical_overlap)
                            other.connections["WEST"] = 0
        print(candidates)
        #Create the corridors on the map array
        for key, value in candidates.items():
            if value is not None and value is not 0:
                dir = [0, 0]
                start_pos = [rm.pos_x, rm.pos_y]
                end_pos = [value[0].pos_x, value[0].pos_y]
                mid_overlap = value[1][len(value[1])//2]
                if key == "NORTH":
                    dir[1] = -1
                    start_pos[0] = mid_overlap
                    start_pos[1] -= 1
                    end_pos[0] = mid_overlap
                    end_pos[1] += other.height
                elif key == "SOUTH":
                    dir[1] = 1
                    start_pos[0] = mid_overlap
                    start_pos[1] += rm.height
                    end_pos[0] = mid_overlap
                    end_pos[1] -= 1
                elif key == "EAST":
                    dir[0] = 1
                    start_pos[0] += rm.width
                    start_pos[1] = mid_overlap
                    end_pos[0] -= 1
                    end_pos[1] = mid_overlap
                elif key == "WEST":
                    dir[0] = -1
                    start_pos[0] -= 1
                    start_pos[1] = mid_overlap
                    end_pos[0] += other.width
                    end_pos[1] = mid_overlap
                print(key)
                print(start_pos)
                print(end_pos)
                print(dir)
                Map[start_pos[0]][start_pos[1]] = 2
                Map[end_pos[0]][end_pos[1]] = 2 
                distance = (start_pos[0] - end_pos[0]) + (start_pos[1] - end_pos[1])
                print(distance)
                next_pos = start_pos
                for i in range(abs(distance)):
                    next_pos = [next_pos[0] + dir[0], next_pos[1] + dir[1]]
                    print(next_pos)
                    Map[next_pos[0]][next_pos[1]] = 2 
                    

                
                


            


def draw():
    for i in range(TILE_ACROSS):
        for j in range(TILE_DOWN):
            if Map[i][j] == 0:
                screen.blit(dirt_tile, (i*32, j*32))
            else:
                screen.blit(room_tile, (i*32, j*32))