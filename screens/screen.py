import pygame as pg


class Screen(pg.sprite.Group):
	''' Представление экрана '''

	def __init__(self):
		super().__init__()

	def check_event(self) -> None:
		''' Проверка событий '''

		raise ModuleNotFoundError(f'{self} has not method "check_event"!')
