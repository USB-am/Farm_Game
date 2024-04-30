import pygame

from tools.properties import StringProperty


class Screen(pygame.sprite.Group):
	''' Базовое представление экрана '''

	name = StringProperty()
