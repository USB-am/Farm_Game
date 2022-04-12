# -*- coding: utf-8 -*-

import unittest

import pygame

from bin.objects import hero, peaceful_enemy, enemy
import settings as Settings


def main():
	sprites = pygame.sprite.Group()
	hero_ = hero.Hero(rect=pygame.Rect(2, 3, 1, 1))
	sprites.add(
		enemy.Goblin(health=50),
		peaceful_enemy.PeacefulEnemy(health=10, rect=pygame.Rect(4, 3, 2, 2)),
		hero_
	)

	screen = pygame.display.set_mode(Settings.SCREEN.size)
	pygame.display.set_caption('Stardew Valley')
	timer = pygame.time.Clock()
	run = True

	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
				run = False

			if event.type == pygame.KEYDOWN:
				if event.key in Settings.PLAYER_MANAGER.keys():
					hero_.update(Settings.PLAYER_MANAGER[event.key])
				if event.key == pygame.K_SPACE:
					hero_.attack([s for s in sprites][0])

		screen.fill((255, 255, 255))

		sprites.draw(screen)

		pygame.display.update()
		timer.tick(60)


if __name__ == '__main__':
	main()