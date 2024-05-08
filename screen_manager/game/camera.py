from typing import Callable

import pygame

from view.entity import Entity

# https://habr.com/ru/articles/193888/


class Camera:
	''' Камера '''

	def __init__(self, camera_func: Callable, width: int, height: int):
		self.camera_func = camera_func
		self.rect = pygame.Rect(0, 0, width, height)

	def apply(self, target: Entity) -> pygame.Rect:
		''' Сместить target в позицию камеры '''

		return target.rect.move(self.rect.topleft)

	def update(self, target: Entity) -> None:
		''' Обновление камеры '''

		self.rect = self.camera_func(self.rect, target.rect)
