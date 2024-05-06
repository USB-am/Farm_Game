class PathManager(list):
	''' Менеджер путей по экранам '''

	def __init__(self, screen_manager: 'ScreenManager'):
		self.__screen_manager = screen_manager

	def forward(self, screen_name: str) -> 'Screen':
		''' Перейти к экрану с названием screen_name '''

		self.__screen_manager.move_to(screen_name)
		self.append(screen_name)

		return self.__screen_manager.current_screen

	def back(self) -> None:
		''' Вернуться на экран назад '''

		self.pop(-1)

		screen_name = self[-1].name
		self.__screen_manager.move_to(screen_name)

		return self.__screen_manager.current_screen
