import pygame as pg

import settings


class Camera:
	def __init__(self, width: int, height: int):
		self.rect = pg.Rect(0, 0, width, height)

	def apply(self, target: pg.sprite.Sprite) -> pg.Rect:
		''' Сместить таргет в позицию камеры '''

		return target.rect.move(self.rect.topleft)

	def update(self, target: pg.sprite.Sprite) -> None:
		''' Обновление позиции камеры относительно таргета '''

		l, t = target.rect.topleft
		l, t = -l + settings.SCREEN_SIZE[0] / 2, -t + settings.SCREEN_SIZE[1] / 2

		l = min(0, l)
		l = max(-(self.rect.width  - settings.SCREEN_SIZE[0]), l)
		t = min(0, t)
		t = max(-(self.rect.height - settings.SCREEN_SIZE[1]), t)

		self.rect = pygame.Rect(l, t, *self.rect.size)