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

    def play_music(self):
        pygame.mixer.music.load("./music/backgroundmusic.wav")
        pygame.mixer.music.play(-1, 0.0)

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
        self.play_music()
        self.time = pygame.time.get_ticks()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pygame.time.delay(1000)
                        self.play()
            self.background = image["loading_screen"].convert()
            self.background = pygame.transform.scale(self.background, (SCREEN_WIDTH * UNIT_PIXEL, SCREEN_HEIGHT * UNIT_PIXEL))
            self.SCREEN_SURF.blit(self.background, (0, 0))

            if pygame.time.get_ticks() - self.time <= 500:
                self.SCREEN_SURF.blit(textSurf["loading_screen"], (380, 400))
            elif pygame.time.get_ticks() - self.time >= 1000:
                self.time = pygame.time.get_ticks()

            pygame.display.update()



SOKOBAN = Game("SOKOBAN")


## creat map
for i in range(SOKOBAN.max_level):
    SOKOBAN.maps.append(Map(level = i + 1))

SOKOBAN.game_loop()

