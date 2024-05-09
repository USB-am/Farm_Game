import pygame

from view.entity import Entity
from settings import SCREEN_SIZE

# https://habr.com/ru/articles/193888/


class Camera:
	''' Камера '''

	def __init__(self, width: int, height: int):
		self.rect = pygame.Rect(0, 0, width, height)

	def apply(self, target: Entity) -> pygame.Rect:
		''' Сместить target в позицию камеры '''

		return target.rect.move(self.rect.topleft)

	def update(self, target: Entity) -> None:
		''' Обновление положения камеры относительно target '''

		l, t = target.rect.topleft
		l, t = -l + SCREEN_SIZE[0] / 2, -t + SCREEN_SIZE[1] / 2

		l = min(0, l)
		l = max(-(self.rect.width  - SCREEN_SIZE[0]), l)
		t = min(0, t)
		t = max(-(self.rect.height - SCREEN_SIZE[1]), t)

		self.rect = pygame.Rect(l, t, *self.rect.size)
