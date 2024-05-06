import pygame

from screen_manager.screen import Screen
from view.map import Map



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


class Game(Screen):
	''' Главный класс игры '''

	def __init__(self, **kwargs):
		super().__init__(name='game', **kwargs)

		self._map = Map()
		self._map.load_map(MAP)
		self.add(self._map)

	def draw(self, surface: pygame.Surface) -> None:
		''' Отрисовка спрайтов экрана '''

		self._map.draw(surface)
