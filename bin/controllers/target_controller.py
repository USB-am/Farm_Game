# -*- coding: utf-8 -*-

import pygame


class TargetController:
	def __init__(self, current_target: pygame.sprite.Sprite):
		self._target = current_target

	@property
	def target(self) -> pygame.sprite.Sprite:
		return self._target

	@target.setter
	def target(self, sprite: pygame.sprite.Sprite) -> None:
		self._target = sprite

	def execute(self, event: pygame.event) -> None:
		print(self._target, 'use', event)