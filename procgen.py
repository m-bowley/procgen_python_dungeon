import secrets
import math

WIDTH = 1000
HEIGHT = 700

ROOM_COLOUR = (150, 150, 150)
MAX_ROOM_SIZE = 150
MIN_ROOM_SIZE = 75
ROOM_PADDING = 50

MAP_BORDER = 40

NUMBER_OF_ROOMS = 8

CORRIDOR_WIDTH = 40

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
    if rm_pos_x < MAP_BORDER:
        rm_pos_x = MAP_BORDER
    rm_pos_y = secrets.randbelow(HEIGHT - rm_height - MAP_BORDER)
    if rm_pos_y < MAP_BORDER:
        rm_pos_y = MAP_BORDER

    return Room(rm_width, rm_height, rm_pos_x, rm_pos_y)

def generate_hall(rm_1, rm_2, direction):
    diff = [rm_2.image.center[0] - rm_1.image.center[0], rm_2.image.center[1] - rm_1.image.center[1]]

    up = True
    across = True

    if (abs(diff[0]) < (rm_1.image.width/2)) or abs(diff[0]) < (rm_2.image.width/2):
        across = False
    if (abs(diff[1]) < (rm_1.image.height/2)) or abs(diff[1]) < (rm_2.image.height/2):
        up = False
    hall_1_pos, hall_2_pos = None, None
    
    hall_2_pos = [rm_1.image.center[0], rm_1.image.center[1]]
    hall_1_pos = [rm_2.image.center[0], rm_2.image.center[1]]

    corridors = []

    if up:
        hall_1_pos[1] -= (diff[1]/2)
        if not across:
            hall_1_pos[0] -= (diff[0]/2)
        hall = Room(CORRIDOR_WIDTH, abs(diff[1])+CORRIDOR_WIDTH, hall_1_pos[0], hall_1_pos[1])
        hall.image.center = tuple(hall_1_pos)
        corridors.append(hall)
    if across:
        hall_2_pos[0] += (diff[0]/2)
        if not up:
            hall_2_pos[1] += (diff[1]/2)
        hall = Room(abs(diff[0])+CORRIDOR_WIDTH, CORRIDOR_WIDTH, hall_2_pos[0], hall_2_pos[1])
        hall.image.center = tuple(hall_2_pos)
        corridors.append(hall) 
    return corridors



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
    if connections < 1: 
        connections = 1 
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

    for slot in range(connections):
        dir = secrets.choice(options)
        connector = secrets.choice(Map)
        conn_value = 1000000000000000000
        if dir == 'N':
            for room in Map:
                if rm != room and room.image.y < rm.image.y:
                    diff = [rm.image.x - room.image.x, rm.image.y - room.image.y]
                    magnitude = math.sqrt(diff[0]**2 + diff[1]**2)
                    if magnitude < conn_value:
                        connector = room
                        conn_value = magnitude
        elif dir == 'S':
            for room in Map:
                if rm != room and room.image.y > rm.image.y:
                    diff = [rm.image.x - room.image.x, rm.image.y - room.image.y]
                    magnitude = math.sqrt(diff[0]**2 + diff[1]**2)
                    if magnitude < conn_value:
                        connector = room
                        conn_value = magnitude
        elif dir == 'E':
            for room in Map:
                if rm != room and room.image.x > rm.image.x:
                    diff = [rm.image.x - room.image.x, rm.image.y - room.image.y]
                    magnitude = math.sqrt(diff[0]**2 + diff[1]**2)
                    print(magnitude)
                    if magnitude < conn_value:
                        connector = room
                        conn_value = magnitude
        elif dir == 'E':
            for room in Map:
                if rm != room and room.image.x > rm.image.x:
                    diff = [rm.image.x - room.image.x, rm.image.y - room.image.y]
                    magnitude = math.sqrt(diff[0]**2 + diff[1]**2)
                    print(magnitude)
                    if magnitude < conn_value:
                        connector = room
                        conn_value = magnitude
        if dir == 'N':
            rm.NORTH = True
            rm.children.append(generate_hall(rm, connector, dir))
            options.remove('N')
            connector.SOUTH = True
        elif dir == 'S':
            rm.SOUTH = True
            rm.children.append(generate_hall(rm, connector, dir))
            options.remove('S')
            connector.NORTH = True
        elif dir == 'E':
            rm.EAST = True
            rm.children.append(generate_hall(rm, connector, dir))
            options.remove('E')
            connector.WEST = True
        elif dir == 'W':
            rm.WEST = True
            rm.children.append(generate_hall(rm, connector, dir))
            options.remove('W')
            connector.EAST = True
            


def draw():
    screen.fill((0, 0, 0))
    for rm in Map:
        screen.draw.filled_rect(rm.image, ROOM_COLOUR)
        for item in rm.children:
            for i in item:
                screen.draw.filled_rect(i.image, ROOM_COLOUR)