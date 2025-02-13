import sys

import pygame as pg

from screens.screen import Screen
from .map import Map, MAP
from .camera import Camera
from .character import Character


class GameScreen(Screen):
	def __init__(self):
		super().__init__()
		self._map = Map(MAP)
		self.target = Character((60, 60), group=self._map)
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

		if self.target.inventory.is_open:
			self.target.inventory.draw(parent)

	def update(self) -> None:
		self.camera.update(self.target)
