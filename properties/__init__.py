from abc import ABC, abstractclassmethod
from typing import Any

from exceptions import properties as Exc


class _Property(ABC):
	''' Шаблон '''

	def __set_name__(self, owner, name):
		self.public_name = name
		self.private_name = '_' + name

	def __get__(self, instance, name):
		return instance.__dict__.get(self.private_name, name)

	@abstractclassmethod
	def __set__(self, instance, value):
		pass


class NumberProperty(_Property):
	''' Целое число '''

	def __init__(self, value: int=0):
		super().__init__()
		self.value = value

	def __set__(self, instance, value):
		if not isinstance(value, int):
			raise AttributeError

		self.value = value
		instance.__dict__[self.private_name] = self.value


class IntegerProperty(_Property):
	''' Положительное целое число '''

	def __set__(self, instance, value):
		if value <= 0:
			raise Exc.EmptyError

		instance.__dict__[self.private_name] = value


class TypeProperty(_Property):
	''' Объект строго по заданному типу '''

	def __init__(self, obj_type: Any):
		super().__init__()

		self.obj_type = obj_type

	def __set__(self, instance, value):
		if not isinstance(value, self.obj_type):
			raise AttributeError

		instance.__dict__[self.private_name] = value
