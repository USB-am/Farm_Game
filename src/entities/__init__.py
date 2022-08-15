import pygame


class Entity(pygame.sprite.Sprite):
	def __init__(self, position: tuple, size: tuple):
		super().__init__()

		# setup
		self.image = pygame.Surface(size)
		self.image.fill('purple')
		self.rect = pygame.Rect(position, size)