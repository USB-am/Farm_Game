import sys

import pygame as pg

from screens.screen import Screen
from .map import Map, MAP
from .camera import Camera


class TestHero(pg.sprite.Sprite):
	''' Персонаж '''

	def __init__(self, pos):
		super().__init__()

		self.image = pg.Surface((50, 50))
		self.image.fill('green')
		self.rect = pg.Rect(*pos, 50, 50)
		self.speed = 100

	def event(self, event) -> None:
		if event.type == pg.KEYDOWN:
			if event.key == pg.K_w:
				self.rect.top -= self.speed
			elif event.key == pg.K_a:
				self.rect.left -= self.speed
			elif event.key == pg.K_s:
				self.rect.top += self.speed
			elif event.key == pg.K_d:
				self.rect.left += self.speed


class GameScreen(Screen):
	def __init__(self):
		super().__init__()
		self.target = TestHero((100, 100))
		self._map = Map(MAP)
		self.camera = Camera(*self._map.size_px)
		self.add(self._map)
		self.add(self.target)

	def check_event(self) -> None:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				sys.exit()
			if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
				sys.exit()

			for sprite in self.sprites():
				sprite.event(event)

	def draw(self, parent: pg.Surface) -> None:
		for sprite in self.sprites():
			pos_rect = self.camera.apply(sprite)
			parent.blit(sprite.image, (pos_rect))

	def update(self) -> None:
		self.camera.update(self.target)
