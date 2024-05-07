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

	def draw(self, surface: pygame.Surface) -> None:
		surface.blit(self.image, self.rect)
