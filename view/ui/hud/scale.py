from typing import Tuple

import pygame

from view.entity import Entity


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


class VerticalScale(pygame.sprite.Sprite):
	''' Вертикальная шкала '''

	def __init__(self, max_value: int, pos: Tuple[int], size: Tuple[int]):
		super().__init__()

		self._value = max_value
		self._max_value = max_value
		self._padding = 4

		self.image = pygame.Surface(size)
		self.image.fill(pygame.Color('grey'))
		self.rect = pygame.Rect(*pos, *size)
		self.value_scale = pygame.Surface((
			size[0] - self._padding,
			int(self._value / self._max_value * size[1] - self._padding*2))
		)

	@property
	def value(self) -> int:
		return self._value

	@value.setter
	def value(self, value: int) -> None:
		if value > self._max_value:
			value = self._max_value
		elif value < 0:
			raise ValueError

		self._value = value

	def update(self, value: int) -> None:
		self._value = value
		coeff = self.value / self._max_value

		if coeff >= .75:
			self.value_scale.fill(pygame.Color('green'))
		elif coeff >= .35:
			self.value_scale.fill(pygame.Color('yellow'))
		else:
			self.value_scale.fill(pygame.Color('red'))

	def draw(self, surface: pygame.Surface) -> None:
		surface.blit(self.image, self.rect)
		l, t, w, h = self.rect

		l += self._padding // 2
		c = self._value / self._max_value
		t -= int(c * h - h)
		t += self._padding*2
		self.value_scale = pygame.transform.scale(
			self.value_scale, (
				self.value_scale.get_size()[0],
				self.rect.bottom - t
			)
		)
		surface.blit(self.value_scale, (l, t))


class Scale(pygame.sprite.Sprite):
	''' Горизонтальная шкала '''

	def __init__(self, max_value: int, target: Entity):
		super().__init__()

		self._value = max_value
		self._max_value = max_value
		self._target = target

		size = (self._target.rect.width, 10)
		pos = (self._target.rect.x, self._target.rect.y - 20)
		self.image = pygame.Surface(size)
		self.rect = pygame.Rect(*pos, *size)

	def update(self, value: int) -> None:
		self.update_pos()
		self.update_image(value)

	def update_pos(self) -> None:
		pos_x, pos_y = self._target.rect.left, self._target.rect.top - 50
		self.rect.x = pos_x
		self.rect.y = pos_y

	def update_image(self, value: int) -> None:
		self._value = value
		coeff = self.value / self._max_value

		if coeff >= .75:
			self.image.fill(pygame.Color('green'))
		elif coeff >= .35:
			self.image.fill(pygame.Color('yellow'))
		else:
			self.image.fill(pygame.Color('red'))

	@property
	def value(self) -> int:
		return self._value

	@value.setter
	def value(self, value: int) -> None:
		if value > self._max_value:
			value = self._max_value
		elif value < 0:
			raise ValueError

		self._value = value

	def collide(self, *a, **kw):
		return False

	def draw(self, surface: pygame.Surface) -> None:
		surface.blit(self.image, self.rect)
