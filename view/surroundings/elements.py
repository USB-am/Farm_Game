from . import Object, FantomObject
# from config import 


class Stone(Object):
	''' Камень '''

	def __init__(self, x: int, y: int):
		super().__init__(x, y)
