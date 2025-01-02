import pygame
import os

pygame.init()
pygame.font.init() # Initializes pygame font librarys
pygame.mixer.init() # Initializes pygame sound effect library

# Window settings
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooters")
BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

# Fonts
HEALTH_FONT = pygame.font.SysFont('arial', 40)
WINNER_FONT = pygame.font.SysFont('arial', 100)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Sound effects
BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Grenade+1.mp3'))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Gun+Silencer.mp3'))

# Game settings
FPS = 60
VEL = 5 # Velocity
BULLET_VEL = 7

# Spaceship settinsg
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
MAX_BULLETS = 3