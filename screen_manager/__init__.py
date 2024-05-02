from . import exceptions as Exc
from .screen import Screen


class ScreenManager(dict):
	''' Менеджер экранов '''

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.__active: str = Screen(name='')

	def add_screen(self, screen: Screen) -> None:
		''' Добавить экран '''

		if screen.name in self:
			raise Exc.ScreenManagerExistsError

		self[screen.name] = screen
		self.__active = screen

	def move_to(self, screen_name: str) -> Screen:
		''' Перейти на экран '''

		if screen_name not in self:
			raise Exc.ScreenManagerExistsError

		self.__active = self[screen_name]

		return self.__active

	@property
	def current_screen(self) -> Screen:
		''' Возвращает текущий экран '''

		return self.__active
