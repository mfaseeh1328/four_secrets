import pygame
import math, time

from settings import *
from main_game_assets import *

pygame.init()

# positions for ships
player_x = [100, 360, 610, 838, 100, 337, 590, 845]
player_y = [200, 200, 200, 200, 560, 570, 550, 550]

x = [100, 350, 600, 850, 100, 350, 600, 850]
y = [200, 200, 200, 200, 550, 550, 550, 550]
x_off = [20, 20, 20, 20, 20, 20, 20, 20]
y_off = [45, 45, 45, 45, 45, 45, 45, 45]

hover_y = [180, 180, 180, 180, 530, 530, 530, 530]
after_hover_y = [200, 200, 200, 200, 550, 550, 550, 550]
after_player_hover_y = [200, 200, 200, 200, 560, 570, 550, 550]
current_select = 0

properties = {
    "One": {
        "Name": "Celestia Guard",
        "Speed": 70,
        "Armour": 50
    }, 
    "Two": {
        "Name": "Nebula Strike",
        "Speed": 60,
        "Armour": 55,
    },
    "Three": {
        "Name": "Nova Phantom",
        "Speed": 60,
        "Armour": 75,
    },
    "Four": {
        "Name": "Stellar Aegis",
        "Speed": 65,
        "Armour": 60,
    },
    "Five": {
        "Name": "Void Reaper",
        "Speed": 80,
        "Armour": 70,
    },
    "Six": {
        "Name": "Astral Seraph",
        "Speed": 85,
        "Armour": 50,
    },
    "Seven": {
        "Name": "Quantom Talon",
        "Speed": 70,
        "Armour": 70,
    },
    "Eight": {
        "Name": "Solar Warden",
        "Speed": 75,
        "Armour": 55,
    },
}

individual_property = [
    properties["One"], properties["Two"], properties["Three"], properties["Four"], properties["Five"], properties["Six"], properties["Seven"], properties["Eight"]
]

def hover_effects(x, y, mouse):
    card_rect = pygame.Rect(x, y, 170, 250)

    if card_rect.collidepoint(mouse):
        return True
    else:
        return False

def draw_ships(ship_image, player_x, player_y, x, y, x_off, y_off):
    WIN.blit(card, (x - x_off, y - y_off))
    WIN.blit(ship_image, (player_x, player_y))

def check_selection(player_select):
    msg = font.render(f"Selected: {player_select+1}", 1, "white")
    WIN.blit(msg, (WIDTH // 3, 30))

def display_properties(ind_prop, i, x, y):
    font = pygame.font.Font("Font/font.otf", 18)
    name = font.render("Name: " + str(ind_prop[i]["Name"]), 1, "black")
    speed = font.render("Speed: " + str(ind_prop[i]["Speed"]), 1, "black")
    armour = font.render("Armour: " + str(ind_prop[i]["Armour"]), 1, "black")

    WIN.blit(detail, (x-20, y))
    WIN.blit(name, (x-1, y+20))
    WIN.blit(speed, (x, y+40))
    WIN.blit(armour, (x, y+60))

class Shop():
    def __init__(self):
        self.running = True

    def choose(self):
        global PLAYER_SELECT, current_select
        
        while self.running:

            mouse_pos = pygame.mouse.get_pos()
            mouse_press = pygame.mouse.get_pressed()[0]
            
            WIN.fill(("black"))
            #bg[-1].set_alpha(200)
            #WIN.blit(bg[-1], (math.sin(time.time()) * 15 + 0, math.cos(time.time()) * 15 + 0))
            WIN.blit(help_bg, (0, 0))

            font = pygame.font.Font("font/Font.otf", 27)
            exit_btn = font.render("Press ESC", 1, "white")
            WIN.blit(exit_btn, (10, 10))

            r, c = 1, 1
            for ships in player_ships:
                draw_ships(ships, player_x[r-1], player_y[c-1], x[r-1], y[c-1], x_off[r-1], y_off[c-1])
                r += 1
                c += 1

            check_selection(current_select)

            for i in range(8):
                hover_effects(x[i], y[i], mouse_pos)
                if hover_effects(x[i], y[i], mouse_pos) == True:
                    if y[i] >= hover_y[i]:
                        y[i] -= 5
                        player_y[i] -= 20 
                    display_properties(individual_property, i, x[i], y[i] + 100)
                
                    if mouse_press == 1:
                        current_select = i
                else:
                    y[i] = after_hover_y[i]
                    player_y[i] = after_player_hover_y[i]

            CLOCK.tick(FPS)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False

        return current_select
        