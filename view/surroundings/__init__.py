from abc import ABC
from typing import Tuple

from pygame import Rect

import settings


class Object(ABC):
	''' Преграждающий объект '''

	def __init__(self, x: int, y: int, size: Tuple[int, int]=settings.BLOCK_SIZE):
		self.rect = Rect((x, y, *size))

	def collide(self, entity) -> bool:
		return self.rect.colliderect(entity.rect)


class FantomObject(Object):
	''' Не преграждающий объект '''

	def collide(self, entity) -> bool:
		return False
