import pygame
pygame.init()
# declaring variables
WIDTH, HEIGHT = 1100, 850
FPS = 60
MONITOR_SIZE = (pygame.display.Info().current_w, pygame.display.Info().current_h)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FULLSCREEN = False
pygame.display.set_caption("Space Shooter")
CLOCK = pygame.time.Clock()
PLAYER_SELECT = 0
CURRENT_STAGE = 0

def play_music(volume):
    # loading music
    pygame.mixer.music.load("Music/bg_music.mp3")
    pygame.mixer.music.set_volume(volume)
    return pygame.mixer.music.play(-1)