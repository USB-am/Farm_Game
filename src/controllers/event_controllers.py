import os

import pygame

from config import SCREEN, LEVELS_DIR
from src.entities.hero import Hero
from src.map import Map
from .camera import Camera


class EventController:
	is_worked = True
	platforms = pygame.sprite.Group()

	def __init__(self, root: pygame.Surface):
		self.root = root

		# setup
		path_to_first_level = os.path.join(LEVELS_DIR, 'level_0.txt')
		self.map_ = Map(path_to_first_level)
		self.map_.load_map()

		self.hero = Hero(self.platforms, (100, 100))
		self.platforms.add(self.hero)
		self.camera = Camera(self.hero, self.map_.size)
		self.platforms.add(self.map_)
		self.camera.add(self.map_)

	def check_event(self) -> None:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.is_worked = False
			if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
				self.is_worked = False

	def update(self) -> None:
		self.map_.update()
		self.camera.update()

	def draw(self) -> None:
		# pygame.sprite.Group.draw(self.platforms, self.root)
		self.camera.draw(self.root)
		# pygame.sprite.Group.draw(self.map_, self.root)