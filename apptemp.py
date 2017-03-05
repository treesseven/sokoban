from map import Map
from gameconfig import *
import pygame, time, sys

class Game:
    def __init__(self, game_name):
        self.maps = []
        self.game_name = game_name
        self.max_level = GAME_LEVEL

        # Initialize pygame
        pygame.init()

        self.SCREEN_SURF = pygame.display.set_mode((SCREEN_WIDTH * UNIT_PIXEL, SCREEN_HEIGHT * UNIT_PIXEL))
        pygame.display.set_caption(game_name)
        gameFont = pygame.font.SysFont("arial.ttf", 30)

    def play(self):
        level = self.current_level
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            level += self.maps[level].play()
            self.current_level = level
            if level >= self.max_level or level < 0:
                level = 0

    def game_loop(self):
        self.current_level = 0

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.play()


            pygame.display.update()



SOKOBAN = Game("SOKOBAN")


## creat map
for i in range(SOKOBAN.max_level):
    SOKOBAN.maps.append(Map(level = i + 1))

SOKOBAN.game_loop()

