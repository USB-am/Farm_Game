import pygame

from tools.properties import StringProperty


class Screen(pygame.sprite.Group):
	''' Базовое представление экрана '''

	name = StringProperty()

	def __init__(self, name: str):
		super().__init__()
		self.name = name

	def check_events(self) -> None:
		''' Обработка событий '''

		for event in pygame.event.get():
			self.exit_event(event)

			if event.type == pygame.KEYDOWN: self.keydown_event(event)
			if event.type == pygame.KEYUP: self.keyup_event(event)
			if event.type == pygame.MOUSEMOTION: self.mouse_motion_event(event)
			if event.type == pygame.MOUSEBUTTONDOWN: self.mouse_down_event(event)
			if event.type == pygame.MOUSEBUTTONUP: self.mouse_up_event(event)

	def exit_event(self, event) -> None:
		''' Событие выхода '''

		if event.type == pygame.QUIT:
			exit()
		if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
			exit()

	def keydown_event(self, event) -> None:
		''' Событие нажатие кнопки '''

	def keyup_event(self, event) -> None:
		''' Событие отпускания кнопки '''

	def mouse_motion_event(self, event) -> None:
		''' Событие движения мыши '''

	def mouse_down_event(self, event) -> None:
		''' Событие нажатия мыши '''

	def mouse_up_event(self, event) -> None:
		''' Событие отпускания мыши '''

		for sprite in self:
			if sprite.rect.collidepoint(*event.pos):
				sprite.click()

	def __str__(self):
		return f'<Screen {self.name} ({len(self)})>'
