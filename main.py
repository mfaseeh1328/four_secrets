import pygame
import sys
import menu
import main_game, main_shop, main_help

# custom files
from settings import *
from hyperspace import *
from main_game_assets import *

pygame.init()

class Game():        
    def __init__(self):
        self.running = True

        # intantiating new objects
        self.star_field = Starfield(self)

    def run(self):
        global PLAYER_SELECT
        play_music(1)

        while self.running:

            pygame.display.set_caption(f"FPS: {round(CLOCK.get_fps(), 2)}")

            mouse_pos = pygame.mouse.get_pos()
            press_mouse = pygame.mouse.get_pressed()[0]
            
            # displaying and updating the window
            WIN.fill(("black"))
            WIN.blit(help_bg, (0, 0))
            self.star_field.run()
            menu.draw()

            # checking the button
            if menu.play_rect.collidepoint(mouse_pos):
                menu.hover_button(menu.play_btn, WIDTH // 2 - 200, HEIGHT // 2 - 200)

                if press_mouse == 1:
                    main_play_game = main_game.Game()
                    main_play_game.run()

            if menu.help_rect.collidepoint(mouse_pos):
                menu.hover_button(menu.help_btn, WIDTH // 2 - 200, HEIGHT // 2 - 75)

                if press_mouse == 1:
                    main_help_menu = main_help.Help()
                    main_help_menu.run()

            if menu.shop_rect.collidepoint(mouse_pos):
                menu.hover_button(menu.shop_btn, WIDTH // 2 - 200, HEIGHT // 2 + 50)

                if press_mouse == 1:
                    main_shop_menu = main_shop.Shop()
                    main_shop_menu.choose()
                    PLAYER_SELECT = main_shop_menu.choose()

            if menu.exit_rect.collidepoint(mouse_pos):
                menu.hover_button(menu.exit_btn, WIDTH // 2 - 200, HEIGHT // 2 + 175)

                if press_mouse == 1:
                    self.running = False
                    
            CLOCK.tick(FPS)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                        sys.exit()

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
