import unittest

from entity.inventory import Inventory, InventoryCell
from item.equipment import Helmet
from exceptions import inventory as ExcInventory


class TestInventory(unittest.TestCase):
	''' Тесты инвентаря '''

	@classmethod
	def setUpClass(cls):
		cls.inventory = Inventory(size=3)

	def setUp(self):
		self.inventory.size = 3

	def test_resize(self):
		self.inventory.size = 10
		# self.assertEqual(len(self.inventory), 10)
		self.assertEqual(self.inventory.size, 10)

		self.inventory.size = 5
		# self.assertEqual(len(self.inventory), 5)
		self.assertEqual(self.inventory.size, 5)

	def test_append(self):
		helmet = Helmet(title='Test helmet')

		self.inventory.append(helmet)
		self.assertEqual(self.inventory.length, 1)

		received_helmet = self.inventory[0].get(count=1)[0]
		self.assertIs(received_helmet, helmet)
		self.assertEqual(self.inventory.length, 0)

		with self.assertRaises(ExcInventory.InventoryElementCountError):
			self.inventory[0].get(count=1)
