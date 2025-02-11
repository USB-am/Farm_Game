import sys
from dataclasses import dataclass

import pygame as pg

from screens.screen import Screen
from .map import Map, MAP
from .camera import Camera


@dataclass
class Vector2D:
	x: int
	y: int

	def __call__(self, x: int, y: int) -> None:
		self.x = x
		self.y = y


class TestHero(pg.sprite.Sprite):
	''' Персонаж '''

	def __init__(self, pos):
		super().__init__()

		self.image = pg.Surface((50, 50))
		self.image.fill('green')
		self.rect = pg.Rect(*pos, 50, 50)
		self.vec = Vector2D(0, 0)
		self.speed = 10

	def event(self, event) -> None:
		if event.type == pg.KEYDOWN:
			if event.key == pg.K_w:
				self.vec.y -= self.speed
			if event.key == pg.K_a:
				self.vec.x -= self.speed
			if event.key == pg.K_s:
				self.vec.y += self.speed
			if event.key == pg.K_d:
				self.vec.x += self.speed

		if event.type == pg.KEYUP:
			if event.key in (pg.K_w, pg.K_s):
				self.vec.y = 0
			if event.key in (pg.K_a, pg.K_d):
				self.vec.x = 0

		self.rect.top += self.vec.y
		self.rect.left += self.vec.x


class GameScreen(Screen):
	def __init__(self):
		super().__init__()
		self.target = TestHero((60, 60))
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

			if event.type == pg.KEYDOWN and event.key == pg.K_F1:
				self.is_show_fps = not self.is_show_fps

			for sprite in self.sprites():
				sprite.event(event)

	def draw(self, parent: pg.Surface) -> None:
		for sprite in self.sprites():
			pos_rect = self.camera.apply(sprite)
			parent.blit(sprite.image, (pos_rect))

	def update(self) -> None:
		self.camera.update(self.target)
