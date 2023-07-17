# -*- coding: utf-8 -*-

import pygame

from config import SCREEN, FPS
from controllers import MenuController


pygame.init()


class Application:
	def __init__(self):
		self.screen = pygame.display.set_mode(SCREEN.size)
		pygame.display.set_caption('Stardew Valley')

		self.timer = pygame.time.Clock()
		self.view = MenuController(self.screen)

	def run(self) -> None:
		while self.view.RUN:
			self.screen.fill((255, 255, 255))

			self.view.check_events()

			pygame.display.flip()
			self.timer.tick(FPS)


if __name__ == '__main__':
	app = Application()
	app.run()