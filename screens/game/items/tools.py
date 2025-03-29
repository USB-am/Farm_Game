import pygame as pg

from settings.assets_path import SHOVEL_TOOL


class Tool(pg.sprite.Sprite):
	''' Базовое преставление инструмента '''


class Shovel(Tool):
	''' Лопата '''

	has_sight = True
	image_color = 'red'

	def __init__(self):
		super().__init__()

		self.image = pg.image.load(SHOVEL_TOOL)
		self.image = pg.transform.scale(self.image, (50, 50))
		self.rect = pg.Rect(0, 0, 50, 50)
