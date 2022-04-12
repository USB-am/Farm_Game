# -*- coding: utf-8 -*-

import unittest
from bin.objects.hero import Hero


class TestHero(unittest.TestCase):
	def test_kill(self):
		hero_1 = Hero()
		hero_2 = Hero(health=1)

		hero_1.attack(hero_2)

		self.assertEqual(hero_2.is_kill(), True)

	def test_attack(self):
		start_health = 100

		hero_1 = Hero()
		hero_2 = Hero(health=start_health)

		hero_1.attack(hero_2)

		self.assertEqual(hero_2.health.value, start_health - hero_1.ATTACK_DAMAGE)

unittest.main()