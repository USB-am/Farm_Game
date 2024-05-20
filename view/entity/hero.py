from typing import Tuple, List

import pygame

from . import Entity
from model.entity.inventory import Inventory as InventoryModel
from view.ui.hud.scale import Scale
from settings import BLOCK_SIZE


class IntegerProperty:
	''' Положительное целое число '''

	def __set_name__(self, owner, name):
		self.public_name = name
		self.private_name = '_' + name

	def __get__(self, instance, name):
		return instance.__dict__.get(self.private_name, name)

	def __set__(self, instance, value):
		if value <= 0:
			raise ValueError

		instance.__dict__[self.private_name] = value


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
	health = IntegerProperty()
	endurance = IntegerProperty()

	def __init__(self, *args, groups=pygame.sprite.Group(), **kwargs):
		super().__init__(*args, **kwargs)
		w, h = self.image.get_size()
		self.image = pygame.Surface((w, h*2))
		self.groups = groups

		self.health = 100
		self.endurance = 100
		self.health_scale = Scale(
			max_value=self.health,
			target=self
		)

		self.inventory = Inventory()

		self.up = self.down = self.left = self.right = False
		self.is_run = False
		self.direction = 'right'

	def update(self) -> None:
		self.MOVE_SPEED = 10 if self.is_run else 5

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
		if any((self.xvel, self.yvel)) and self.is_run:
			self.endurance -= 1

		self.rect.x += self.xvel
		super()._check_collide(self.groups)
		self.rect.y  += self.yvel
		super()._check_collide(self.groups)

		self.update_image()
		self.update_scales()

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

	def update_scales(self) -> None:
		''' Обновление шкал '''

		self.health_scale.update(self.health)
