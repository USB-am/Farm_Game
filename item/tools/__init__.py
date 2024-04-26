from abc import ABC

from item import Item
from properties import NumberProperty


class BaseTool(Item):
	''' Базовое представление инструмента '''


class Sword(BaseTool):
	''' Меч '''

	damage = NumberProperty(0)


class Shovel(BaseTool):
	''' Лопата '''
