from abc import ABC
from typing import Tuple

import pygame

import settings


class Object(pygame.sprite.Sprite):
	''' Преграждающий объект '''

	def __init__(self, x: int, y: int, image_src: str=None):
		super().__init__()

		if image_src is None:
			self.image = pygame.Surface(settings.BLOCK_SIZE)
			self.image.fill(pygame.Color('green'))
		else:
			self.image = pygame.transform.scale(
				pygame.image.load(image_src).convert_alpha(),
				settings.BLOCK_SIZE
			)
		self.rect = pygame.Rect((x, y, *settings.BLOCK_SIZE))

	def collide(self, entity) -> bool:
		return self.rect.colliderect(entity.rect)


class FantomObject(Object):
	''' Не преграждающий объект '''

	def collide(self, entity) -> bool:
		return False
