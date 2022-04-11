# -*- coding: utf-8 -*-

import pygame

from .abstract_enemy import Enemy


class PeacefulEnemy(Enemy):
	def __init__(self, health: int=100, energy: int=100, rect=pygame.Rect(1, 1, 1, 1)):
		super().__init__(
			health=health,
			energy=energy,
			rect=rect
		)