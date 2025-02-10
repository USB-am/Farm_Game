from typing import Tuple

import pygame as pg


MAP = '''
#######################################
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
		size = (60, 60)
		self.image = pg.Surface(size)
		self.image.fill('lightgrey')
		self.rect = pg.Rect(*pos, *size)

	def event(self, event) -> None:
		pass


class Map(pg.sprite.Group):
	''' Карта '''

	def __init__(self, map_: str):
		super().__init__()

		self._fill_group(map_)

	def _fill_group(self, elements: str) -> None:
		for row, row_elements in enumerate(elements.strip().split('\n')):
			for col, element in enumerate(row_elements):
				if element == '#':
					stone = Stone(pos=(col*60, row*60))
					self.add(stone)
