# -*- coding: utf-8 -*-

import pygame

import settings as Settings


class PropertyValue:
	def __init__(self, value: int):
		self._value = value

	@property
	def value(self) -> int:
		return self._value

	@value.setter
	def value(self, value: int) -> None:
		self._value = value


class BaseObject(pygame.sprite.Sprite):
	def __init__(self, health: int, energy: int, rect: pygame.Rect):
		self.health = PropertyValue(health)
		self.energy = PropertyValue(energy)

		b_width, b_height = Settings.BLOCK.size
		self.rect = pygame.Rect(
			rect.x * b_width, rect.y * b_height,
			rect.width * b_width, rect.height * b_height
		)

		super().__init__()

	def is_kill(self) -> bool:
		return self.get_health() <= 0

	def get_health(self) -> int:
		return self.health.value

	def get_energy(self) -> int:
		return self.energy.value

	def take_damage(self, damage: int) -> None:
		self.health.value -= damage

		if self.is_kill():
			self.kill()

	def __str__(self) -> str:
		return f'{self.__class__.__name__} '\
			f'[Health: {self.health.value}, Energy: {self.energy.value}]'

	def draw(self, parent: pygame.Surface) -> None:
		parent.blit(self.image, self.rect.pos)