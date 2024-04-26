from . import Creature
from .equipment import Equipment
from .inventory import Inventory
from item import Item

# Temp
from item.equipment import *
from item.tools import Shovel, Sword


class Hero(Creature):
	def __init__(self, name: str):
		self.name = name
		self.equipment = Equipment()
		self.inventory = Inventory()

		self.pick_up(Shovel(title='Super Shovel1'))
		self.inventory[0].get(count=1)[0]

		super().__init__(hp=50, endurance=50, damage=10)

	def pick_up(self, item: Item) -> None:
		self.inventory.append(item)

	def __str__(self):
		return f'[{self.hp}] {self.name}'
