import pygame
import math
import time
from settings import *

pygame.init()

# loading button images
play_btn = [pygame.image.load("Assets/ui/play.png").convert_alpha(), pygame.image.load("Assets/ui/play_hover.png").convert_alpha()]
help_btn = [pygame.image.load("Assets/ui/help.png").convert_alpha(), pygame.image.load("Assets/ui/help_hover.png").convert_alpha()]
shop_btn = [pygame.image.load("Assets/ui/shop.png").convert_alpha(), pygame.image.load("Assets/ui/shop_hover.png").convert_alpha()]
exit_btn = [pygame.image.load("Assets/ui/exit.png").convert_alpha(), pygame.image.load("Assets/ui/exit_hover.png").convert_alpha()]

btn_width, btn_height = 400, 75

def display_button(button, x, y):
    WIN.blit(button[0], (x, y))

def hover_button(button, x, y):
    WIN.blit(button[1], (x, y))

def draw():
    display_button(play_btn, WIDTH // 2 - 200, HEIGHT // 2 - 200)
    display_button(help_btn, WIDTH // 2 - 200, HEIGHT // 2 - 75)
    display_button(shop_btn, WIDTH // 2 - 200, HEIGHT // 2 + 50)
    display_button(exit_btn, WIDTH // 2 - 200, HEIGHT // 2 + 175)

play_rect = pygame.Rect(WIDTH // 2 - 200, HEIGHT // 2 - 200, btn_width, btn_height)
help_rect = pygame.Rect(WIDTH // 2 - 200, HEIGHT // 2 - 75, btn_width, btn_height)
shop_rect = pygame.Rect(WIDTH // 2 - 200, HEIGHT // 2 + 50, btn_width, btn_height)
exit_rect = pygame.Rect(WIDTH // 2 - 200, HEIGHT // 2 + 175, btn_width, btn_height)