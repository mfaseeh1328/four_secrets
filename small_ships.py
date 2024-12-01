import pygame
import random
import math, time

from settings import *
from main_game_assets import *

pygame.init()
  

class Ships():
    def __init__(self):
        self.random_enemy = []
        self.max_ships = 6
        self.ship_x = 250
        self.rows, self.cols = 3, 6
        self.elapsed_time = 0

        self.rand_pos = []
        for i in range(10):
            rand_x = random.randint(100, 800)
            rand_y = random.randint(100, 400)
            self.rand_pos.append([rand_x, rand_y])

        # generating random enemies
        for i in range(self.rows):
            for j in range(self.cols):
                rand = random.choice(small_ships)
                self.random_enemy.append(rand)

        self.ship_rect = []

    # stage 1
    def tan_move(self):
        for i in range(self.rows):
            for j in range(self.cols):
                x = math.tan(time.time()) * 25 + j * 100 + self.ship_x
                y = i * 100 + 100
                w,h = self.random_enemy[i].get_width(), self.random_enemy[i].get_height()               
                WIN.blit(self.random_enemy[j], (x, y))                
                rect = pygame.Rect(x, y, w, h)
                self.ship_rect.append(rect)
    # stage 2
    def elastic_move(self):
        for i in range(self.rows):
            for j in range(self.cols):
                x = math.sin(time.time()) * (j*150) + j * 100 + self.ship_x
                y = math.cos(time.time()) * (i*100) + i * 100 + 100
                WIN.blit(self.random_enemy[j], (x, y))
    # stage 3
    def random_move(self):
        self.elapsed_time += 1
        for i in range(10):
            if self.elapsed_time >= 90:
                self.rand_pos[i][0] = random.randint(100, 800)
                self.rand_pos[i][1] = random.randint(100, 400)

            WIN.blit(self.random_enemy[i], (self.rand_pos[i][0] - (i*10), self.rand_pos[i][1] - (i*10)))
        if self.elapsed_time >= 100:
            self.elapsed_time = 0
    # stage 4
    def vibrate_move(self):
        for i in range(8):
            for j in range(3):
                x = math.cos(time.time())*(i*70) + j * 50 + 450
                y = math.sin(time.time())*(j*15) + i * 50 + 50
                WIN.blit(self.random_enemy[i], (x, y))
    
    def update(self):
        self.tan_move()
