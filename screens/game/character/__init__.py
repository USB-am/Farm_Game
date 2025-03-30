import enum
from typing import Tuple, List
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

	def __init__(self, size: Tuple[int], position: Tuple[int]):
		super().__init__()

		self.size = size
		self.position = position
		self.image = pg.Surface(size)
		self.image.fill('lightgreen')
		self.rect = pg.Rect(*position, *size)
		self.item = None
		self.count = 0
		self.hover = False

	def add_item(self, item: 'Item', count: int=1) -> None:
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
		if self.hover:
			self.image.fill('lightblue')
		else:
			self.image.fill('lightgreen')

		parent.blit(self.image, self.rect.topleft)
		if self.item is not None:
			item_image = pg.transform.scale(self.item.image, self.size)
			parent.blit(item_image, self.rect.topleft)


class Inventory(pg.sprite.Group):
	''' Инвентарь '''

	def __init__(self):
		super().__init__()

		self.is_open = False
		self.background = InventoryBackground()

		self.inventory_cells: InventoryCell[List] = []

		for cell in range(30):
			row = cell // 10
			col = cell % 10
			pos = (20 + col * (settings.INVENTORY_CELL_SIZE[0] + 5),
			       20 + row * (settings.INVENTORY_CELL_SIZE[1] + 5))

			self.inventory_cells.append(InventoryCell(
				size=settings.INVENTORY_CELL_SIZE,
				position=pos))
			self.add(self.inventory_cells[-1])

	def open(self):
		self.is_open = True

	def close(self):
		self.is_open = False

	def event(self, event) -> None:
		if event.type == pg.KEYDOWN:
			if event.key == pg.K_e:
				self.close()

		if event.type == pg.MOUSEMOTION:
			pos_x, pos_y = event.pos
			offset_mouse_position = (
				pos_x - self.background.rect.x,
				pos_y - self.background.rect.y
			)

			for cell in self.inventory_cells:
				if cell.rect.collidepoint(offset_mouse_position):
					cell.hover = True
					continue
				cell.hover = False

	def draw(self, parent: pg.Surface) -> None:
		parent.blit(self.background.image, self.background.rect.topleft)
		for sprite in self.sprites():
			sprite.draw(self.background.image)

	def add_item(self, item: 'Item', count: int) -> None:
		''' Добавить предмет в инвентарь '''

		for cell in self.inventory_cells:
			if not isinstance(cell.item, type(item)) and cell.item is not None:
				continue

			cell.add_item(item, count)
			break


class Direction(enum.Enum):
	''' Направление персонажа '''

	UP = 0
	LEFT = 1
	DOWN = 2
	RIGHT = 3


class Character(pg.sprite.Sprite):
	''' Персонаж '''

	def __init__(self, pos, group):
		super().__init__()

		self.max_hp = 500
		self.hp = 500

		self.image = pg.Surface((50, 50))
		self.image.fill('green')
		self.rect = pg.Rect(*pos, 50, 50)
		self.group = group
		self.prev_x, self.prev_y = pos
		self.vec = Vector2D(0, 0)
		self.speed = 10
		self.direction = Direction.LEFT
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
				self.direction = Direction.UP
			if event.key == pg.K_s:
				self.vec.y = self.speed
				self.direction = Direction.DOWN
			if event.key == pg.K_a:
				self.vec.x = -self.speed
				self.direction = Direction.LEFT
			if event.key == pg.K_d:
				self.vec.x = self.speed
				self.direction = Direction.RIGHT
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
				if sprite.has_collide_event:
					sprite.target_collide_event(self)
				return True
		return False
