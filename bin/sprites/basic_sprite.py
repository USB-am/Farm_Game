# -*- coding: utf-8 -*-

import pygame


class BasicSprite(pygame.sprite.Sprite):
	def __init__(self, size_on_map: tuple):
		self.size_on_map = size_on_map

		self.controls = {}

		super().__init__()