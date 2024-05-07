import pygame

from screen_manager.screen import Screen
from view.entity.hero import Hero


class Game(Screen):
	''' Главный класс игры '''

	def __init__(self, **kwargs):
		super().__init__(name='game', **kwargs)

		self.hero = Hero(40, 40, (40, 40))

	def keydown_event(self, event) -> None:
		''' Обработка нажатия клавиши '''

		if event.key == pygame.K_w:
			self.hero.up = True
		if event.key == pygame.K_a:
			self.hero.left = True
		if event.key == pygame.K_s:
			self.hero.down = True
		if event.key == pygame.K_d:
			self.hero.right = True

	def keyup_event(self, event) -> None:
		''' Обработка отжатия клавиши '''

		if event.key == pygame.K_w:
			self.hero.up = False
		if event.key == pygame.K_a:
			self.hero.left = False
		if event.key == pygame.K_s:
			self.hero.down = False
		if event.key == pygame.K_d:
			self.hero.right = False

	def update(self) -> None:
		super().update()
		self.hero.update()

	def draw(self, surface: pygame.Surface) -> None:
		super().draw(surface)
		self.hero.draw(surface)
