from typing import Tuple

import pygame as pg


class _ScaleBackgroud(pg.sprite.Sprite):
	''' Задний фон полоски '''

	def __init__(self, size: Tuple[int], position: Tuple[int], color: str):
		super().__init__()

		self.image = pg.Surface(size)
		self.image.fill(color)
		self.rect = pg.Rect(*position, *size)


class _InnerScale(pg.sprite.Sprite):
	''' Движущаяся полоса '''

	def __init__(self, size: Tuple[int], max_value: int):
		super().__init__()

		self.max_value = max_value
		self._value = max_value
		self.size = self.width, self.height = size
		self.image = pg.Surface(size)
		self.rect = pg.Rect(0, 0, *size)

	@property
	def position(self) -> Tuple[int]:
		return self.rect.topleft

	@position.setter
	def position(self, position: Tuple[int]) -> None:
		x, y = position
		self.rect.x = x
		self.rect.y = y

	@property
	def value(self) -> int:
		return self._value

	@value.setter
	def value(self, value: int) -> None:
		if value > self.max_value:
			value = self.max_value

		self._value = value
		self.rect.height = self.__calc_scale_height()
		self.__recolor()

	def __calc_scale_height(self) -> int:
		filled_percent = self._value / self.max_value
		return int(self.height * filled_percent)

	def __recolor(self) -> None:
		pass


class _Scale(pg.sprite.Group):
	''' Полоса прокрутки '''

	def __init__(self, target: 'Character', position: Tuple[int], color: str):
		super().__init__()

		self._target = target
		self._target_scale = _InnerScale(size=(50, 250), max_value=self._target.max_hp)
		self.add(_ScaleBackgroud(size=(50, 250), position=position, color='white'))
		self.add(self._target_scale)

	def update_value(self) -> None:
		''' Обновить значение '''
		raise AttributeError('Method "update_value" is not overriden!')


class HPScale(_Scale):
	''' Полоса здоровья '''

	def __init__(self, target: 'Character'):
		super().__init__(target=target, position=(350, 350), color='red')

	def update_value(self) -> None:
		self._target_scale.value = self.target.hp


class HUD(pg.sprite.Group):
	''' HUD персонажа '''

	def __init__(self, target: 'Character'):
		super().__init__()

		self.target = target
		self.hp_scale = HPScale(self.target)

	def draw(self, parent: pg.Surface) -> None:
		for sprite in self:
			sprite.draw(parent)
