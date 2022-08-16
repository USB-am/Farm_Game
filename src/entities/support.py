import os

import pygame

from config import BLOCK_SIZE


def find_files(folder: str) -> list[str,]:
	base_dir, _, files = list(os.walk(folder))[0]
	result = [os.path.join(base_dir, file) for file in files]

	return result


def get_sprites_from_folder(folder: str, block_size: tuple[int, int]) -> list:
	files = find_files(folder)
	result = []

	for file in files:
		image = pygame.image.load(file)
		image = pygame.transform.scale(image, block_size)

		result.append(image)

	return result