import pygame
import math, time
import random

from main_game_assets import *
from settings import *

pygame.init()

class Player():
    def __init__(self, current_select):
        self.current_player = player_ships[current_select]
        self.width, self.height = self.current_player.get_width(), self.current_player.get_height()
        self.rect = pygame.Rect(WIDTH // 2 - (self.width//2), HEIGHT - self.height - 50, self.width, self.height)
        self.vel = 5
        self.engine_index = 0
        self.explosion_offset = []
        self.total_score = 0
        self.score_y = 35
        self.attempts, self.attempt_index = 0, 0
        self.major_explosion_index = 0

        # laser
        self.laser_index = 0
        self.laser_menu = False
        self.laser_cooldown = 10
        self.laser_counter = 0
        self.laser_store = []
        self.fire_laser = False
        self.laser_vel = 15
        self.laser_x = [150, 300, 450, 600, 750]
        self.laser_y = [HEIGHT // 2, HEIGHT // 2, HEIGHT // 2, HEIGHT // 2, HEIGHT // 2]
        self.select_counter = 0
        self.rand_color = "white"

        # shield
        self.is_shield = False
        self.shield_img_index = 0
        self.shield_cooldown = 200
        self.shield_counter = 0
        self.cooldown_counter = 200
        self.shield_pos_y = HEIGHT - 180
        self.no_shield = True

    def draw_explosion(self):
        self.major_explosion_index += 1
        if self.major_explosion_index >= 210:
            self.major_explosion_index = 209

        WIN.blit(major_explosion[self.major_explosion_index // 15], (self.rect.x, self.rect.y))

    def draw_shield(self):
        keys = pygame.key.get_pressed()
        rect = pygame.Rect(self.rect.x - 10, self.rect.y - 10, player_shield[0].get_width(), player_shield[0].get_height())

        if keys[pygame.K_x]:
            self.is_shield = True

        if self.is_shield == True:
            self.shield_counter += 1

            if self.shield_counter >= self.shield_cooldown:
                self.cooldown_counter -= 1

                if self.cooldown_counter <= 0:
                    self.is_shield = False
                    self.shield_counter = 0
                    self.cooldown_counter = 200
        if self.is_shield == True and self.cooldown_counter >= 200:
            try:
                def animate():
                    self.shield_img_index += 1
                    if self.shield_img_index >= 64:
                        self.shield_img_index = 0   
            except Exception as error:
                raise error
            
            animate()

            WIN.blit(player_shield[self.shield_img_index // 8], rect)

            pygame.draw.rect(WIN, (50, 50, 50), (self.rect.x, self.rect.y - 15, 200, 10))
            pygame.draw.rect(WIN, ("maroon"), (self.rect.x, self.rect.y-15, self.shield_counter, 10))
            pygame.draw.rect(WIN, ("purple"), (self.rect.x, self.rect.y-15, 200, 10), 3)

        if self.cooldown_counter >= 200:
            WIN.blit(pygame.transform.scale(player_shield[self.shield_img_index // 8], (90, 90)), (10, self.shield_pos_y))

    def draw(self):
        def animate_engine():
            self.engine_index += 1
            if self.engine_index >= 48:
                self.engine_index = 0

        animate_engine()
        WIN.blit(engine_vfx[self.engine_index // 6], (self.rect.x+(self.rect.width // 2) - 10, self.rect.y+self.height-2))
        WIN.blit(pygame.transform.scale(self.current_player, (self.rect.width, self.rect.height)), (self.rect.x, self.rect.y))

    def move(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_UP] and self.rect.y >= HEIGHT // 3:
            self.rect.y -= self.vel

        if keys_pressed[pygame.K_DOWN] and self.rect.y <= self.shield_pos_y:
            self.rect.y += self.vel

        if keys_pressed[pygame.K_LEFT] and self.rect.x >= 0:
            self.rect.x -= self.vel

        if keys_pressed[pygame.K_RIGHT] and self.rect.x <= WIDTH - self.width - 5:
            self.rect.x += self.vel

    def draw_laser_menu(self):

        self.select_counter += 1

        if self.select_counter >= 20:
            self.rand_color = random.choice(["red", "green", "lime", "cyan", "blue", "gold", "yellow", "pink", "purple"])
            self.select_counter = 0

        font = pygame.font.Font("Font/font.otf", 40)
        pause = font.render("Game Paused!", 1, "yellow")
        WIN.blit(pause, (math.sin(time.time()) * 15 + 30, math.cos(time.time()) * 15 + 20))

        menu_surf = pygame.Surface((900, 700))
        menu_surf.fill(("grey"))
        menu_surf.set_alpha(100)
        WIN.blit(menu_surf, (100, 75))
        WIN.blit(cross, (980, 75))

        msg = font.render("Selected: " + str(self.laser_index+1), 1, self.rand_color)
        WIN.blit(msg, (WIDTH // 3 + 30, 80))

        for i in range(5):
            rect = pygame.Rect(self.laser_x[i]+30, self.laser_y[i]+30, lasers[i].get_width()-50, lasers[i].get_height())
            WIN.blit(lasers[i], (rect.x-30, rect.y-30))

            # creating a selection menu for lasers
            try:
                mouse = pygame.mouse.get_pos()
                press = pygame.mouse.get_pressed()[0]
                if rect.collidepoint(mouse):
                    # hover effect
                    if self.laser_y[i] >= HEIGHT // 2 - 40:
                        self.laser_y[i] -= 10
                    # selection
                    if press == 1:
                        self.laser_index = i
                else:
                    self.laser_y[i] = HEIGHT // 2
            except Exception as error:
                print(error)

    def draw_laser(self, index, total):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.fire_laser = True

        if index <= total-1:
            if self.fire_laser:
                self.laser_counter += 1

                if self.laser_counter >= self.laser_cooldown:
                    rect = pygame.Rect(self.rect.x + (self.width // 2 - 58), self.rect.y, 32, 32)
                    self.laser_store.append(rect)
                    self.laser_counter = 0
                    self.fire_laser = False
                    player_laser.play()

            for laser in self.laser_store:
                WIN.blit(lasers[self.laser_index], (laser.x, laser.y))
                laser.y -= self.laser_vel

                if laser.y <= -100:
                    self.laser_store.remove(laser)

    def update(self, i, t):
        self.move()
        self.draw_laser(i, t)
        if self.score_y < 0:
            self.score_y = 35

class HealtBar():
    def __init__(self):
        self.current_health = health_fg.get_width()
        self.damage = 3
        self.blood_effect = False
        self.effect_index = 0

    def draw_msg(self):
        font = pygame.font.Font("font/Font.otf", 30)
        msg = font.render(f"Health: {self.current_health}", 1, (0, 206, 255))

        WIN.blit(msg, (WIDTH - 250, 50))
        WIN.blit(msg, (WIDTH - 251, 50))

    def draw(self):
        WIN.blit(health_bar, (WIDTH - health_bar.get_width() - 5, 5))
        WIN.blit(health_bg, (WIDTH - health_bg.get_width() - 8, 8))
        WIN.blit(pygame.transform.scale(health_fg, (self.current_health, health_fg.get_height())), (WIDTH - health_fg.get_width() - 8, 8))

    def damage_effect_screen(self):

        if self.blood_effect == True:
            self.effect_index += 1
            WIN.blit(damage_effect, (0, 0))

            if self.effect_index >= 30:
                self.blood_effect = False
                self.effect_index = 0
    
    def damage_effect_full_screen(self):

        if self.blood_effect == True:
            self.effect_index += 1
            WIN.blit(damage_effect_fullscreen, (0, 0))

            if self.effect_index >= 30:
                self.blood_effect = False
                self.effect_index = 0

    def update(self):
        self.draw_msg()
        self.draw()
        
