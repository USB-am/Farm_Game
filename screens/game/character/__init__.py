from typing import Tuple
from dataclasses import dataclass

import pygame as pg

import settings


@dataclass
class Vector2D:
	x: int
	y: int

	def __call__(self, x: int, y: int) -> None:
		self.x = x
		self.y = y

	def __str__(self):
		return f'({self.x}, {self.y})'


class InventoryBackground(pg.sprite.Sprite):
	''' Задний фон инвентаря '''

	def __init__(self):
		super().__init__()
		self.size = (settings.SCREEN_SIZE[0] * .8, settings.SCREEN_SIZE[1] * .8)
		self.image = pg.Surface(self.size)
		self.image.fill('darkgrey')
		self.rect = pg.Rect(settings.SCREEN_SIZE[0] * .1, settings.SCREEN_SIZE[1] * .1, *self.size)


class InventoryCell(pg.sprite.Sprite):
	''' Ячейка инвентаря '''

	def __init__(self, size: Tuple[int], pos: Tuple[int]):
		super().__init__()

		self.image = pg.Surface(size)
		self.image.fill('lightgreen')
		self.rect = pg.Rect(*pos, *size)
		self.item = None
		self.count = 0

	def add(self, item: 'Item', count: int=1) -> None:
		if self.item is None:
			self.item = item
			self.count += count

	def get(self, count: int=1) -> 'Item':
		if self.count < count:
			raise ValueError(f'Cell hasn\'t {count} items')

		self.count -= count
		item = self.item
		if not self.count:
			self.item = None

		return item

	def draw(self, parent: pg.Surface) -> None:
		parent.blit(self.image, self.rect.topleft)


class Inventory(pg.sprite.Group):
	''' Инвентарь '''

	def __init__(self):
		super().__init__()

		self.is_open = False
		self.background = InventoryBackground()

		for cell in range(30):
			row = cell // 10
			col = cell % 10
			pos = (col * 30, row * 30)

			self.add(InventoryCell((25, 25), pos))

	def open(self):
		self.is_open = True

	def close(self):
		self.is_open = False

	def event(self, event) -> None:
		if event.type == pg.KEYDOWN:
			if event.key == pg.K_e:
				self.close()

	def draw(self, parent: pg.Surface) -> None:
		parent.blit(self.background.image, self.background.rect.topleft)
		for sprite in self.sprites():
			sprite.draw(self.background.image)


class Character(pg.sprite.Sprite):
	''' Персонаж '''

	def __init__(self, pos, group):
		super().__init__()

		self.image = pg.Surface((50, 50))
		self.image.fill('green')
		self.rect = pg.Rect(*pos, 50, 50)
		self.group = group
		self.prev_x, self.prev_y = pos
		self.vec = Vector2D(0, 0)
		self.speed = 10
		self.inventory = Inventory()

	def event(self, event) -> None:
		self.prev_x = self.rect.x
		self.prev_y = self.rect.y

		if self.inventory.is_open:
			self.inventory.event(event)
			return

		if event.type == pg.KEYDOWN:
			if event.key == pg.K_w:
				self.vec.y = -self.speed
			if event.key == pg.K_a:
				self.vec.x = -self.speed
			if event.key == pg.K_s:
				self.vec.y = self.speed
			if event.key == pg.K_d:
				self.vec.x = self.speed
			if event.key == pg.K_e:
				self.inventory.open()

		if event.type == pg.KEYUP:
			if event.key in (pg.K_w, pg.K_s):
				self.vec.y = 0
			if event.key in (pg.K_a, pg.K_d):
				self.vec.x = 0

		self.rect.y += self.vec.y
		if self.is_collide(self.group):
			self.rect.y = self.prev_y
		self.rect.x += self.vec.x
		if self.is_collide(self.group):
			self.rect.x = self.prev_x

	def is_collide(self, group: pg.sprite.Group) -> bool:
		''' Проверка на колизии '''

		for sprite in group:
			if sprite.collide(self.rect):
				return True
		return False
