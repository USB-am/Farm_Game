import pygame

from . import BaseController


class MenuController(BaseController):
	''' Обработчик событий в окне Меню '''

	def __init__(self, screen):
		super().__init__(screen)

	def check_event(self) -> None:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.RUN = False
			if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
				self.RUN = False