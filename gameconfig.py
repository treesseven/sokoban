
SCREEN_WIDTH = 16
SCREEN_HEIGHT = 8

UNIT_PIXEL = 64

SPRITE_SIZE = 64

DOOR_PADDLE = 16
PLAYER_PADDLE = 13

PLAYER_RECENT_STATE = "DOWN"

#GAME LEVEL
GAME_LEVEL = 13


##COLOR                 R     G     B

BGCOLOR         =       (98,  140,  102)
PANELBGCOLOR    =       (158, 199,  162)
BLUE            =       (0,     0,  255)
RED             =       (255,   0,  0  )
GREEN           =       (0,   255,  0  )
BLACK           =       (255, 255,  255)

##sound and images

import pygame
pygame.init()
image = {
    "player": {
        "DOWN"  : pygame.image.load("./images/playerdown.png"),
        "UP"    : pygame.image.load("./images/playerup.png"),
        "LEFT"  : pygame.image.load("./images/playerleft.png"),
        "RIGHT" : pygame.image.load("./images/playerright.png")
    },
    "box"   : {
        "norm"      : pygame.image.load("./images/box.png"),
        "overlapped": pygame.image.load("./images/boxoverlapped.png")
    },
    "wall"  : pygame.image.load("./images/wall.png"),
    "door"  : pygame.image.load("./images/door.png"),
    "loading_screen" : pygame.image.load("./images/loading_screen.png")
}

sound_effect = {
    "box_deny" : pygame.mixer.Sound("./music/hitwall1.wav"),
    "box_in_door" : pygame.mixer.Sound("./music/boxindoor.wav"),
    "box_hit_box" : pygame.mixer.Sound("./music/hitbox.wav"),
    "win"       : pygame.mixer.Sound("./music/win.wav")
}

gameFont = pygame.font.SysFont("arial.ttf", 30)

textSurf = {
    "win"           :   gameFont.render("CONGRATULATION !"      , True, RED),
    "lose"          :   gameFont.render("GOOD LUCK NEXT TIME :)", True, GREEN),
    "loading_screen":   gameFont.render("PRESS SPACE TO START"  , True,  )
}
