from typing import Tuple

import pygame as pg

import settings
from .items.tools import Shovel


class MapElement(pg.sprite.Sprite):
	has_collide_event = False

	def __init__(self, pos: Tuple[int]):
		super().__init__()
		self.image = pg.Surface(settings.BLOCK_SIZE)
		self.rect = pg.Rect(*pos, *settings.BLOCK_SIZE)

	def event(self, instance) -> None:
		pass

	def collide(self, rect: pg.Rect) -> bool:
		return self.rect.colliderect(rect)


class Drop(MapElement):
	has_collide_event = True

	def __init__(self, pos: Tuple[int]):
		super().__init__(pos)
		self.image.fill('red')

	def target_collide_event(self, target: 'Character') -> None:
		''' Событие коллизии с таргетом '''
		target.inventory.add_item(Shovel(), 1)
		self.kill()


MAP = '''
###################
#  D              #
#   ##  ##        #
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
	def __init__(self, pos: Tuple[int]):
		super().__init__(pos)
		self.image.fill('lightgrey')


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

	@property
	def size(self) -> Tuple[int]:
		return (self.width, self.height)

	@property
	def size_px(self) -> Tuple[int]:
		return (self.width_px, self.height_px)
