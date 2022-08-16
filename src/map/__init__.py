import os
from types import GeneratorType

import pygame

from config import BLOCK_SIZE
from . import blocks


class LevelReader:
	def __init__(self, path_to_level_file: str):
		if not os.path.exists(path_to_level_file):
			raise OSError(f'Level file "{path_to_level_file}" not found!')

		self.path_to_level_file = path_to_level_file

		self.symbols_width = 0
		self.symbols_height = 0

	def read(self) -> pygame.sprite.Group:
		output = pygame.sprite.Group()

		with open(self.path_to_level_file, mode='r') as level_file:
			file_text = level_file.read()
			self.size = self._get_size_from_string(file_text)
			[output.add(sprite) for sprite in self._string_to_sprites(file_text)]

		return output

	def get_size(self) -> tuple[int, int]:
		width, height = self.size
		pixel_size = (width * BLOCK_SIZE.width, height * BLOCK_SIZE.height)

		return pygame.Rect((0, 0), pixel_size)

	def _get_size_from_string(self, map_string: str) -> tuple[int, int]:
		enter_split_map = map_string.split('\n')
		size = (len(enter_split_map[0]), len(enter_split_map))

		return size

	def _string_to_sprites(self, map_string: str) -> pygame.sprite.Sprite:
		enter_split_map = map_string.split('\n')

		for y, row in enumerate(enter_split_map):
			for x, symbol in enumerate(row):
				sprite = blocks.BLOCK_SYMBOLS.get(symbol)

				if sprite is None:
					continue

				position = (x * BLOCK_SIZE.width, y * BLOCK_SIZE.height)
				yield sprite(position)


class Map(pygame.sprite.Group):
	def __init__(self, path_to_level_file: str):
		super().__init__()

		self.path_to_level_file = path_to_level_file
		self.size = pygame.Rect(0, 0, 100, 100)

	def load_map(self) -> None:
		self.empty()

		level_reader = LevelReader(self.path_to_level_file)
		self.add(level_reader.read())
		self.size = level_reader.get_size()