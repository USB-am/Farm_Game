from typing import List


class ScreenManager:
	''' Менеджер окон '''

	def __init__(self):
		self.__screens: List['Screen'] = []
		self.current_screen = None

	def add_screen(self, screen: 'Screen') -> None:
		if self.current_screen is None:
			self.current_screen = screen
		self.__screens.append(screen)
