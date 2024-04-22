import pygame

from models.menu import MenuModel
from views.menu import MenuView


class MenuController:
	''' Базовый контроллер '''

	def __init__(self, screen):
		self._screen = screen
		self._model = MenuModel()	# Started model
		self._view = MenuView()	# Started view

		self.RUN = True	# Mail loop status

	def check_events(self) -> None:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.RUN = False
			if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
				self.RUN = False