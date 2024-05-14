from typing import Tuple

import pygame


class Entity(pygame.sprite.Sprite):
	''' Существо '''

	def __init__(self, x: int, y: int, size: Tuple[int, int]):
		super().__init__()

		self.image = pygame.Surface(size)
		self.image.fill(pygame.Color('green'))
		self.rect = pygame.Rect(x, y, *size)

		self.xvel = 0
		self.yvel = 0

	def _check_collide(self, group: pygame.sprite.Group) -> None:
		''' Проверка элементов на столкновение с self '''

		for sprite in group:
			if sprite.collide(self):
				if self.xvel > 0:
					self.rect.right = sprite.rect.left
				if self.xvel < 0:
					self.rect.left = sprite.rect.right
				if self.yvel > 0:
					self.rect.bottom = sprite.rect.top
				if self.yvel < 0:
					self.rect.top = sprite.rect.bottom
