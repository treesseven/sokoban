import pygame

pygame.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Hello world")
done = False

player_sprite = pygame.image.load("character.png")
# RGB
# min = 0
# max = 255

BACK_GROUND = (98, 140, 102)
PANEL_BACKGROUND = (158, 199, 162 )
BLUE = (0, 0, 255)

screen_x = 10
screen_y = 10
screen_width = 400 - 10
screen_height = 300 - 10
player_x = 0
player_y = 0

def getdir(key):
    if key == pygame.K_RIGHT:
        player_x += 30


while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            step_x, step_y = getdir(event.type)




    screen.fill(BACK_GROUND)
    pygame.draw.rect(screen, PANEL_BACKGROUND, (screen_x, screen_y, screen_width, screen_height))

    screen.blit(player_sprite, (player_x, player_x))
     # pygame.draw.rect(screen, BLUE, (10, 10, 30, 50))
    pygame.display.flip()
