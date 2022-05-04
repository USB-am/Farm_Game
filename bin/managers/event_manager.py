# -*- coding: utf-8 -*-

import pygame


class EventManager:
	def check_events(self) -> pygame.event:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
			if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
				exit()

			if event.type == pygame.KEYDOWN:
				return event

		return