from typing import List

import pygame

from settings import SCREEN_SIZE


class Toolboard(pygame.sprite.Group):
	''' Панель быстрого доступа '''

	def __init__(self, inventory_cells: List[pygame.sprite.Sprite]):
		super().__init__(*inventory_cells)
		self._cell_width, self._cell_height = inventory_cells[0].rect.size
		self._toolboard_margin = (SCREEN_SIZE[0] - len(inventory_cells) * self._cell_width) // 2
		self._select_cell = 0	# Индекс выбранной ячейки панели

	@property
	def select_cell(self) -> int:
		return self._select_cell

	@select_cell.setter
	def select_cell(self, index: int) -> None:
		ind = index - 1
		if ind < 0:
			ind = 9

		self._select_cell = ind

	def draw(self, surface: pygame.Surface) -> None:
		for index, cell in enumerate(self):
			if index == self.select_cell:
				cell.image.fill(pygame.Color('blue'))
			else:
				cell.image.fill(pygame.Color('yellow'))

			x_pos = index * self._cell_width + self._toolboard_margin
			y_pos = int(SCREEN_SIZE[1] - self._cell_height * 1.5)
			surface.blit(cell.image, (x_pos, y_pos))
