import logging
from abc import ABC
from typing import TypeVar


TEnemy = TypeVar('TEnemy', bound='Enemy')


class EmptyError(Exception):
	pass


def attack_handler(func):
	def wrapper(cls, enemy):
		try:
			return func(cls, enemy)
		except EmptyError:
			enemy.kill()

	return wrapper


class IntegerProperty:
	def __set_name__(self, owner, name):
		self.public_name = name
		self.private_name = '_' + name

	def __get__(self, instance, name):
		return instance.__dict__.get(self.private_name, name)

	def __set__(self, instance, value):
		if value <= 0:
			raise EmptyError

		instance.__dict__[self.private_name] = value


class Enemy(ABC):
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
	def attack(self, enemy: TEnemy) -> None:
		''' Ударить enemy '''

		logging.info(f'{str(self)} caused {self.damage} damage to the {str(enemy)}')
		enemy.hp -= self.damage

	def kill(self) -> None:
		''' Убить '''

		del self


class Hero(Enemy):
	def __init__(self, name: str):
		super().__init__(hp=50, mp=50, endurance=50, damage=10)
		self.name = name

	def __str__(self):
		return f'[{self.hp}] {self.name}'


class Goblin(Enemy):
	def __str__(self):
		return f'[{self.hp}] Goblin'
