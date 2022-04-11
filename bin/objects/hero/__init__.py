# -*- coding: utf-8 -*-

import pygame

import settings as Settings
from bin.objects.abstract_enemy import Enemy
from .inventory import Inventory


class Hero(Enemy):
	ATTACK_DAMAGE = 150

	def __init__(self, health: int=100, energy: int=100, rect=pygame.Rect((1, 1, 1, 1))):
		super().__init__(
			health=health,
			energy=energy,
			rect=rect
		)

		self.image = pygame.Surface(self.rect.size)
		self.image.fill((255, 0, 0))

		self.inventory = Inventory()

	def update(self, direction: str) -> None:
		up = direction == 'up'
		left = direction == 'left'
		down = direction == 'down'
		right = direction == 'right'
		ms = Settings.MOVE_SPEED

		if up:
			self.rect.y -= ms
		if left:
			self.rect.x -= ms
		if down:
			self.rect.y += ms
		if right:
			self.rect.x += ms

		self.direction = direction

	def attack(self, o):
		others = []
		others.append(o)

		super().attack(others)