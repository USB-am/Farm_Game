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
		self.image.fill('lightgreen')
		self.rect = pg.Rect(0, 0, *size)

	@property
	def value(self) -> int:
		return self._value

	@value.setter
	def value(self, value: int) -> None:
		if value > self.max_value:
			value = self.max_value

		self._value = value
		self.rect.height = self.__calc_scale_height()
		# self.image = pg.Surface(self.rect.size)
		# self.image.fill('lightgreen')
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
		size = (50, 250)
		self._scale_bg = _ScaleBackgroud(size=size, position=position, color='white')
		self._target_scale = _InnerScale(size=size, max_value=self._target.max_hp)

	def update_value(self) -> None:
		''' Обновить значение '''
		raise AttributeError('Method "update_value" is not overriden!')

	def draw(self, parent: pg.Surface) -> None:
		parent.blit(self._scale_bg.image, self._scale_bg.rect.topleft)
		self._scale_bg.image.blit(self._target_scale.image, self._target_scale.rect.bottomleft)
		# self._scale_bg.image.blit(self._target_scale.image, self._target_scale.rect.topleft)


class HPScale(_Scale):
	''' Полоса здоровья '''

	def __init__(self, target: 'Character'):
		super().__init__(target=target, position=(150, 150), color='red')

	def update_value(self) -> None:
		self._target_scale.value = self._target.hp


class HUD(pg.sprite.Group):
	''' HUD персонажа '''

	def __init__(self, target: 'Character'):
		super().__init__()

		self.target = target
		self.hp_scale = HPScale(self.target)

	def draw(self, parent: pg.Surface) -> None:
		self.hp_scale.draw(parent)
