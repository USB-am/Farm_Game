# -*- coding: utf-8 -*-

import pygame

import settings as Settings


class Window(pygame.sprite.Group):
	'''
	Popup window
		* size: tuple(0-1, 0-1)
	'''

	def __init__(self, size: tuple):
		super().__init__()

		self.rect = self._calc_position(size)

	def _calc_position(self, size: tuple) -> pygame.Rect:
		width, height = Settings.SCREEN.size
		win_width = width * size[0]
		win_height = height * size[1]

		padding_x = (width - win_width) // 2
		padding_y = (height - win_height) // 2

		result = pygame.Rect((padding_x, padding_y, win_width, win_height))

		return result


class Shop(Window):
	''' Abstract shop class '''
	def __init__(self):
		super().__init__(size=(.9, .9))

		self.image = pygame.Surface(self.rect.size)
		self.image.fill((128, 128, 128))