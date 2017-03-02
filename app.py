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
PLAYER_RECENT_STATE = "DOWN"

P = {"x": 2, "y": 2}
box = {"x": 3, "y": 3}

BOXES = [box,
         {"x" : 1, "y" : 1},
         {"x" : 2, "y" : 4}
         ]
d = {"x": 4, "y": 4}
DOORS = [d,
         {"x" : 1, "y": 2},
         {"x" : 3, "y": 4}
         ]
WALLS = []
##COLOR                 R     G     B

BGCOLOR         =       (98,  140,  102)
PANELBGCOLOR    =       (158, 199,  162)
BLUE            =       (0,     0,  255)
RED             =       (255,   0,  0  )
GREEN           =       (0,   255,  0  )

## import needed framework and modules
import pygame, time, sys
pygame.init()

##GAME PRELOAD
image = {
    "player": {
        "DOWN"  : pygame.image.load("./images/playerdown.png"),
        "UP"    : pygame.image.load("./images/playerup.png"),
        "LEFT"  : pygame.image.load("./images/playerleft.png"),
        "RIGHT" : pygame.image.load("./images/playerright.png")
    },
    "wall"  : pygame.image.load("./images/wall.png"),
    "box"   : pygame.image.load("./images/box.png"),
    "door"  : pygame.image.load("./images/door.png")
}
pygame.mixer.music.load("./music/backgroundmusic.wav")
pygame.mixer.music.play(-1, 0.0)

gameFont = pygame.font.SysFont("arial.ttf", 30)

textSurf = {
    "WIN"   :   gameFont.render("CONGRATULATION !", True, RED),
    "LOSE"  :   gameFont.render("GOOD LUCK NEXT TIME :)", True, GREEN)
}

SCREEN_SURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("SOKOBAN")

GAME = True
walls = []

def fill_gameBound():
    for y in range(WORLDBOUND_HEIGHT):
        if y == 0 or y == WORLDBOUND_HEIGHT - 1:
            step = 1
        else:
            step = WORLDBOUND_HEIGHT - 1
        for x in range(0, WORLDBOUND_WIDTH, step):
            WALLS.append({"x": x - 1,
                          "y": y - 1})

def drawMap():
    ## vẽ bao quanh map
    for y in range(WORLDBOUND_HEIGHT):
        if (y == 0) or (y == WORLDBOUND_HEIGHT - 1) :
            step = 1
        else:
            step = WORLDBOUND_WIDTH - 1

        for x in range(0, WORLDBOUND_WIDTH, step):
            SCREEN_SURF.blit(image["wall"],(PADDLE + x * SPRITE_SIZE, PADDLE + y * SPRITE_SIZE))

    ## add door
    for door in DOORS:
        SCREEN_SURF.blit(image["door"], (PADDLE + DOOR_PADDLE + (door["x"] + 1) * SPRITE_SIZE,
                                         PADDLE + DOOR_PADDLE + (door["y"] + 1) * SPRITE_SIZE))

    ## add người chơi

    SCREEN_SURF.blit(image["player"][PLAYER_RECENT_STATE], (PLAYER_PADDLE + PADDLE + (P["x"] + 1) * SPRITE_SIZE,
                                       PADDLE + (P["y"] + 1) * SPRITE_SIZE))

    ## add box
    for box in BOXES:
        SCREEN_SURF.blit(image["box"], (PADDLE + (box["x"] + 1) * SPRITE_SIZE,
                                        PADDLE + (box["y"] + 1) * SPRITE_SIZE))


## Main Process

def game_update(dx, dy):
    if collide(P, WALLS, dx, dy) is None:

        if collide(P, BOXES, dx, dy) is not None:
            box = collide(P, BOXES, dx, dy)
            if collide(box, WALLS, dx, dy) is None:
                P["x"], P["y"] = move(P, dx, dy)
                box["x"], box["y"] = move(box, dx, dy)
        else:
            P["x"], P["y"] = move(P, dx, dy)

def move(object, dx, dy):
    return object["x"] + dx, object["y"] + dy

def collide(object, others, dx, dy):

    for anotherObject in others:
        if anotherObject["x"] == object["x"] + dx and anotherObject["y"] == object["y"] + dy:
            return anotherObject
    return None

def overlap(object, anotherObject):
    if object["x"] == anotherObject["x"] and object["y"] == anotherObject["y"] :
        return True
    return False

fill_gameBound()

def gameovercheck():
    global GAME, PLAYER_RECENT_STATE
    doorsLeft = len(DOORS)

    for box in BOXES:
        for door in DOORS:
            if overlap(box, door) :
                doorsLeft -= 1

    if doorsLeft == 0:
        SCREEN_SURF.blit(textSurf["WIN"], (700, 200))
        PLAYER_RECENT_STATE = "DOWN"
        GAME = DONE

while True :
    dx = 0
    dy = 0
    for event in pygame.event.get():
        ## trường hợp người chơi chán quá muốn quit
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        ## trường hợp người chơi di chuyển nhân vật
        if GAME is not DONE:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    # P["x"] -= 1
                    dx -= 1
                    PLAYER_RECENT_STATE = "LEFT"
                if event.key == pygame.K_RIGHT:
                    # P["x"] += 1
                    dx += 1
                    PLAYER_RECENT_STATE = "RIGHT"

                if event.key == pygame.K_UP:
                    # P["y"] -= 1
                    dy -= 1
                    PLAYER_RECENT_STATE = "UP"

                if event.key == pygame.K_DOWN:
                    # P["y"] += 1
                    dy += 1
                    PLAYER_RECENT_STATE = "DOWN"

    game_update(dx, dy)
    SCREEN_SURF.fill(BGCOLOR)
    pygame.draw.rect(SCREEN_SURF, PANELBGCOLOR, (50, 50, WORLDBOUND_WIDTH * SPRITE_SIZE, WORLDBOUND_HEIGHT * SPRITE_SIZE))
    drawMap()
    gameovercheck()
    pygame.display.update()












