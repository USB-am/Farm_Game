# -*- coding: utf-8 -*-

import pygame

from .managers import EventManager
from .controllers import TargetController


pygame.init()


class Game:
	SCREEN = pygame.display.set_mode((400, 250))
	TIMER = pygame.time.Clock()
	RUN = True
	EVENT_MANAGER = EventManager()
	CONTROLLER = TargetController(pygame.sprite.Sprite)

	def run(self) -> None:
		while self.RUN:
			event = self.EVENT_MANAGER.check_events()

			if event is not None:
				self.CONTROLLER.execute(event)

			self.SCREEN.fill((255, 255, 255))
			pygame.display.update()
			self.TIMER.tick(60)

		print('Game over!')