import logging

from enemy import *


# Set logging level
logging.basicConfig(level=logging.INFO)


def main():
	es = [Goblin(hp=10) for i in range(10)]
	e1 = Hero(name='Hero')
	for e in es:
		e1.attack(e)


if __name__ == '__main__':
	main()
