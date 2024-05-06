from typing import List

import pygame

from settings import BLOCK_SIZE
from view.surroundings.elements import *


OBJECTS = {
	'#': Stone,
	'S': Stone,
}


MAP = [
	'####################',
	'# SSS              #',
	'#     SS           #',
	'#   S              #',
	'#   SS S SSSSSS    #',
	'#                  #',
	'#                  #',
	'#                  #',
	'#                  #',
	'#                  #',
	'#                  #',
	'#                  #',
	'#                  #',
	'#                  #',
	'####################',
]


class Map(pygame.sprite.Group):
	''' Карта '''

	def load_map(self, map_: List[str]) -> None:
		''' Загрузить карту '''

		self.empty()

		for row, row_elements in enumerate(map_):
			for col, element in enumerate(row_elements):
				if element == ' ':
					continue
				x_pos = col * BLOCK_SIZE[0]
				y_pos = row * BLOCK_SIZE[1]
				self.add(OBJECTS[element](x_pos, y_pos))

	# def draw(self, surface: pygame.Surface) -> None:
	# 	for sprite in self:
	# 		sprite.draw(surface)
	# 	print('draw is finished')
