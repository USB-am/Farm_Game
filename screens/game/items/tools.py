import pygame as pg


class Tool(pg.sprite.Sprite):
	''' Базовое преставление инструмента '''


class Shovel(Tool):
	''' Лопата '''

	has_sight = True

	def __init__(self):
		super().__init__()

		self.image = pg.Surface((50, 50))
		self.image.fill('red')
		self.rect = pg.Rect(0, 0, 50, 50)
