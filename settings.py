# -*- coding: utf-8 -*-

import pygame


SCREEN = pygame.Rect((0, 0, 400, 250))

MOVE_SPEED = 10
PLAYER_MANAGER = {
	pygame.K_w: 'up',
	pygame.K_a: 'left',
	pygame.K_s: 'down',
	pygame.K_d: 'right',
}