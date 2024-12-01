import pygame

from settings import *
from main_game_assets import *

pygame.init()

class Help():
    def __init__(self):
        self.running = True

    def run(self):
        while self.running:
            
            pygame.display.update()
            CLOCK.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False 


"""
if event.key == pygame.K_f:
    FULLSCREEN = True
    
    if FULLSCREEN == True:
        WIN = pygame.display.set_mode(MONITOR_SIZE, pygame.FULLSCREEN)

if event.key == pygame.K_u:
    FULLSCREEN = False
    WIN = pygame.display.set_mode((1100, 900))
"""