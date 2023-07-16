# -*- coding: utf-8 -*-

import pygame

from config import SCREEN, FPS


pygame.init()


class Application:
	def __init__(self):
		self.screen = pygame.display.set_mode(SCREEN.size)
		pygame.display.set_caption('Stardew Valley')

		self.timer = pygame.time.Clock()

	def run(self) -> None:
		_RUN = True

		while _RUN:
			self.screen.fill((255, 255, 255))

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					_RUN = False

			pygame.display.flip()
			self.timer.tick(FPS)


if __name__ == '__main__':
	app = Application()
	app.run()