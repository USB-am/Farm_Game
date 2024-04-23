from typing import Any

from exceptions import properties as Exc


class IntegerProperty:
	''' Положительное целое число '''

	def __set_name__(self, owner, name):
		self.public_name = name
		self.private_name = '_' + name

	def __get__(self, instance, name):
		return instance.__dict__.get(self.private_name, name)

	def __set__(self, instance, value):
		if value <= 0:
			raise Exc.EmptyError

		instance.__dict__[self.private_name] = value


class TypeProperty:
	''' Объект строго по заданному типу '''

	def __init__(self, obj_type: Any):
		self.obj_type = obj_type

	def __set_name__(self, owner, name):
		self.public_name = name
		self.private_name = '_' + name

	def __get__(self, instance, name):
		return instance.__dict__.get(self.private_name, name)

	def __set__(self, instance, value):
		if not isinstance(value, self.obj_type):
			raise AttributeError

		instance.__dict__[self.private_name] = value
