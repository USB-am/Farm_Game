import pygame

from screen_manager.screen import Screen
from settings import SCREEN_SIZE, BLOCK_SIZE
from view.entity.hero import Hero
from view.entity import Entity
from view.surroundings.elements import Stone
from .camera import Camera


LEVEL = [
	'##################################',
	'#                                #',
	'#                                #',
	'#                                #',
	'#                                #',
	'#                                #',
	'#                                #',
	'#                                #',
	'#                                #',
	'#                                #',
	'#                                #',
	'#                                #',
	'#                                #',
	'#                                #',
	'#                                #',
	'#                                #',
	'#                                #',
	'#                                #',
	'#                                #',
	'#                                #',
	'#                                #',
	'#                                #',
	'#  #### # #   #                  #',
	'#  #      ##  #                  #',
	'#  ###  # # # #                  #',
	'#  #    # #  ##                  #',
	'#  #    # #   #                  #',
	'#                                #',
	'##################################',
]


class Game(Screen):
	''' Главный класс игры '''

	def __init__(self, **kwargs):
		super().__init__(name='game', **kwargs)

		self.target = Hero(200, 200, (30, 30), groups=self)
		level_width = len(LEVEL[0]) * BLOCK_SIZE[0]
		level_height = len(LEVEL) * BLOCK_SIZE[1]
		self.camera = Camera(level_width, level_height)
		self.add(self.target)

		# Temp
		for row, _ in enumerate(LEVEL):
			for col, simbol in enumerate(_):
				if simbol == '#':
					self.add(Stone(col * BLOCK_SIZE[0], row * BLOCK_SIZE[1]))

	def keydown_event(self, event) -> None:
		''' Обработка нажатия клавиши '''

		if event.key == pygame.K_w:
			self.target.up = True
		if event.key == pygame.K_a:
			self.target.left = True
		if event.key == pygame.K_s:
			self.target.down = True
		if event.key == pygame.K_d:
			self.target.right = True

	def keyup_event(self, event) -> None:
		''' Обработка отжатия клавиши '''

		if event.key == pygame.K_w:
			self.target.up = False
		if event.key == pygame.K_s:
			self.target.down = False
		if event.key == pygame.K_a:
			self.target.left = False
		if event.key == pygame.K_d:
			self.target.right = False

	def update(self) -> None:
		self.camera.update(self.target)
		self.target.update()

	def draw(self, surface: pygame.Surface) -> None:
		for sprite in self:
			surface.blit(sprite.image, self.camera.apply(sprite))
