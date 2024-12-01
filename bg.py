import pygame

from settings import *
from main_game_assets import *

pygame.init()

class Background():
    def __init__(self):
        self.scroll = 0
        self.height = 1100
        self.scroll_speed = 0.5
        # setting up bg and planets
        self.bg_image = bg
        self.bg_index = 0
     
    def draw_bg(self):
        self.scroll += self.scroll_speed
        if self.scroll >= self.height:
            self.scroll = 0

        WIN.blit(self.bg_image[self.bg_index], (0, self.scroll))
        WIN.blit(self.bg_image[self.bg_index], (0, 0 - self.height + self.scroll))

class Transition():
    def __init__(self):
        self.x, self.y = WIDTH, 0
        self.appear = False
        self.vel = 50
        self.surf = pygame.Surface((1100, 1100))

    def draw(self):
        self.x -= self.vel
        self.surf.fill(('black'))
        WIN.blit(self.surf, (self.x, self.y))

class EnergyBar():
    def __init__(self):
        self.current_index = 0
        self.energy_level = [
            green, green, green, green, green,
            yellow, yellow, yellow, yellow, yellow,
            orange, orange, orange, orange, orange,
            red, red, red, red, red
        ]
        self.is_energy_used = False
        self.energy_counter = 0
        self.counter_threshold = 10
        self.msg_counter = 0
        self.cooldown_counter = 0

    def display_warning(self):
        font = pygame.font.Font("Font/font.otf", 22)
        msg = font.render("Engine Overheated!", 1, "red")
        self.msg_counter += 1
        if self.msg_counter <= 2:
            engine_warning.play()
            engine_warning.set_volume(0.4)
        if self.msg_counter <= 40:
            WIN.blit(msg, (280, 10))
    
        else:
            if self.msg_counter >= 60:
                self.msg_counter = 0

    def display_msg(self):
        font = pygame.font.Font("Font/font.otf", 30)
        msg = font.render(f"Engine Meter: {self.current_index}", 1, (245, 5, 105))
        WIN.blit(msg, (10, 50))
        WIN.blit(msg, (11, 50))

    def draw(self, player_laser):

        keys = pygame.key.get_pressed()
        WIN.blit(energy_bar, (5, 5))

        try:
            if keys[pygame.K_SPACE]:
                self.is_energy_used = True
            else:
                self.is_energy_used = False
                if self.current_index > 0 and self.current_index != len(self.energy_level):
                    self.current_index -= 1
            
            if self.is_energy_used:
                self.energy_counter += 1
            else:
                if self.energy_counter > 0:
                    self.energy_counter -= 1

            if self.energy_counter >= self.counter_threshold:
                if self.current_index <= len(self.energy_level) - 1:
                    self.current_index += 1
                self.energy_counter = 0

            if self.current_index == len(self.energy_level):
                self.display_warning()
                self.cooldown_counter += 1

            if self.cooldown_counter >= 100:
                self.current_index = 0
                self.cooldown_counter = 0
                
                player_laser.clear()
            
            for i in range(self.current_index):
                WIN.blit(self.energy_level[i], (i*12+11, 10))

        except Exception as error:
            print(error)
        
    def update(self, player_laser):
        self.display_msg()
        self.draw(player_laser)
