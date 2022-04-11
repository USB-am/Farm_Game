# -*- coding: utf-8 -*-

import pygame

from .abstract_object import BaseObject


class Enemy(BaseObject):
	ATTACK_DAMAGE = 5

	def __init__(self, health: int=100, energy: int=100, rect=pygame.Rect((1, 1, 1, 1))):
		super().__init__(
			health=health,
			energy=energy,
			rect=rect
		)
		self.direction = 'left'

		self.image = pygame.Surface(self.rect.size)
		self.image.fill((0, 0, 0))

	def attack(self, others: list) -> None:
		for other in others:
			other.take_damage(self.ATTACK_DAMAGE)