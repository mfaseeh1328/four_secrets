import pygame, random
import main_shop, main_help

# importing settings
from settings import *
from main_game_assets import *
# importing the game componenets i.e player, enemy, bg
from player import Player, HealtBar
from bg import Background, EnergyBar, Transition
from boss import Boss
from powerup import PowerUp

pygame.init()

# making collision function
def player_collision(player_rect, boss_laser):

    for laser in boss_laser:
        laser_rect = pygame.Rect(laser.x + 20, laser.y + 10, laser.w - 40, laser.h - 20)

        if player_rect.colliderect(laser_rect):
            boss_laser.remove(laser)
            return True
        
    return False

def boss_collision(boss_rect, player_laser):

    new_boss_rect = pygame.Rect(boss_rect.x+55, boss_rect.y+90, boss_rect.w-5, boss_rect.h-180)

    for laser in player_laser:
        laser_rect = pygame.Rect(laser.x+45, laser.y+50, laser.w, laser.h+20)

        if new_boss_rect.colliderect(laser_rect):
            player_laser.remove(laser)
            return True
        
    return False

def explosion_effect(x, y, index, divisor):
    WIN.blit(mini_explosion[index // divisor], (x, y))

def draw_msg(x, y, msg, color, size):
    font = pygame.font.Font("font/Font.otf", size)
    score = font.render(msg, 1, color)
    WIN.blit(score, (x, y))

class Game():
    def __init__(self):
        self.running = True
        self.player = Player(main_shop.current_select)
        self.bg = Background()
        self.energy_bar = EnergyBar()
        self.health_bar = HealtBar()
        self.transition = Transition()

        x, y = 300, 0
        self.boss_one = Boss(boss_one_img, x, y, 150, boss_one_explode, "pink", "magenta", 2, 6, 5, 15, 50, boss_one_lasers)
        self.boss_two = Boss(boss_two_img, x, y+10, 175, boss_two_explode, "grey", (235, 51, 0), 3, 8, 6, 18, 45, boss_two_lasers)
        self.boss_three = Boss(boss_three_img, x, y+15, 200, boss_three_explode, (189, 89, 53), "gold", 4, 9, 7, 21, 40, boss_three_lasers)
        self.boss_four = Boss(boss_four_img, x, y+25, 225, boss_four_explode, "light blue", "yellow", 4, 10, 8, 24, 35, boss_four_lasers)

        self.bosses = [self.boss_one, self.boss_two, self.boss_three, self.boss_four]

        self.player_power_up = PowerUp()

    def run(self):
        global FULLSCREEN, WIN, CURRENT_STAGE

        play_music(0.25)
        while self.running:
            pygame.display.set_caption(f"FPS: {round(CLOCK.get_fps(), 2)}")

            keys = pygame.key.get_pressed()
            WIN.fill(("black"))

            self.bg.bg_index = CURRENT_STAGE
            self.bg.draw_bg()
            
            if FULLSCREEN:
                self.health_bar.damage_effect_full_screen()
                self.player.shield_pos_y = 870
            else:
                self.health_bar.damage_effect_screen()
                self.player.shield_pos_y = HEIGHT - 180

            # player i.e draw, bars, health etc...
            if self.player.laser_menu  != True:
                self.player.update(self.energy_bar.current_index, len(self.energy_bar.energy_level))
                
                try:
                    if self.bosses[CURRENT_STAGE].is_dead != True:
                        self.bosses[CURRENT_STAGE].move()
                        self.bosses[CURRENT_STAGE].draw_laser()
                except Exception as error:
                    raise error
            
            self.energy_bar.update(self.player.laser_store)
            self.health_bar.update()
            self.player.draw()

            if CURRENT_STAGE >= 1:
                self.player.vel = 11

            if CURRENT_STAGE >= 2:
                self.player.draw_shield()

            if CURRENT_STAGE >= 3:
                if keys[pygame.K_r]:
                    if (self.player.rect.width <= self.player.width) and (self.player.rect.height <= self.player.height):
                        self.player.rect.width += 1
                        self.player.rect.height += 1
                    
                if keys[pygame.K_w]:
                    if (self.player.rect.width >= 80) and (self.player.rect.height >= 80):
                        self.player.rect.width -= 1
                        self.player.rect.height -= 1

            if CURRENT_STAGE >= 3 and self.player_power_up.appear == True:
                self.health_bar.current_health = 249
                        
            # making a short menu to let player select laser
            if keys[pygame.K_s] and self.player.laser_menu == False:
                self.player.laser_menu = True

            # boss
            self.bosses[CURRENT_STAGE].update()

            # powerup
            self.player_power_up.draw()

            # drawing text for score
            draw_msg(WIDTH // 2 - 100, 10, f"Total Score: {round(self.player.total_score, 2)}", (250, 246, 0), 30)
            draw_msg(WIDTH // 2 - 99, 10, f"Total Score: {round(self.player.total_score, 2)}", (250, 246, 0), 30)
            if self.bosses[CURRENT_STAGE].is_dead != True and self.player.laser_menu != True:
                self.player.total_score += 0.2


            self.player.attempt_index += 1
            if self.player.attempt_index <= 30:
                draw_msg(WIDTH - 150, HEIGHT - 100, f"Attempts: {self.player.attempts+1}", ("orange"), 30)
                draw_msg(WIDTH - 149, HEIGHT - 50, f"Stage: {CURRENT_STAGE+1}", (245, 5, 105), 30)
                draw_msg(1100, HEIGHT // 3, f"Support If You Liked", ("white"), 20)
            
            if self.player.attempt_index >= 60:
                self.player.attempt_index = 0

            # collision call
            if (player_collision(self.player.rect, self.bosses[CURRENT_STAGE].laser_store) == True) and (self.health_bar.current_health > self.health_bar.damage - self.health_bar.damage):
                if (self.player.is_shield == True and self.player.cooldown_counter < 200) or (self.player.is_shield == False):
                    if self.health_bar.current_health >= 25:
                        self.health_bar.damage = random.randint(3, 16)
                    else:
                        if self.health_bar.current_health <= 25:
                            self.health_bar.damage = 5
                        if self.health_bar.current_health <= 5:
                            self.health_bar.damage = 1
                    self.health_bar.current_health -= self.health_bar.damage
                    self.health_bar.blood_effect = True
                    self.player.explosion_offset = []
                    self.player.explosion_offset.append([self.player.rect.x + 20, self.player.rect.y])
                    player_hit.play()
            
            
            if (boss_collision(self.bosses[CURRENT_STAGE].rect, self.player.laser_store) == True and (self.bosses[CURRENT_STAGE].current_health > self.bosses[CURRENT_STAGE].damage - self.bosses[CURRENT_STAGE].damage)):
                self.bosses[CURRENT_STAGE].damage = random.uniform(0.4, 2.0)
                self.bosses[CURRENT_STAGE].current_health -= self.bosses[CURRENT_STAGE].damage
                self.bosses[CURRENT_STAGE].laser_hit = True
                self.bosses[CURRENT_STAGE].explosion_effect = []
                self.bosses[CURRENT_STAGE].explosion_effect.append([self.bosses[CURRENT_STAGE].rect.x, self.bosses[CURRENT_STAGE].rect.y])
                self.player.total_score += 25
                boss_hit.set_volume(0.45)
                boss_hit.play()

            # explosion effects
            if self.health_bar.blood_effect == True:
                for offset in self.player.explosion_offset:
                    explosion_effect(offset[0], offset[1], self.health_bar.effect_index, 3)

            if self.bosses[CURRENT_STAGE].laser_hit == True:
                for offset in self.bosses[CURRENT_STAGE].explosion_effect:
                    explosion_effect(offset[0]+60, offset[1]+90, self.bosses[CURRENT_STAGE].effect_index, 2)
                
                self.player.score_y -= 1
                draw_msg(WIDTH // 2 + 100, self.player.score_y, "+25", "red", 25)

            # progress
            if self.bosses[CURRENT_STAGE].current_health <= 0:
                self.bosses[CURRENT_STAGE].is_dead = True

            if self.bosses[CURRENT_STAGE].is_dead:
                self.bosses[CURRENT_STAGE].explode_counter += 1

                if self.bosses[CURRENT_STAGE].explode_counter <= 10:
                    boss_explode.play()
                    self.bosses[CURRENT_STAGE].is_dead = False
                    self.player_power_up.appear = True

            # progressing to next bosses
            def reset():
                self.bosses[CURRENT_STAGE].is_dead = False
                self.bosses[CURRENT_STAGE].x = 300
                self.bosses[CURRENT_STAGE].y = 20
                self.bosses[CURRENT_STAGE].current_health = self.bosses[CURRENT_STAGE].current_health

            if self.player_power_up.appear == True:
                if self.player_power_up.collide(self.player.rect) == True:
                    self.player_power_up.collided = True

                if self.bosses[CURRENT_STAGE].death_counter >= 200:
                    self.transition.appear = True
                if self.bosses[CURRENT_STAGE].death_counter >= 250:
                    if CURRENT_STAGE <= 2:
                        CURRENT_STAGE += 1
                        self.player_power_up.power_up_index += 1
                        reset()
                        self.player_power_up.collided = False
                        self.player_power_up.appear = False
                        self.bosses[CURRENT_STAGE].death_counter = 0
                        self.transition.appear = False

            if self.player_power_up.collided:
                self.bosses[CURRENT_STAGE].death_counter += 1
                self.player_power_up.rect.x = -100
                self.player_power_up.draw_msg()
            else:
                self.player_power_up.rect.x = WIDTH // 2 - 150

            if self.transition.appear:
                self.transition.draw()
            else:
                self.transition.x = WIDTH

            if CURRENT_STAGE >= 3 and self.bosses[CURRENT_STAGE].death_counter >= 240:
                CURRENT_STAGE = 0
                self.running = False

            # player loses
            if self.health_bar.current_health <= 0:
                self.player.draw_explosion()
                if self.player.major_explosion_index <= 30:
                    boss_explode.play()
                if self.player.major_explosion_index >= 209:
                    self.player.attempts += 1
                    self.health_bar.current_health = 249
                    CURRENT_STAGE = 0

            # laser selection for player
            if self.player.laser_menu:
                self.player.draw_laser_menu()

            mouse_pos = pygame.mouse.get_pos()
            if pygame.Rect(980, 75, 20, 20).collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0] == 1:
                    self.player.laser_menu = False

            CLOCK.tick(FPS)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                    
                    if event.key == pygame.K_f:
                        FULLSCREEN = True
                        
                        if FULLSCREEN == True:
                            WIN = pygame.display.set_mode(MONITOR_SIZE, pygame.FULLSCREEN)

                    if event.key == pygame.K_u:
                        FULLSCREEN = False
                        WIN = pygame.display.set_mode((1100, 900))
