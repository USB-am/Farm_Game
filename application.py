import pygame

import settings
from screen_manager import ScreenManager
from screen_manager.menu import Menu
from screen_manager.game import Game
from screen_manager.path_manager import PathManager


pygame.init()


class Application:
	''' Главный класс игры '''

	def __init__(self):
		self.screen = pygame.display.set_mode(settings.SCREEN_SIZE)
		pygame.display.set_caption('Farm Game')

		self.timer = pygame.time.Clock()
		self.screen_manager = ScreenManager()
		self.path_manager = PathManager(self.screen_manager)

		self.screen_manager.add_screen(Menu(path_manager=self.path_manager))
		self.screen_manager.add_screen(Game(path_manager=self.path_manager))

	def run(self) -> None:
		''' Цикл приложения '''

		while True:
			self.screen.fill('black')

			self.screen_manager.current_screen.check_events()
			self.screen_manager.current_screen.update()
			self.screen_manager.current_screen.draw(self.screen)

			pygame.display.flip()
			self.timer.tick(settings.FPS)
