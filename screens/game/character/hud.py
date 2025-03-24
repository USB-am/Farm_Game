from typing import Tuple

import pygame as pg

from settings import SCREEN_SIZE


class _VerticalScale(pg.sprite.Sprite):
	''' Вертикальная полоса '''

	def __init__(self, target: 'Character', position: Tuple[int]):
		super().__init__()

		self.target = target
		self.pos_x, self.pos_y = position
		size = self.width, self.height = (50, 200)
		self.image = pg.Surface(size)
		self.image.fill(self.color)
		self.rect = pg.Rect(*position, *size)


class HPScale(_VerticalScale):
	''' Полоса здоровья '''

	def __init__(self, target: 'Character', position: Tuple[int]):
		self.color = 'lightgreen'
		super().__init__(target, position)

	def update(self):
		max_height = self.height
		max_hp = self.target.max_hp
		now_hp = self.target.hp

		hp_percent = now_hp / max_hp
		now_height = max_height * hp_percent
		pos_y = self.pos_y + self.height - int(now_height)
		self.image = pg.Surface((self.width, int(now_height)))
		self.image.fill(self.color)
		self.rect.y = pos_y


class HUD(pg.sprite.Group):
	''' HUD персонажа '''

	def __init__(self, target: 'Character'):
		super().__init__()

		self.target = target
		self.hp_scale = HPScale(
			target=self.target,
			position=(SCREEN_SIZE[0]-50, SCREEN_SIZE[1]-200))
		self.add(self.hp_scale)

	def update(self):
		[sprite.update() for sprite in self]
