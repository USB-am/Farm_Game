import os

import pygame


SCREEN = pygame.Rect(0, 0, 400, 250)
BLOCK_SIZE = pygame.Rect(0, 0, 32, 32)

PLAYER_CONTROL = {
	'up':    pygame.K_w,
	'left':  pygame.K_a,
	'down':  pygame.K_s,
	'right': pygame.K_d,
	'run':   pygame.K_LSHIFT,
}

BASE_DIR = os.getcwd()
LEVELS_DIR = os.path.join(BASE_DIR, 'src', 'map', 'levels')