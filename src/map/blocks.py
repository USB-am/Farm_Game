import pygame

from config import BLOCK_SIZE


class BaseBlock(pygame.sprite.Sprite):
	def __init__(self, position: tuple[int, int], size: tuple[int, int]):
		super().__init__()

		# setup
		self.image = pygame.Surface(size)
		self.image.fill('#ffffff')
		self.rect = pygame.Rect(position, size)

		self.health = float('inf')


class Border(BaseBlock):
	def __init__(self, position: tuple[int, int]):
		super().__init__(position, BLOCK_SIZE.size)


BLOCK_SYMBOLS = {
	'#': Border,
}