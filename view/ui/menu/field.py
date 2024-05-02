import os
from typing import Callable

import pygame

from settings import FONT_NAME
from config.path import MENU_SPRITES_DIR


pygame.font.init()


_FONT = pygame.font.SysFont(FONT_NAME, 30)


class Button(pygame.sprite.Sprite):
	''' Кнопка '''

	def __init__(self, title: str, rect: pygame.Rect, *groups: pygame.sprite.Group):
		super().__init__(groups)
		path_img = os.path.join(MENU_SPRITES_DIR, 'button.png')
		self.title = title
		self.image = pygame.image.load(path_img).convert_alpha()
		self.rect = rect

		self.__callback = lambda *_: None
		self.text_surf = _FONT.render(self.title, False, (255, 255, 255))

	def bind(self, callback: Callable) -> None:
		''' Присвоить событие при клике '''
		self.__callback = callback

	def click(self) -> None:
		''' Вызвать событие при клике '''
		return self.__callback()

	def draw(self, surface: pygame.Surface) -> None:
		surface.blit(self.image, self.rect)
		text_center = (self.rect.center[0] - self.text_surf.get_width()  // 2,
		               self.rect.center[1] - self.text_surf.get_height() // 2)
		surface.blit(self.text_surf, text_center)
