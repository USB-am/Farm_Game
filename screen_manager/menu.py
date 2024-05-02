import pygame

from .screen import Screen
from view.ui.menu import field


class Menu(Screen):
	''' Окно меню '''

	def __init__(self):
		super().__init__(name='menu')

		new_game_btn = field.Button('New Game', pygame.Rect(100, 50, 300, 140))
		new_game_btn.bind(lambda: print('New Game'))

		load_game_btn = field.Button('Load Game', pygame.Rect(100, 200, 300, 140))
		load_game_btn.bind(lambda: print('Load Game'))
		self.add(new_game_btn, load_game_btn)

	def draw(self, surface: pygame.Surface) -> None:
		for sprite in self:
			sprite.draw(surface)
