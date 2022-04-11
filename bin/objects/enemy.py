# -*- coding: utf-8 -*-

import pygame

from .abstract_enemy import Enemy


class Goblin(Enemy):
	ATTACK_DAMAGE = 10

	def __init__(self, health: int=100, energy: int=100, rect=pygame.Rect(5, 7, 1, 1)):
		super().__init__(
			health=health,
			energy=energy,
			rect=rect
		)
		self.image.fill((128, 255, 128))