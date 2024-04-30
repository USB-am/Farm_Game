import pygame

from tools.properties import StringProperty


class Screen(pygame.sprite.Group):
	''' Базовое представление экрана '''

	name = StringProperty()

	def __init__(self, name: str, *sprites):
		super().__init__(*sprites)
		self.name = name

	def check_events(self) -> None:
		''' Обработка событий '''

	def __str__(self):
		return f'<Screen {self.name} ({len(self)})>'
