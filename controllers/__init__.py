from models.menu import MenuModel
from views.menu import MenuView


class BaseController:
	''' Базовый контроллер '''

	def __init__(self, screen):
		self._screen = screen
		self._model = MenuModel(screen)	# Started model
		self._view = MenuView(screen)	# Started view

		self.RUN = True	# Mail loop status

	def check_events(self) -> None:
		pass


class Controller:
	def __init__(self, screen):
		pass