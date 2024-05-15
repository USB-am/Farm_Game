import os

from . import Object, FantomObject
from config.path import GAME_BORDER_SPRITES


class Stone(Object):
	''' Камень '''

	def __init__(self, x: int, y: int):
		# super().__init__(x, y, image_src=os.path.join(GAME_BORDER_SPRITES, 'border.png'))
		super().__init__(x, y)
