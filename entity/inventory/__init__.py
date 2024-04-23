from item import Item
from exceptions import inventory as Exc


class Inventory(list):
	''' Инвентарь '''

	def __init__(self, *elements: Item, size: int=10):
		super().__init__(elements)
		self._size = size

	@property
	def size(self) -> int:
		return self._size

	@size.setter
	def size(self, value: int) -> None:
		if value < len(self):
			raise Exc.InventoryOverSizeError

		self._size = value

	def append(self, elem: Item) -> None:
		if len(self) + 1 > self.size:
			raise Exc.InventoryFilledError

		super().append(elem)

	def __str__(self):
		return f'Inventory {len(self)}/{self.size}'
