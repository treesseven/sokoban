## set GAME CONFIGS

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

SPRITE_WIDTH = 40
SPRITE_HEIGHT = 50

SPRITE_SIZE = 64

DONE = False
WORLDBOUND_WIDTH = 8
WORLDBOUND_HEIGHT = 8

DOOR_PADDLE = 16
PLAYER_PADDLE = 13
PADDLE = 50
GAMEBOUND_WIDTH = WORLDBOUND_WIDTH - 2
GAMEBOUND_HEIGHT = WORLDBOUND_HEIGHT - 2

P = {"x": 2, "y": 2}
b = {"x": 3, "y": 3}
d = {"x": 4, "y": 4}

##COLOR                 R     G     B

BGCOLOR =               (98,  140,  102)
PANEBGCOLOR =           (158, 199,  162)
BLUE =                  (0,     0,  255)

## import needed framework and modules
import pygame, time

##GAME PRELOAD
image = {
    "player": pygame.image.load("./images/player1.png"),
    "wall"  : pygame.image.load("./images/wall.png"),
    "box"   : pygame.image.load("./images/box.png"),
    "door"  : pygame.image.load("./images/door.png")

}

pygame.init()
SCREEN_SURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("SOKOBAN")
GAME = True
walls = []

def drawMap():
    ## vẽ bao quanh map
    for y in range(WORLDBOUND_HEIGHT):
        if (y == 0) or (y == WORLDBOUND_HEIGHT - 1) :
            step = 1
        else:
            step = WORLDBOUND_WIDTH - 1

        for x in range(0, WORLDBOUND_WIDTH, step):
            SCREEN_SURF.blit(image["wall"],(PADDLE + x * SPRITE_SIZE, PADDLE + y * SPRITE_SIZE))


    ## add người chơi

    SCREEN_SURF.blit(image["player"], (PLAYER_PADDLE + PADDLE + (P["x"] + 1) * SPRITE_SIZE,
                                       PADDLE + (P["y"] + 1) * SPRITE_SIZE))

    ## add door
    SCREEN_SURF.blit(image["door"], (PADDLE + DOOR_PADDLE + (d["x"] + 1)* SPRITE_SIZE,
                                     PADDLE + DOOR_PADDLE + (d["y"] + 1)* SPRITE_SIZE))

    ## add box
    SCREEN_SURF.blit(image["box"], (PADDLE + (b["x"] + 1) * SPRITE_SIZE,
                                    PADDLE + (b["y"] + 1) * SPRITE_SIZE))


while GAME is not DONE :
    for event in pygame.event.get():
        ## trường hợp người chơi chán quá muốn quit
        if event.type == pygame.QUIT:
            DONE = True

        ## trường hợp người chơi di chuyển nhân vật

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                P["x"] -= 1
            if event.key == pygame.K_RIGHT:
                P["x"] += 1
            if event.key == pygame.K_UP:
                P["y"] -= 1
            if event.key == pygame.K_DOWN:
                P["y"] += 1

    SCREEN_SURF.fill(BGCOLOR)
    pygame.draw.rect(SCREEN_SURF, PANEBGCOLOR, (50, 50, WORLDBOUND_WIDTH * SPRITE_SIZE, WORLDBOUND_HEIGHT * SPRITE_SIZE))
    drawMap()
    pygame.display.update()








