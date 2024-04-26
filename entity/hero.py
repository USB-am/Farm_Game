from . import Creature
from .equipment import Equipment
from .inventory import Inventory
from item.equipment import *


class Hero(Creature):
	def __init__(self, name: str):
		self.name = name
		self.equipment = Equipment()
		self.inventory = Inventory()
		self.inventory.append(Helmet(title='Super Helmet1', integrity=10, hp=10))
		self.inventory.append(Helmet(title='Super Helmet2'))
		self.inventory[0].get(count=1)[0]

		super().__init__(hp=50, endurance=50, damage=10)

	def __str__(self):
		return f'[{self.hp}] {self.name}'
