import pygame

from screen_manager.screen import Screen
from settings import SCREEN_SIZE
from view.entity.hero import Hero
from view.entity import Entity
from view.surroundings.elements import Stone
from .camera import Camera


def camera_configure(camera: Camera, target: Entity) -> pygame.Rect:
	''' Конфигурирование окна '''

	l, t = target.rect.topleft
	w, h = camera.rect.size
	l, t = -l + SCREEN_SIZE[0] / 2, -t + SCREEN_SIZE[1] / 2

	l = max(-(camera.rect.width  - SCREEN_SIZE[0]), l)
	t = max(-(camera.rect.height - SCREEN_SIZE[1]), t)
	l = min(0, l)
	t = min(0, t)

	return pygame.Rect(l, t, w, h)


class Game(Screen):
	''' Главный класс игры '''

	def __init__(self, **kwargs):
		super().__init__(name='game', **kwargs)

		self.target = Hero(40, 40, (40, 40), groups=self)

		# Temp
		self.add(Stone(120, 120))
		# self.add(Stone(120, 160))
		self.add(Stone(120, 200))

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
		super().update()
		self.target.update()

	def draw(self, surface: pygame.Surface) -> None:
		super().draw(surface)
		self.target.draw(surface)
