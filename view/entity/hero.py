from typing import Tuple, List

import pygame

from . import Entity
from model.entity.inventory import Inventory as InventoryModel
from settings import BLOCK_SIZE


class Item:
	pass


class InventoryCell(pygame.sprite.Sprite):
	''' Ячейка инвентаря '''

	def __init__(self, pos: Tuple[int], size: Tuple[int]):
		super().__init__()
		self.image = pygame.Surface((40, 40))
		self.image.fill(pygame.Color('yellow'))
		self.rect = pygame.Rect(*pos, *size)


class Inventory(pygame.sprite.Group):
	''' Инвентарь '''

	def __init__(self):
		super().__init__()
		self.cells: List[InventoryCell] = []

		self.__model = InventoryModel(size=40)
		for row in range(4):
			for col in range(10):
				cell = InventoryCell((col * BLOCK_SIZE[0], row * BLOCK_SIZE[1]), BLOCK_SIZE)
				self.add(cell)
				self.cells.append(cell)

	def put(self, item: Item) -> None:
		''' Положить item в инвентарь '''

		self.__model.append(item)

	def __getitem__(self, index: int) -> pygame.sprite.Sprite:
		return self.cells[index]


class Hero(Entity):
	''' Персонаж '''

	MOVE_SPEED = 5

	def __init__(self, *args, groups=pygame.sprite.Group(), **kwargs):
		super().__init__(*args, **kwargs)
		w, h = self.image.get_size()
		self.image = pygame.Surface((w, h*2))
		self.groups = groups

		self.inventory = Inventory()

		self.up = self.down = self.left = self.right = False
		self.direction = 'right'

	def update(self) -> None:
		if self.left:
			self.xvel = -self.MOVE_SPEED
		if self.right:
			self.xvel = self.MOVE_SPEED
		if self.up:
			self.yvel = -self.MOVE_SPEED
		if self.down:
			self.yvel = self.MOVE_SPEED

		if not any((self.left, self.right)):
			self.xvel = 0
		if not any((self.up, self.down)):
			self.yvel = 0

		self.rect.x += self.xvel
		super()._check_collide(self.groups)
		self.rect.y  += self.yvel
		super()._check_collide(self.groups)

		self.update_image()

	def collide(self, *a, **kw) -> bool:
		return False

	def update_image(self) -> None:
		if self.left:
			self.direction = 'left'
			self.image.fill(pygame.Color('green'))
		if self.right:
			self.direction = 'right'
			self.image.fill(pygame.Color('white'))
		if self.up:
			self.direction = 'up'
			self.image.fill(pygame.Color('blue'))
		if self.down:
			self.direction = 'down'
			self.image.fill(pygame.Color('red'))
