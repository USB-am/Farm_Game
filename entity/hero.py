from . import Entity
from .equipment import Equipment
from .inventory import Inventory
from item import *


class Hero(Entity):
	def __init__(self, name: str):
		self.name = name
		self.equipment = Equipment()
		self.inventory = Inventory()
		self.inventory.append(Helmet(title='Super Helmet'))
		print(self.inventory)

		super().__init__(hp=50, mp=50, endurance=50, damage=10)

	def __str__(self):
		return f'[{self.hp}] {self.name}'
