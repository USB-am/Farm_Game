from typing import Tuple

import pygame as pg

import settings
from settings.assets_path import STONE_ASSET, SHOVEL_TOOL, HOUSE_ASSET
from .items.tools import Shovel


class MapElement(pg.sprite.Sprite):
	has_collide_event = False

	def __init__(self, pos: Tuple[int]):
		super().__init__()
		self.pos = pos
		self.image = pg.image.load(self.image_path)
		self.image = pg.transform.scale(self.image, settings.BLOCK_SIZE)
		self.rect = pg.Rect(*pos, *settings.BLOCK_SIZE)

	def event(self, instance) -> None:
		pass

	def collide(self, rect: pg.Rect) -> bool:
		return self.rect.colliderect(rect)

	def draw(self, parent: pg.Surface, camera_rect: pg.Rect) -> None:
		parent.blit(self.image, camera_rect)


class Drop(MapElement):
	has_collide_event = True
	image_path = SHOVEL_TOOL

	def target_collide_event(self, target: 'Character') -> None:
		''' Событие коллизии с таргетом '''
		target.inventory.add_item(Shovel(), 1)
		self.kill()


MAP = '''
###################
#  D              #
#   ##   H        #
#                 #
#     ##          #
#                 #
#                 #
#                 #
#                 #
#                 #
#                 #
#                 #
#                 #
#                 #
#                 #
#                 #
#                 #
###################'''

class Stone(MapElement):
	''' Камень '''
	image_path = STONE_ASSET


class House(MapElement):
	''' Дом '''
	image_path = HOUSE_ASSET

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.size_image = (settings.BLOCK_SIZE[0]*3, settings.BLOCK_SIZE[1]*2)
		self.size_rect = (settings.BLOCK_SIZE[0]*3, settings.BLOCK_SIZE[1])
		self.image = pg.transform.scale(self.image, self.size_image)
		self.rect = pg.Rect(
			self.rect.x,
			self.rect.y,
			*self.size_rect)

	def draw(self, parent: pg.Surface, camera_rect: pg.Rect) -> None:
		roof_rect = camera_rect.copy()
		roof_rect.y -= settings.BLOCK_SIZE[1]
		parent.blit(self.image, roof_rect, (0, 0, *self.size_rect))
		parent.blit(self.image, camera_rect, (0, settings.BLOCK_SIZE[1], *self.size_rect))


class Map(pg.sprite.Group):
	''' Карта '''

	def __init__(self, map_: str):
		super().__init__()

		self._fill_group(map_)

	def _fill_group(self, elements: str) -> None:
		self.width = 0
		self.height = 0
		self.width_px = 0
		self.height_px = 0

		for row, row_elements in enumerate(elements.strip().split('\n')):
			self.height += 1
			self.height_px += settings.BLOCK_SIZE[1]

			for col, element in enumerate(row_elements):
				self.width += 1
				self.width_px += settings.BLOCK_SIZE[0]

				if element == '#':
					stone = Stone(pos=(col*60, row*60))
					self.add(stone)
				if element == 'D':
					drop = Drop(pos=(col*60, row*60))
					self.add(drop)
				if element == 'H':
					house = House(pos=(col*60, row*60))
					self.add(house)

	@property
	def size(self) -> Tuple[int]:
		return (self.width, self.height)

	@property
	def size_px(self) -> Tuple[int]:
		return (self.width_px, self.height_px)
