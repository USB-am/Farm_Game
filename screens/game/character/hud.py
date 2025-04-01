from typing import Tuple

import pygame as pg

from settings import SCREEN_SIZE


class _VerticalScale(pg.sprite.Sprite):
	''' Вертикальная полоса '''

	def __init__(self, target: 'Character', position: Tuple[int]):
		super().__init__()

		self.target = target
		self.pos_x, self.pos_y = position
		size = self.width, self.height = (50, 200)
		self.image = pg.Surface(size)
		self.image.fill(self.color)
		self.rect = pg.Rect(*position, *size)

	def draw(self, parent: pg.Surface) -> None:
		parent.blit(self.image, self.rect.topleft)


class HPScale(_VerticalScale):
	''' Полоса здоровья '''

	def __init__(self, target: 'Character', position: Tuple[int]):
		self.color = 'lightgreen'
		super().__init__(target, position)

	def update(self):
		max_height = self.height
		max_hp = self.target.max_hp
		now_hp = self.target.hp

		hp_percent = now_hp / max_hp
		now_height = max_height * hp_percent
		pos_y = self.pos_y + self.height - int(now_height)
		self.image = pg.Surface((self.width, int(now_height)))
		self.image.fill(self.color)
		self.rect.y = pos_y


class ToolPanel(pg.sprite.Group):
	''' Панель инструментов '''

	def __init__(self, inventory, position: Tuple[int]):
		super().__init__()

		self.inventory = inventory
		self.position = position
		self.size = (int(SCREEN_SIZE[0]*.8), 75)
		self.background = pg.Surface(self.size)
		self.background.fill('red')
		self.background_rect = pg.Rect(self.position, self.size)
		self.add(*self.inventory.inventory_cells[:10])

	def draw(self, parent: pg.Surface) -> None:
		parent.blit(self.background, self.background_rect.topleft)
		for cell in self:
			cell.draw(self.background)


class HUD(pg.sprite.Group):
	''' HUD персонажа '''

	def __init__(self, target: 'Character'):
		super().__init__()

		self.target = target
		self.hp_scale = HPScale(
			target=self.target,
			position=(SCREEN_SIZE[0]-50, SCREEN_SIZE[1]-200))
		self.add(self.hp_scale)

		self.tool_panel = ToolPanel(
			inventory=self.target.inventory,
			position=(int(SCREEN_SIZE[0]*.1), SCREEN_SIZE[1]-75))
		self.add(self.tool_panel)

	def update(self):
		[sprite.update() for sprite in self]

	def draw(self, parent):
		self.hp_scale.draw(parent)
		self.tool_panel.draw(parent)
