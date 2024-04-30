import pygame

import settings
from screen_manager import ScreenManager


pygame.init()


class Application:
	''' Главный класс игры '''

	def __init__(self):
		self.screen = pygame.display.set_mode(settings.SCREEN_SIZE)
		pygame.display.set_caption('Farm Game')

		self.timer = pygame.time.Clock()
		self.screen_manager = ScreenManager()

	def run(self) -> None:
		''' Цикл приложения '''

		while self.controller.RUN:
			self.screen.fill('black')

			self.controller.check_events()

			pygame.display.flip()
			self.timer.tick(settings.FPS)
