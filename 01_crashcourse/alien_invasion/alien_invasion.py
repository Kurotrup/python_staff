import  sys
import pygame
import os

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("AAliens envasion")
    bg_color =(230,230,230)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)
        pygame.display.flip()
x = 10
y = 35
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

run_game()
# page 234 creating Settings calass
