from typing import Type, Tuple, List

from item import Item
from exceptions import inventory as Exc


class InventoryCell(list):
	def __init__(self, obj_type: Type[Item]=None):
		self.obj_type = obj_type

	def append(self, element: Item) -> None:
		''' Добавить элемент в ячейку '''

		if self.obj_type is None:
			self.obj_type = type(element)

		if not isinstance(element, self.obj_type):
			raise Exc.InventoryElementTypeError

		super().append(element)

	def __getitem__(self, count: int) -> Tuple[Item]:
		if len(self) < count:
			raise Exc.InventoryElementCountError

		output = self[:count]
		self = self[count:]
		return output

	def is_empty(self) -> bool:
		return len(self) == 0


class Inventory(list):
	''' Инвентарь '''

	def __init__(self, size: int=10):
		super().__init__()
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
