from abc import ABC

from item import Item
from properties import NumberProperty, IntegerProperty


class BaseEquipment(Item):
	''' Базовое представление экипировки '''

	hp = NumberProperty(0)
	endurance = NumberProperty(0)
	damage = NumberProperty(0)
	integrity = NumberProperty(0)

	def __init__(self, title: str, hp: int=0, endurance: int=0, damage: int=0, integrity: int=0):
		super().__init__(title=title)

		self.hp = hp
		self.endurance = endurance
		self.damage = damage
		self.integrity = integrity


class Helmet(BaseEquipment):
	pass


class Armor(BaseEquipment):
	pass


class Bracers(BaseEquipment):
	pass


class Leggins(BaseEquipment):
	pass


class Boots(BaseEquipment):
	pass
