from typing import Type, Tuple, List

from model.item import Item
from model.exceptions import inventory as Exc


class InventoryCell(list):
	def __init__(self, obj_type: Type[Item]=None):
		self.obj_type = obj_type

	def append(self, element: Item) -> None:
		''' Добавить элемент в ячейку '''

		if self.obj_type is None:
			self.obj_type = type(element)

		if not isinstance(element, self.obj_type):
			raise Exc.InventoryElementTypeError(f'{element.__class__} type is not {self.obj_type}')

		super().append(element)

	def get(self, count: int) -> Tuple[Item]:
		if len(self) < count:
			raise Exc.InventoryElementCountError

		output = self[:count]
		[self.pop(0) for _ in range(count)]
		if not self:
			self.obj_type = None

		return output

	def is_empty(self) -> bool:
		return len(self) == 0


class Inventory(list):
	''' Инвентарь '''

	def __init__(self, size: int=10):
		self._size = size
		super().__init__(InventoryCell() for _ in range(self.size))

	@property
	def size(self) -> int:
		return self._size

	@size.setter
	def size(self, value: int) -> None:
		if value < self.length:
			raise Exc.InventoryOverSizeError

		self._size = value

	@property
	def length(self) -> int:
		''' Получить длину инвентаря '''
		return sum((1 for cell in self if not cell.is_empty()))

	def append(self, elem: Item) -> None:
		''' Добавить в инвентарь '''
		if self.length + 1 > self.size:
			raise Exc.InventoryFilledError

		for cell in self:
			try:
				cell.append(elem)
				break
			except Exc.InventoryElementTypeError:
				pass
		else:
			raise Exc.InventoryFilledError

	def __str__(self):
		return f'Inventory {self.length}/{self.size}'
