from os import path

import pygame

from config import BLOCK_SIZE, RELIEF_GRASS, RELIEF_BORDER, HOUSES_DIR
from src.entities import support


class BaseBlock(pygame.sprite.Sprite):
	def __init__(self, position: tuple[int, int], size: tuple[int, int], fantom: bool=True):
		super().__init__()

		# setup
		self.image = pygame.Surface(size)
		self.image.fill('#ffffff')
		self.rect = pygame.Rect(position, size)

		# True - the player can move through the block
		self.fantom = fantom
		self.health = float('inf')


class MultiblockDesign(pygame.sprite.Group):
	def __init__(self, size: tuple[int, int]):
		super().__init__()

		# setup
		self.size = size


class Border(BaseBlock):
	texture = path.join(RELIEF_BORDER, 'image_part_013.png')

	def __init__(self, position: tuple[int, int]):
		super().__init__(position, BLOCK_SIZE.size)

		self.fantom = False
		self.image = pygame.image.load(self.texture)
		self.image = pygame.transform.scale(self.image, BLOCK_SIZE.size)


class Grass(BaseBlock):
	texture = path.join(RELIEF_GRASS, 'image_part_002.png')

	def __init__(self, position: tuple[int, int]):
		super().__init__(position, BLOCK_SIZE.size)

		self.image = pygame.image.load(self.texture)
		self.image = pygame.transform.scale(self.image, BLOCK_SIZE.size)


class MultiblockDesignElement(BaseBlock):
	def __init__(self, position: tuple[int, int], image: pygame.image, fantom: bool=False):
		super().__init__(position, BLOCK_SIZE.size, fantom)

		self.image = image


class Home(pygame.sprite.Group):
	textures = support.get_sprites_from_folder(path.join(HOUSES_DIR, '1'), BLOCK_SIZE.size)

	def __init__(self, position: tuple[int, int]):
		super().__init__()

		self.position = self.pos_x, self.pos_y = position
		self.width, self.height = (6, 4)

		for y in range(self.height):
			for x in range(self.width):
				index = x * self.height + y
				texture = self.textures[index]

				sprite_pos = (
					self.pos_x + x * BLOCK_SIZE.width,
					self.pos_y + y * BLOCK_SIZE.height)
				size = BLOCK_SIZE.size
				design_element = MultiblockDesignElement(sprite_pos, size)
				design_element.image = texture

				self.add(design_element)

BLOCK_SYMBOLS = {
	# ' ': Grass,
	'#': Border,
	'H': Home,
}