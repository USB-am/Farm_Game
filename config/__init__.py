import os

import pygame


SCREEN = pygame.Rect(0, 0, 400, 250)
BLOCK_SIZE = pygame.Rect(0, 0, 32, 32)

PLAYER_SIZE = (BLOCK_SIZE.width * 2, BLOCK_SIZE.height * 2)
PLAYER_CONTROL = {
	'up':    pygame.K_w,
	'left':  pygame.K_a,
	'down':  pygame.K_s,
	'right': pygame.K_d,
	'run':   pygame.K_LSHIFT,
}

BASE_DIR = os.getcwd()

# levels
LEVELS_DIR = os.path.join(BASE_DIR, 'src', 'map', 'levels')

# assest
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')

# - relief
RELIEF_DIR = os.path.join(ASSETS_DIR, 'relief')
RELIEF_GRASS = os.path.join(RELIEF_DIR, 'grass')
RELIEF_BORDER = os.path.join(RELIEF_DIR, 'border')

# - character
CHARACTER_DIR = os.path.join(ASSETS_DIR, 'character')
CHARACTER_WALK_UP = os.path.join(CHARACTER_DIR, 'walk_up')
CHARACTER_WALK_LEFT = os.path.join(CHARACTER_DIR, 'walk_left')
CHARACTER_WALK_DOWN = os.path.join(CHARACTER_DIR, 'walk_down')
CHARACTER_WALK_RIGHT = os.path.join(CHARACTER_DIR, 'walk_right')

# - objects
OBJECTS_DIR = os.path.join(ASSETS_DIR, 'objects')
HOUSES_DIR = os.path.join(OBJECTS_DIR, 'houses')