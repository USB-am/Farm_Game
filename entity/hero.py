from enum import Enum

from . import Entity
from item import Helmet, Armor, Bracers, Leggins, Boots
from properties import ItemProperty


class EquipTypes(Enum):
	helmet = Helmet
	armor = Armor
	bracers = Bracers
	leggins = Leggins
	boots = Boots


class Equipment:
	''' Экипировка Персонажа '''

	helmet = ItemProperty(EquipTypes.helmet.value)
	armor = ItemProperty(EquipTypes.armor.value)
	bracers = ItemProperty(EquipTypes.bracers.value)
	leggins = ItemProperty(EquipTypes.leggins.value)
	boots = ItemProperty(EquipTypes.boots.value)


class Hero(Entity):
	def __init__(self, name: str):
		self.name = name
		self.equipment = Equipment()

		super().__init__(hp=50, mp=50, endurance=50, damage=10)

	def __str__(self):
		return f'[{self.hp}] {self.name}'
