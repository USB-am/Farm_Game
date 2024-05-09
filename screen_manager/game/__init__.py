import pygame

from screen_manager.screen import Screen
from settings import SCREEN_SIZE, BLOCK_SIZE
from view.entity.hero import Hero
from view.entity import Entity
from view.surroundings.elements import Stone
from .camera import Camera


def camera_configure(camera: Camera, target: Entity) -> pygame.Rect:
	''' Конфигурирование окна '''

	l, t = target.rect.topleft
	l, t = -l + SCREEN_SIZE[0] / 2, -t + SCREEN_SIZE[1] / 2

	l = min(0, l)
	l = max(-(camera.rect.width  - SCREEN_SIZE[0]), l)
	t = min(0, t)
	t = max(-(camera.rect.height - SCREEN_SIZE[1]), t)

	out = pygame.Rect(l, t, *camera.rect.size)
	print(out)
	return out


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

		self.target = Hero(200, 200, (40, 40), groups=self)
		level_width = len(LEVEL[0]) * BLOCK_SIZE[0]
		level_height = len(LEVEL) * BLOCK_SIZE[1]
		self.camera = Camera(camera_configure, level_width, level_height)
		self.add(self.target)

		# Temp
		for row, _ in enumerate(LEVEL):
			for col, simbol in enumerate(_):
				if simbol == '#':
					self.add(Stone(col * BLOCK_SIZE[0], row * BLOCK_SIZE[1]))
		# self.add(Stone(120, 120))
		# self.add(Stone(120, 160))
		# self.add(Stone(120, 200))

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
		# super().update()
		self.camera.update(self.target)
		self.target.update()

	def draw(self, surface: pygame.Surface) -> None:
		for sprite in self:
			surface.blit(sprite.image, self.camera.apply(sprite))
		# self.target.draw(surface)
