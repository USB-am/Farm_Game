from abc import ABC


class Item(ABC):
	def __init__(self, title: str):
		self.title = title

	def __str__(self):
		return f'Item "{self.title}"'


class Helmet(Item):
	pass


class Armor(Item):
	pass


class Bracers(Item):
	pass


class Leggins(Item):
	pass


class Boots(Item):
	pass