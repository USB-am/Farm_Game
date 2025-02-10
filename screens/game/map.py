from typing import Tuple

import pygame as pg

import settings


MAP = '''
#######################################
#                                     #
#                                     #
#                                     #
#                                     #
#                                     #
#                                     #
#                                     #
#                                     #
#                                     #
#                                     #
#                                     #
#                                     #
#                                     #
#                                     #
#                                     #
#                                     #
#######################################
'''

class Stone(pg.sprite.Sprite):
	def __init__(self, pos: Tuple[int]):
		super().__init__()
		self.image = pg.Surface(settings.BLOCK_SIZE)
		self.image.fill('lightgrey')
		self.rect = pg.Rect(*pos, *settings.BLOCK_SIZE)

	def event(self, event) -> None:
		pass


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

	@property
	def size(self) -> Tuple[int]:
		return (self.width, self.height)

	@property
	def size_px(self) -> Tuple[int]:
		return (self.width_px, self.height_px)
