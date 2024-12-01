import pygame, math, time, random

from settings import *
from main_game_assets import *

pygame.init()

class Boss():
    def __init__(self, base_img, x, y, current_health, explosion_img, border_color, bar_color, vel, stop_vel, laser_vel, laser_stop_vel, stop_cooldown, laser_img):
        self.base_img = base_img
        self.x, self.y = x, y
        self.rect = pygame.Rect(self.x, self.y, self.base_img.get_width() - 90, self.base_img.get_height())
        self.vel, self.stop_vel = vel, stop_vel
        self.move_dir = "left"
        self.index = 0
        self.explosion_img = explosion_img
        self.is_dead = False
        self.explode_counter, self.death_counter = 0, 0
        
        # defining lasers
        self.laser_img = laser_img
        self.img = random.choice(self.laser_img)
        self.laser_store = []
        self.laser_counter, self.laser_cooldown, self.stop_cooldown = 0, 200, stop_cooldown
        self.is_fire = True
        self.laser_vel, self.laser_stop_vel = laser_vel, laser_stop_vel

        # defining health bar
        self.current_health = current_health
        self.health_bar_width = current_health
        self.damage = 1
        self.laser_hit = False
        self.effect_index = 0
        self.explosion_effect = []
        self.bar_color, self.border_color = bar_color, border_color

    def explosion_timer(self):    
        if self.laser_hit == True:
            self.effect_index += 1

            if self.effect_index >= 22:
                self.laser_hit = False
                self.effect_index = 0

    def draw_health_bar(self):
        offset_x, offset_y = 60, 80
        pygame.draw.rect(WIN, (50, 50, 50), (self.rect.x+offset_x, self.rect.y+offset_y, self.health_bar_width, 10))
        pygame.draw.rect(WIN, (self.bar_color), (self.rect.x+offset_x, self.rect.y+offset_y, self.current_health, 10))
        pygame.draw.rect(WIN, (self.border_color), (self.rect.x+offset_x, self.rect.y+offset_y, self.health_bar_width, 10), 2)

    def draw_laser(self):
        if self.is_fire:
            self.laser_counter += 1

            if self.laser_counter >= self.laser_cooldown:
                rect = pygame.Rect(self.rect.x+50, self.rect.y+50, self.img.get_width(), self.img.get_height())
                self.laser_store.append(rect)
                self.laser_counter = 0
                boss_laser.play()

        for laser in self.laser_store:
            laser.y += self.laser_vel
            if laser.y >= HEIGHT+200:
                self.laser_store.remove(laser)
                self.img = random.choice(self.laser_img)
            WIN.blit(self.img, (laser.x, laser.y))
  
    def move(self):
        def right():
            self.rect.x += self.vel  
        def left():
            self.rect.x -= self.vel
        def left_change():
            return self.rect.x <= 0 - 45
        def right_change():
            return self.rect.x >= WIDTH - self.rect.width - 45
        if self.move_dir == "left":
            left()
        if self.move_dir == "right":
            right()

        if left_change():
            self.move_dir = "right"
            self.vel += 1
            self.laser_vel += 5
            self.laser_cooldown -= 20
        if right_change():
            self.move_dir = "left"
            self.vel += 1
            self.laser_vel += 5
            self.laser_cooldown -= 20

        if self.vel >= self.stop_vel:
            self.vel = self.stop_vel
        if self.laser_vel >= self.laser_stop_vel:
            self.laser_vel = self.laser_stop_vel
        if self.laser_cooldown <= 50:
            self.laser_cooldown = 50

    def draw(self):

        def animate():
            if self.is_dead == True:
                self.index += 1
                if self.index >= 44:
                    self.index = 43
        animate()

        if self.current_health > 0 and self.is_dead == False:
            WIN.blit(pygame.transform.rotozoom(self.base_img, math.sin(time.time()) * 5, 1), (self.rect.x, self.rect.y))
        else:
            WIN.blit(self.explosion_img[self.index // 4], (self.rect.x, self.rect.y))
            if self.index >= 43:
                self.rect.x, self.rect.y = -500, -500
            
    def update(self):
        self.draw()
        self.draw_health_bar()
        self.explosion_timer()