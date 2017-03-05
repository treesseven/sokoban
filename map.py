from door import Door
from player import Player
from box import Box
from wall import Wall
from gameconfig import *
import pygame, sys, time

##GAME PRELOAD

rep = {
    "player": "@",
    "door"  : ".",
    "wall"  : "#",
    "box"   : "$"
}

DONE = False
pygame.init()

class Map:
    def __init__(self, level):
        self.level = level
        # dx, dy = direction x and y of game


    def get_data_file(self):
        data_file = str(self.level)
        while len(data_file) < 3:
            data_file = '0' + data_file
        data_file = "soko" + data_file + ".txt"
        return data_file

    def data_process(self, line, y):
        for x in range(len(line)):
            if line[x] == rep["player"] : self.player = Player(x = x, y = y)
            if line[x] == rep["door"]   : self.doors.append(Door(x = x, y = y))
            if line[x] == rep["box"]    : self.boxes.append(Box(x = x, y = y))
            if line[x] == rep["wall"]   : self.walls.append(Wall(x = x, y = y))

    def move(self, object, dx, dy):
        object.move(self.current_dx, self.current_dy)

    def load(self):
        self.doors = []
        self.boxes = []
        self.walls = []
        data_file = self.get_data_file()
        with open ("./maps/"+ data_file, "r") as myfile:
            y = -1
            max_width = 0
            for line in myfile:
                y += 1
                self.data_process(line, y)
                max_width = max(max_width, len(line))

        self.width = max_width
        self.height = y + 1
        self.loaded = True

    def update(self, dx, dy):
        self.player.dx = dx
        self.player.dy = dy
        if self.player.collide(self.walls) is None:
            box = self.player.collide(self.boxes)
            if box is not None:
                box.dx = dx
                box.dy = dy
                if box.collide(self.walls) is None and box.collide(self.boxes) is None:
                    box.move()
                    if box.overlap(self.doors):
                        box.overlapped = True
                        sound_effect["box_in_door"].play()
                    self.player.move()
                else:
                    sound_effect["box_deny"].play()
            else:
                self.player.move()

    def get_actual_coords(self, x, y):
        return x * UNIT_PIXEL, y * UNIT_PIXEL

    def draw(self):

        self.screen_surf.blit(image["player"][self.player.state],
                              (self.player.x * UNIT_PIXEL + PLAYER_PADDLE, self.player.y * UNIT_PIXEL))

        for wall in self.walls:
            self.screen_surf.blit(image["wall"], (wall.x * UNIT_PIXEL, wall.y * UNIT_PIXEL))

        for door in self.doors:
            self.screen_surf.blit(image["door"], (door.x * UNIT_PIXEL, door.y * UNIT_PIXEL))

        for box in self.boxes:
            state = "norm"
            if box.overlap(self.doors):
                state = "overlapped"
            self.screen_surf.blit(image["box"][state], (box.x * UNIT_PIXEL, box.y * UNIT_PIXEL))

    def music(self):
        pygame.mixer.music.load("./music/backgroundmusic.wav")
        pygame.mixer.music.play(-1, 0.0)

    def add_text(self):
        pass

    def play(self):
        self.load()
        print(self.player.x, self.player.y)
        self.GAME = True
        self.screen_surf = pygame.display.set_mode((SCREEN_WIDTH * UNIT_PIXEL, SCREEN_HEIGHT * UNIT_PIXEL))
        # self.music()
        while True:
            dx = 0
            dy = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT or \
                ( event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_n:
                        ## Chuyen man tiep theo
                        return +1

                    if event.key == pygame.K_b:
                        ## Lui` man` truoc
                        return -1

                    if event.key == pygame.K_r:
                        ## Choi lai man
                        return 0

                    ####################################################
                    if self.GAME is not DONE:

                        if event.key == pygame.K_LEFT:
                            dx -= 1
                            self.player.state = "LEFT"

                        if event.key == pygame.K_RIGHT:
                            dx += 1
                            self.player.state = "RIGHT"

                        if event.key == pygame.K_UP:
                            dy -= 1
                            self.player.state = "UP"

                        if event.key == pygame.K_DOWN:
                            dy += 1
                            self.player.state = "DOWN"

            self.update(dx, dy)
            self.screen_surf.fill(BGCOLOR)
            self.draw()
            self.add_text()
            pygame.display.update()

