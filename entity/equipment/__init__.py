from enum import Enum

from item import Item
from item.equipment import Helmet, Armor, Bracers, Leggins, Boots
from properties import TypeProperty


class EquipTypes(Enum):
	helmet = Helmet
	armor = Armor
	bracers = Bracers
	leggins = Leggins
	boots = Boots


class Equipment:
	''' Экипировка Персонажа '''

	helmet = TypeProperty(EquipTypes.helmet.value)
	armor = TypeProperty(EquipTypes.armor.value)
	bracers = TypeProperty(EquipTypes.bracers.value)
	leggins = TypeProperty(EquipTypes.leggins.value)
	boots = TypeProperty(EquipTypes.boots.value)

	def equip(self, item: Item) -> None:
		''' Экипировать '''

		# TODO: Change this
		if isinstance(item, EquipTypes.helmet.value):
			self.helmet = item
		elif isinstance(item, EquipTypes.armor.value):
			self.armor = item
		elif isinstance(item, EquipTypes.bracers.value):
			self.bracers = item
		elif isinstance(item, EquipTypes.leggins.value):
			self.leggins = item
		elif isinstance(item, EquipTypes.boots.value):
			self.boots = item