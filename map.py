from door import Door
from player import Player
from box import Box
from wall import Wall
from ground import Ground
from gameconfig import *
import pygame, sys, time

##GAME PRELOAD

rep = {
    "player": "@",
    "door"  : ".",
    "wall"  : "#",
    "box"   : "$",
    "ground": " "
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
            if line[x] == rep["ground"] : self.grounds.append(Ground(x = x, y = y))

    def move(self, object, dx, dy):
        object.move(self.current_dx, self.current_dy)

    def load(self):
        self.doors = []
        self.boxes = []
        self.walls = []
        self.grounds = []
        data_file = self.get_data_file()
        with open ("./maps/"+ data_file, "r") as myfile:
            y = -1
            max_width = 0
            for line in myfile:
                y += 1
                self.data_process(line, y)
                max_width = max(max_width, len(line) - 1)

        self.width = max_width
        self.height = y
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
        else:
            sound_effect["box_deny"].play()

    def get_actual_coords(self, x, y):
        return x * UNIT_PIXEL, y * UNIT_PIXEL

    def draw(self):

        for y in range(self.height):
            for x in range(self.width):
                self.screen_surf.blit(image["ground"], (x * UNIT_PIXEL, y * UNIT_PIXEL))

        for door in self.doors:
            self.screen_surf.blit(image["door"], (door.x * UNIT_PIXEL + DOOR_PADDLE, door.y * UNIT_PIXEL + DOOR_PADDLE))

        self.screen_surf.blit(image["player"][self.player.state],
                              (self.player.x * UNIT_PIXEL + PLAYER_PADDLE, self.player.y * UNIT_PIXEL))

        for wall in self.walls:
            self.screen_surf.blit(image["wall"], (wall.x * UNIT_PIXEL, wall.y * UNIT_PIXEL))



        for box in self.boxes:
            state = "norm"
            if box.overlap(self.doors):
                state = "overlapped"
            self.screen_surf.blit(image["box"][state], (box.x * UNIT_PIXEL, box.y * UNIT_PIXEL))

    def music(self):
        pygame.mixer.music.load("./music/loading_music.mp3")
        pygame.mixer.music.play(-1, 0.0)

    def play_sound(self, sound):
        sound_effect[sound].play()

    def stop_music(self):
        pygame.mixer.music.stop()

    def check_win(self):
        for box in self.boxes:
            if not box.overlap(self.doors):
                return False
        self.GAME = False
        return True

    def add_text(self, text, x, y):
        self.screen_surf.blit(textSurf[text], (x, y))

    def add_screen_text(self):
        self.add_text("next_level", 600, 350)
        self.add_text("back_level", 600, 400)
        self.add_text("reset_level", 600, 450)

    def play(self):
        self.load()
        sound_effect["win"].stop()
        print(self.player.x, self.player.y)
        self.GAME = True
        self.screen_surf = pygame.display.set_mode((SCREEN_WIDTH * UNIT_PIXEL, SCREEN_HEIGHT * UNIT_PIXEL))
        self.music()
        self.played_sound = False
        self.time = pygame.time.get_ticks()
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
                        pygame.time.wait(500)
                        return +1

                    if event.key == pygame.K_b:
                        ## Lui` man` truoc
                        pygame.time.wait(500)
                        return -1

                    if event.key == pygame.K_r:
                        ## Choi lai man
                        pygame.time.wait(200)
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
            self.screen_surf.fill(BGCOLOR)
            self.draw()
            self.update(dx, dy)
            self.add_screen_text()
            if self.check_win():
                if pygame.time.get_ticks() - self.time <= 400:
                    self.add_text("win", 600, 100)
                elif pygame.time.get_ticks() - self.time >= 800:
                    self.time = pygame.time.get_ticks()
                    print(self.time)

                self.player.state = "DOWN"
                if not self.played_sound:
                    self.stop_music()
                    self.play_sound("win")
                    self.played_sound = True
            pygame.display.update()

