import pygame

from settings import *
from main_game_assets import *

pygame.init()

class Help():
    def __init__(self):
        self.running = True

    def run(self):
        while self.running:

            WIN.fill(("black"))
            WIN.blit(help_bg, (0, 0))
            WIN.blit(help_fg, (0, 0))

            pygame.display.update()
            CLOCK.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False 
