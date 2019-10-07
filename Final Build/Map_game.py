import Map_Creator_Stage3

WIDTH = Map_Creator_Stage3.WIDTH
HEIGHT = Map_Creator_Stage3.HEIGHT

room_tile = "sprite_00.png"
dirt_tile = "sprite_01.png"

Map = Map_Creator_Stage3.create_map()


def draw():
    for i in range(WIDTH//32):
        for j in range(HEIGHT//32):
            if Map[i][j] == 0:
                screen.blit(dirt_tile, (i*32, j*32))
            else:
                screen.blit(room_tile, (i*32, j*32))