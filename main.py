# -*- coding: utf-8 -*-

import pygame

from config import SCREEN
from src.controllers.event_controllers import EventController


pygame.init()


class Application:
	def __init__(self):
		self.screen = pygame.display.set_mode(SCREEN.size)
		pygame.display.set_caption('Stardew Valley')

		self.timer = pygame.time.Clock()

		self.event_controller = EventController(self.screen)

	def run(self) -> None:
		while self.event_controller.is_worked:
			self.event_controller.check_event()

			self.screen.fill((0, 0, 0))

			self.event_controller.update()
			self.event_controller.draw()

			pygame.display.update()
			self.timer.tick(60)


if __name__ == '__main__':
	app = Application()
	app.run()