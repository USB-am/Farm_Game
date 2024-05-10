from typing import List, Tuple

import pygame

from screen_manager.screen import Screen
from settings import SCREEN_SIZE, BLOCK_SIZE
from view.entity.hero import Hero
from view.entity import Entity
from view.surroundings.elements import Stone
from .camera import Camera


LEVEL = [
	'##################################',
	'#                                #',
	'#                                #',
	'#                                #',
	'#                                #',
	'#                                #',
	'#                                #',
	'#                                #',
	'#                                #',
	'#                                #',
	'#                                #',
	'#                                #',
	'#                                #',
	'#                                #',
	'#                                #',
	'#                                #',
	'#                                #',
	'#                                #',
	'#                                #',
	'#                                #',
	'#                                #',
	'#                                #',
	'#  #### # #   #                  #',
	'#  #      ##  #                  #',
	'#  ###  # # # #                  #',
	'#  #    # #  ##                  #',
	'#  #    # #   #                  #',
	'#                                #',
	'##################################',
]


BLOCKS = {
	'#': Stone,
}


class Map(pygame.sprite.Group):
	''' Карта '''

	def __init__(self, map_list: List[str], **kwargs):
		super().__init__(**kwargs)
		self._map_list = map_list

		self._init_map()

	@property
	def map_list(self) -> List[str]:
		return self._map_list

	@map_list.setter
	def map_list(self, new_map: List[str]) -> None:
		if not isinstance(new_map, list):
			raise ValueError

		self._map_list = new_map
		self._init_map()

	def _init_map(self) -> None:
		''' Инициализировать объекты карты '''

		self.empty()

		for row, _ in enumerate(self.map_list):
			for col, symbol in enumerate(_):
				block_obj = BLOCKS.get(symbol)
				if block_obj is None:
					continue
				pos_x = col * BLOCK_SIZE[0]
				pos_y = row * BLOCK_SIZE[1]
				self.add(block_obj(pos_x, pos_y))

	@property
	def size(self) -> Tuple[int]:
		''' Максимальный размер карты '''

		width = max([len(row) for row in self._map_list])
		height = len(self._map_list)

		return (width, height)

	@property
	def size_px(self) -> Tuple[int]:
		''' Максимальный размер карты в пикселях '''

		width, height = self.size
		return (width * BLOCK_SIZE[0], height * BLOCK_SIZE[1])


class Game(Screen):
	''' Главный класс игры '''

	def __init__(self, **kwargs):
		super().__init__(name='game', **kwargs)

		self.target = Hero(200, 200, (30, 30), groups=self)
		self.map_ = Map(LEVEL)
		self.add(*self.map_)
		self.camera = Camera(*self.map_.size_px)
		self.add(self.target)

	def keydown_event(self, event) -> None:
		''' Обработка нажатия клавиши '''

		if event.key == pygame.K_w:
			self.target.up = True
		if event.key == pygame.K_a:
			self.target.left = True
		if event.key == pygame.K_s:
			self.target.down = True
		if event.key == pygame.K_d:
			self.target.right = True

	def keyup_event(self, event) -> None:
		''' Обработка отжатия клавиши '''

		if event.key == pygame.K_w:
			self.target.up = False
		if event.key == pygame.K_s:
			self.target.down = False
		if event.key == pygame.K_a:
			self.target.left = False
		if event.key == pygame.K_d:
			self.target.right = False

	def update(self) -> None:
		self.camera.update(self.target)
		self.target.update()

	def draw(self, surface: pygame.Surface) -> None:
		for sprite in self:
			surface.blit(sprite.image, self.camera.apply(sprite))
