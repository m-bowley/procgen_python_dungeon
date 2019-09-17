import secrets
import math

WIDTH = 1000
HEIGHT = 700

ROOM_COLOUR = (150, 150, 150)
MAX_ROOM_SIZE = 200
MIN_ROOM_SIZE = 75
ROOM_PADDING = 50

MAP_BORDER = 75

NUMBER_OF_ROOMS = 2

CORRIDOR_WIDTH = 50

class Room():
    def __init__(self, width, height, pos_x, pos_y):
        self.image = Rect((pos_x, pos_y), (width, height))
        self.NORTH = None
        self.SOUTH = None
        self.EAST = None
        self.WEST = None
        self.children = []
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

rm_1 = Map[0]
rm_2 = Map[1]

diff = [rm_2.image.center[0] - rm_1.image.center[0], rm_2.image.center[1] - rm_1.image.center[1]]

print(rm_1.image.center)
print(rm_2.image.center)
print(diff)

up = True
across = True

if (abs(diff[0]) < (rm_1.image.width/2)) or abs(diff[0]) < (rm_2.image.width/2):
    across = False
if (abs(diff[1]) < (rm_1.image.height/2)) or abs(diff[1]) < (rm_2.image.height/2):
    up = False

if up:
    hall_pos = [rm_2.image.center[0], rm_2.image.center[1]]
    hall_pos[1] -= (diff[1]/2)
    if not across:
        hall_pos[0] -= (diff[0]/2)
    #hall_pos[0] -= CORRIDOR_WIDTH
    #hall_pos[1] -= abs(diff[1])
    hall = Room(CORRIDOR_WIDTH, abs(diff[1])+CORRIDOR_WIDTH, hall_pos[0], hall_pos[1])
    print(hall.image.x)
    print(hall.image.y)
    hall.image.center = tuple(hall_pos)
    print(hall.image.x)
    print(hall.image.y)
    Map.append(hall)
if across:
    hall_pos = [rm_1.image.center[0], rm_1.image.center[1]]
    hall_pos[0] += (diff[0]/2)
    if not up:
        hall_pos[1] += (diff[1]/2)
    #hall_pos[0] -= abs(diff[0])/2
    #hall_pos[1] -= CORRIDOR_WIDTH/2
    hall = Room(abs(diff[0])+CORRIDOR_WIDTH, CORRIDOR_WIDTH, hall_pos[0], hall_pos[1])
    print(hall.image.x)
    print(hall.image.y)
    hall.image.center = tuple(hall_pos)
    print(hall.image.x)
    print(hall.image.y)
    Map.append(hall)
    

print(up)
print(across)

def draw():
    screen.fill((0, 0, 0))
    for rm in Map:
        screen.draw.filled_rect(rm.image, ROOM_COLOUR)