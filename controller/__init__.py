import pygame


class _BaseController:
	''' Базовый событий приложения '''

	RUN: bool = True	# Main loop status

	def check_events(self) -> None:
		''' Проверка событий ввода '''

		for event in pygame.event.get():
			self.exit_event(event)
			self.keydown_event(event)
			self.keyup_event(event)
			self.mouse_event(event)

	def exit_event(self, event) -> None:
		''' События выхода '''

		if event.type == pygame.QUIT:
			self.RUN = False
		if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
			self.RUN = False

	def keydown_event(self, event) -> None:
		''' События нажатия клавиши '''

	def keyup_event(self, event) -> None:
		''' События отпускания клавиши '''

	def mouse_event(self, event) -> None:
		''' События мыши '''


class ApplicationController(_BaseController):
	''' Обработчик событий приложения '''
