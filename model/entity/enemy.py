from . import Entity


class Goblin(Entity):
	def __str__(self):
		return f'[{self.hp}] Goblin'
