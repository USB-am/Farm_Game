import pygame

from . import Entity


class Hero(Entity):
	''' Персонаж '''

	MOVE_SPEED = 5

	def __init__(self, *args, groups=pygame.sprite.Group(), **kwargs):
		super().__init__(*args, **kwargs)
		self.groups = groups

		self.up = self.down = self.left = self.right = False

	def update(self) -> None:
		if self.up:
			self.yvel = -self.MOVE_SPEED
		if self.down:
			self.yvel = self.MOVE_SPEED
		if self.left:
			self.xvel = -self.MOVE_SPEED
		if self.right:
			self.xvel = self.MOVE_SPEED

		if not any((self.left, self.right)):
			self.xvel = 0
		if not any((self.up, self.down)):
			self.yvel = 0

		self.rect.left += self.xvel
		super()._check_collide(self.groups)
		self.rect.top  += self.yvel
		super()._check_collide(self.groups)
