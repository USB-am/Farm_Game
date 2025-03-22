import pygame as pg


class HPScale(pg.sprite.Sprite):
	''' Полоса здоровья '''

	def __init__(self, target: 'Character'):
		super().__init__()

		self.target = target
		pos = self.pos_x, self.pos_y = (300, 150)
		size = self.width, self.height = (50, 250)
		self.image = pg.Surface(size)
		self.image.fill('lightgreen')
		self.rect = pg.Rect(*pos, *size)

	def update(self):
		max_height = self.height
		max_hp = self.target.max_hp
		now_hp = self.target.hp

		hp_percent = now_hp / max_hp
		now_height = max_height * hp_percent
		pos_y = self.pos_y + self.height - int(now_height)
		self.image = pg.Surface((self.width, int(now_height)))
		self.image.fill('lightgreen')
		self.rect.y = pos_y


class HUD(pg.sprite.Group):
	''' HUD персонажа '''

	def __init__(self, target: 'Character'):
		super().__init__()

		self.target = target
		self.hp_scale = HPScale(self.target)
		self.add(self.hp_scale)

	def update(self):
		[sprite.update() for sprite in self]
