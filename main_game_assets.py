import pygame
from settings import *
pygame.init()

# loading player images
player_ships_raw = [pygame.image.load(f"Assets/ships/{i}.png").convert_alpha() for i in range(1, 9)]
player_ships = [pygame.transform.scale(player_ships_raw[i], (player_ships_raw[i].get_width() // 5, player_ships_raw[i].get_height() // 5)) for i in range(8)]

planets_raw = [pygame.image.load(f"Assets/planets/{i}.png").convert_alpha() for i in range(1, 5)]
planets = [pygame.transform.scale(planets_raw[i], (planets_raw[i].get_width() // 2, planets_raw[i].get_height() // 2)) for i in range(4)]

card = pygame.image.load("Assets/ui/card.png").convert_alpha()
help_fg = pygame.image.load("Assets/ui/help_fg.png").convert_alpha()
help_bg = pygame.transform.scale(pygame.image.load("Assets/ui/help_bg.png"), (1100, 1100)).convert_alpha()

bg = [pygame.transform.scale(pygame.image.load(f"Assets/bg/{i}.png"), (1100, 1100)).convert_alpha() for i in range(1, 6)]

detail = pygame.image.load("Assets/ui/details.png").convert_alpha()
engine_vfx = [pygame.image.load(f"Assets/ships/engine/{i}.png").convert_alpha() for i in range(1, 9)]
lasers = [pygame.image.load(f"Assets/ships/lasers/{i}.png").convert_alpha() for i in range(1, 6)]

cross = pygame.image.load("Assets/ui/cross.png").convert_alpha()

small_ships = [pygame.transform.scale2x(pygame.image.load(f"Assets/small_enemy_ships/{i}.png")).convert_alpha() for i in range(1, 5)]
small_ship_lasers = [pygame.transform.scale(pygame.image.load(f"Assets/small_enemy_ships/lasers/{i}.png"), (22, 35)).convert_alpha() for i in range(1, 8)]

boss_one_img = pygame.transform.scale2x(pygame.image.load("Assets/boss_1/1.png")).convert_alpha()
boss_one_explode = [pygame.transform.scale2x(pygame.image.load(f"Assets/boss_1/Explosion/{i}.png")).convert_alpha() for i in range(1, 12)]

boss_two_img = pygame.transform.scale2x(pygame.image.load("Assets/boss_2/1.png")).convert_alpha()
boss_two_explode = [pygame.transform.scale2x(pygame.image.load(f"Assets/boss_2/Explosion/{i}.png")).convert_alpha() for i in range(1, 12)]

boss_three_img = pygame.transform.scale2x(pygame.image.load("Assets/boss_3/1.png")).convert_alpha()
boss_three_explode = [pygame.transform.scale2x(pygame.image.load(f"Assets/boss_3/Explosion/{i}.png")).convert_alpha() for i in range(1, 12)]

boss_four_img = pygame.transform.scale2x(pygame.image.load("Assets/boss_4/1.png")).convert_alpha()
boss_four_explode = [pygame.transform.scale2x(pygame.image.load(f"Assets/boss_4/Explosion/{i}.png")).convert_alpha() for i in range(1, 12)]

boss_one_lasers = [pygame.transform.scale(pygame.image.load(f"Assets/boss_laser/{i}.png"), (78, 128)).convert_alpha() for i in range(1, 3)]
boss_two_lasers = [pygame.transform.scale(pygame.image.load(f"Assets/boss_laser/{i}.png"), (78, 128)).convert_alpha() for i in range(3, 5)]
boss_three_lasers = [pygame.transform.scale(pygame.image.load(f"Assets/boss_laser/{i}.png"), (78, 128)).convert_alpha() for i in range(5, 7)]
boss_four_lasers = [pygame.transform.scale(pygame.image.load(f"Assets/boss_laser/{i}.png"), (78, 128)).convert_alpha() for i in range(7, 9)]

player_shield = [pygame.transform.scale(pygame.image.load(f"Assets/ships/shield/{i}.png"), (180, 180)).convert_alpha() for i in range(1, 9)]

# vfx
energy_bar = pygame.image.load("Assets/ships/energy/bg.png").convert_alpha()
green = pygame.image.load("Assets/ships/energy/1.png").convert_alpha()
yellow = pygame.image.load("Assets/ships/energy/2.png").convert_alpha()
orange = pygame.image.load("Assets/ships/energy/3.png").convert_alpha()
red = pygame.image.load("Assets/ships/energy/4.png").convert_alpha()
health_bar = pygame.image.load("Assets/ships/health/health_bar.png").convert_alpha()
health_bg = pygame.image.load("Assets/ships/health/health_bg.png").convert_alpha()
health_fg = pygame.image.load("Assets/ships/health/health_fg.png").convert_alpha()
damage_effect = pygame.transform.scale(pygame.image.load("Assets/ships/damage/damage_effect.png"), (1100, 900)).convert_alpha()
damage_effect_fullscreen = pygame.transform.scale(pygame.image.load("Assets/ships/damage/damage_effect.png"), (1100, 1100)).convert_alpha()
mini_explosion = [pygame.transform.scale2x(pygame.image.load(f"Assets/explosion/mini/{i}.png"), ).convert_alpha() for i in range(1, 12)]
major_explosion = [pygame.transform.scale(pygame.image.load(f"Assets/explosion/major/{i}.png"), (180, 180)).convert_alpha() for i in range(1, 15)]

# powerups
power_up = [pygame.transform.scale2x(pygame.image.load(f"Assets/power_ups/{i}.png")).convert_alpha() for i in range(1, 6)]

# loading font
font = pygame.font.Font("Font/font.otf", 50)

# loading sound effects
player_laser = pygame.mixer.Sound("Sound Effects/player_laser.wav")
boss_laser = pygame.mixer.Sound("Sound Effects/boss_laser.mp3")
player_hit = pygame.mixer.Sound("Sound Effects/player_hit.mp3")
boss_hit = pygame.mixer.Sound("Sound Effects/boss_hit.mp3")
boss_explode = pygame.mixer.Sound("Sound Effects/boss_explode.mp3")
engine_warning = pygame.mixer.Sound("Sound EFfects/engine_warning.mp3")