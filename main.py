import logging

from entity.hero import Hero
from entity.enemy import Goblin


# Set logging level
logging.basicConfig(level=logging.DEBUG)


def main():
	h = Hero(name='Hero')
	goblins = [Goblin(hp=10) for i in range(10)]

	for goblin in goblins:
		h.attack(goblin)


if __name__ == '__main__':
	main()
