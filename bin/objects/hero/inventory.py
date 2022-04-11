# -*- coding: utf-8 -*-

import pygame


class Inventory(pygame.sprite.Group):
	STATE = False

	def __init__(self):
		super().__init__()

	def open_close(self) -> None:
		self.STATE = not self.STATE