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
		self.image.fill('lightgreen')
		self.rect = pg.Rect(*pos, 50, 50)


class GameScreen(Screen):
	def __init__(self):
		super().__init__()
		self.camera = Camera(200, 150)
		self.add(Map(MAP))

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
			parent.blit(sprite.image, pos_rect)
