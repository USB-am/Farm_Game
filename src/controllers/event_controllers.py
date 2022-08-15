import pygame

from config import SCREEN
from src.entities.hero import Hero
from .camera import Camera


class EventController:
	is_worked = True
	platforms = pygame.sprite.Group()

	def __init__(self, root: pygame.Surface):
		self.root = root

		# setup
		self.map_ = pygame.Rect(0, 0, 1200, 800)	# temp
		self.hero = Hero(self.platforms, (100, 100))
		self.camera = Camera(self.hero, self.map_)
		self.platforms.add(self.hero)

	def check_event(self) -> None:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.is_worked = False
			if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
				self.is_worked = False

	def update(self) -> None:
		self.camera.update()
		# self.hero.update()

	def draw(self) -> None:
		# pygame.sprite.Group.draw(self.platforms, self.root)
		self.camera.draw(self.root)