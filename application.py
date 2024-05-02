import pygame

import settings
from screen_manager import ScreenManager
from screen_manager.menu import Menu


pygame.init()


class Application:
	''' Главный класс игры '''

	def __init__(self):
		self.screen = pygame.display.set_mode(settings.SCREEN_SIZE)
		pygame.display.set_caption('Farm Game')

		self.timer = pygame.time.Clock()
		self.screen_manager = ScreenManager()
		self.screen_manager.add_screen(Menu())

	def run(self) -> None:
		''' Цикл приложения '''

		while True:
			self.screen.fill('black')

			self.screen_manager.current_screen.check_events()
			self.screen_manager.current_screen.update()
			self.screen_manager.current_screen.draw(self.screen)

			pygame.display.flip()
			self.timer.tick(settings.FPS)
