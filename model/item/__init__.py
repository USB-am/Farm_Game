from abc import ABC


class Item(ABC):
	def __init__(self, title: str, **kwargs):
		self.title = title

	def __str__(self):
		return f'Item "{self.title}"'
