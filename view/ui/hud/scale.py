import pygame


class ScaleProperty:
	''' Дескриптор положительного числа (<= 0) '''

	def __set_name__(self, owner, name):
		self.public_name = name
		self.private_name = '_' + name

	def __get__(self, instance, name):
		return instance.__dict__.get(self.private_name, name)

	def __set__(self, instance, value):
		if value < 0:
			raise AttributeError

		instance.__dict__[self.private_name] = value


class Scale(pygame.sprite.Group):
	''' Вертикальная шкала '''

	value = ScaleProperty()

	def __init__(self, max_value: int):
		super().__init__()

		self.value = max_value
