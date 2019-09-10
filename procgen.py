import random

WIDTH = 1000
HEIGHT = 700

ROOM_COLOUR = (150, 150, 150)
MAX_ROOM_SIZE = 200
MIN_ROOM_SIZE = 75

NUMBER_OF_ROOMS = 10

class Room():
    def __init__(self, width, height, pos_x, pos_y):
        self.image = Rect((pos_x, pos_y), (width, height))

def generate_room():
    rm_width = MIN_ROOM_SIZE + random.randint(0, MAX_ROOM_SIZE - MIN_ROOM_SIZE + 1)
    rm_height = MIN_ROOM_SIZE + random.randint(0, MAX_ROOM_SIZE - MIN_ROOM_SIZE + 1)

    rm_pos_x = random.randint(0, WIDTH - rm_width)
    rm_pos_y = random.randint(0, HEIGHT - rm_height)

    return Room(rm_width, rm_height, rm_pos_x, rm_pos_y)

Map = []
for i in range(NUMBER_OF_ROOMS):

    intersect = True
    while intersect:
        rm = generate_room()
        intersect = False
        pos = len(Map) - 1
        while (not intersect) and pos >= 0:
            if(Map[pos].image.colliderect(rm.image)):
                intersect = True
            pos -= 1

    Map.append(rm)

def draw():
    screen.fill((0, 0, 0))
    for rm in Map:
        screen.draw.filled_rect(rm.image, ROOM_COLOUR)