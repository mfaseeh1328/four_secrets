import pygame, math, time

from settings import *
from main_game_assets import *

pygame.init()

class PowerUp():
    def __init__(self):
        self.power_up_index = 0
        self.power_up = power_up
        self.index = 0
        self.appear = False
        self.rect = pygame.Rect(WIDTH // 2, 0, self.power_up[0].get_width(), self.power_up[0].get_height())
        self.msg_list = ["2x Speed!", "Shield(X)!", "Resizing Ability (R)!", "Full Health, Congrats!"]
        self.colors = ["yellow", "lime", "cyan", "maroon"]
        self.collided = False

    def draw(self):
        self.rect.y = math.sin(time.time()) * 15 + 350
        if self.appear == True:

            def animate():
                self.index += 1
                if self.index >= 20:
                    self.index = 0
            animate()
            WIN.blit(self.power_up[self.index // 4], self.rect)

    def collide(self, player_rect):
        if player_rect.colliderect(self.rect):
            return True
        
    def draw_msg(self):
        font = pygame.font.Font("font/Font.otf", 40)
        msg = font.render(f"You Got {self.msg_list[self.power_up_index]}", 1, self.colors[self.power_up_index])

        WIN.blit(msg, (WIDTH // 2 - 150, math.tan(time.time()) * 25 + 300))