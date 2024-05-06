import pygame

from .screen import Screen
from view.ui.menu import field


class Menu(Screen):
	''' Окно меню '''

	def __init__(self, **kwargs):
		super().__init__(name='menu', **kwargs)

		new_game_btn = field.Button('New Game', pygame.Rect(100, 25, 300, 140))
		new_game_btn.bind(lambda: self._path_manager.forward('game'))

		load_game_btn = field.Button('Load Game', pygame.Rect(100, 165, 300, 140))
		load_game_btn.bind(lambda: print('Load Game'))

		options_btn = field.Button('Options', pygame.Rect(100, 305, 300, 140))
		options_btn.bind(lambda: print('Options'))

		exit_btn = field.Button('Exit', pygame.Rect(100, 445, 300, 140))
		exit_btn.bind(lambda: exit())
		self.add(new_game_btn, load_game_btn, options_btn, exit_btn)

	def draw(self, surface: pygame.Surface) -> None:
		for sprite in self:
			sprite.draw(surface)
