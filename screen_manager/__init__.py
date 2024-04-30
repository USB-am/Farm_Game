from . import exceptions as Exc
from .screen import Screen


class ScreenManager(dict):
	''' Менеджер экранов '''

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.active: str = Screen(name='')

	def add_screen(self, screen: Screen) -> None:
		''' Добавить экран '''

		if screen.name in self:
			raise Exc.ScreenManagerExistsError

		self[screen.name] = screen

	def move_to(self, screen_name: str) -> Screen:
		''' Перейти на экран '''

		if screen_name not in self:
			raise Exc.ScreenManagerExistsError

		self.active = self[screen_name]

		return self.active

	@property
	def current_screen(self) -> Screen:
		''' Возвращает текущий экран '''

		return self.active
