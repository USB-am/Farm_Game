import logging
from abc import ABC
from typing import List, TypeVar

from properties import IntegerProperty
from item import Item
from exceptions import properties as Exc


TEntity = TypeVar('TEntity', bound='Entity')


def attack_handler(func):
	def wrapper(cls, entity):
		try:
			return func(cls, entity)
		except Exc.EmptyError:
			entity.kill()

	return wrapper


class Entity(ABC):
	hp = IntegerProperty()
	mp = IntegerProperty()
	endurance = IntegerProperty()
	damage = IntegerProperty()

	def __init__(self, hp: int=1, mp: int=1, endurance: int=1, damage: int=1):
		self.hp = hp
		self.mp = mp
		self.endurance = endurance
		self.damage = damage

	@attack_handler
	def attack(self, entity: TEntity) -> None:
		''' Ударить entity '''

		# logging.info(f'{str(self)} caused {self.damage} damage to the {str(entity)}')
		entity.hp -= self.damage

	def kill(self) -> None:
		''' Убить '''

		# logging.info(f'{str(self)} is dead!')
		del self
