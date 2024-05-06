import pygame

from screen_manager.screen import Screen


class Game(Screen):
	''' Главный класс игры '''

	def __init__(self, **kwargs):
		super().__init__(name='game', **kwargs)

	def draw(self, surface: pygame.Surface) -> None:
		''' Отрисовка спрайтов экрана '''

		for sprite in self:
			sprite.draw(surface)
