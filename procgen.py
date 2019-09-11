import secrets
import math

WIDTH = 1000
HEIGHT = 700

ROOM_COLOUR = (150, 150, 150)
MAX_ROOM_SIZE = 200
MIN_ROOM_SIZE = 75
ROOM_PADDING = 50

MAP_BORDER = 75

NUMBER_OF_ROOMS = 7

CORRIDOR_WIDTH = 50

class Room():
    def __init__(self, width, height, pos_x, pos_y):
        self.image = Rect((pos_x, pos_y), (width, height))
        self.NORTH = None
        self.SOUTH = None
        self.EAST = None
        self.WEST = None
        self.connections = 0

def generate_room():
    rm_width = MIN_ROOM_SIZE + secrets.randbelow(MAX_ROOM_SIZE - MIN_ROOM_SIZE + 1)
    rm_height = MIN_ROOM_SIZE + secrets.randbelow(MAX_ROOM_SIZE - MIN_ROOM_SIZE + 1)

    rm_pos_x = secrets.randbelow(WIDTH - rm_width - MAP_BORDER)
    rm_pos_y = secrets.randbelow(HEIGHT - rm_height - MAP_BORDER)

    return Room(rm_width, rm_height, rm_pos_x, rm_pos_y)

Map = []
for i in range(NUMBER_OF_ROOMS):

    intersect = True
    while intersect:
        rm = generate_room()
        intersect = False
        pos = len(Map) - 1
        while (not intersect) and pos >= 0:
            padded_width = rm.image.width + ROOM_PADDING
            padded_height = rm.image.height + ROOM_PADDING
            padded_room = Rect((rm.image.x, rm.image.y), (padded_width, padded_height))
            padded_room.center = rm.image.center
            if(Map[pos].image.colliderect(padded_room)):
                intersect = True
            pos -= 1

    Map.append(rm)

for rm in Map:
    options = ['N', 'S', 'E', 'W']
    connections = secrets.randbelow(5)
    count = 0
    if rm.NORTH != None:
        count += 1
        options.remove('N')
    if rm.SOUTH != None:
        count += 1
        options.remove('S')  
    if rm.EAST != None:
        count += 1
        options.remove('E')
    if rm.WEST != None:
        count += 1
        options.remove('W')

    connections -= count

    if connections > 0:
        dir = secrets.choice(options)
        if dir = 'N':
            


def draw():
    screen.fill((0, 0, 0))
    for rm in Map:
        screen.draw.filled_rect(rm.image, ROOM_COLOUR)