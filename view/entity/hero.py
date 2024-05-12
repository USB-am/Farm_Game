import pygame

from . import Entity


class Hero(Entity):
	''' Персонаж '''

	MOVE_SPEED = 5

	def __init__(self, *args, groups=pygame.sprite.Group(), **kwargs):
		super().__init__(*args, **kwargs)
		self.groups = groups

		self.up = self.down = self.left = self.right = False
		self.direction = 'right'

	def update(self) -> None:
		if self.left:
			self.xvel = -self.MOVE_SPEED
		if self.right:
			self.xvel = self.MOVE_SPEED
		if self.up:
			self.yvel = -self.MOVE_SPEED
		if self.down:
			self.yvel = self.MOVE_SPEED

		if not any((self.left, self.right)):
			self.xvel = 0
		if not any((self.up, self.down)):
			self.yvel = 0

		self.rect.x += self.xvel
		super()._check_collide(self.groups)
		self.rect.y  += self.yvel
		super()._check_collide(self.groups)

		self.update_image()

	def collide(self, *a, **kw) -> bool:
		return False

	def update_image(self) -> None:
		if self.left:
			self.direction = 'left'
			self.image.fill(pygame.Color('green'))
		if self.right:
			self.direction = 'right'
			self.image.fill(pygame.Color('white'))
		if self.up:
			self.direction = 'up'
			self.image.fill(pygame.Color('blue'))
		if self.down:
			self.direction = 'down'
			self.image.fill(pygame.Color('red'))

	def draw(self, surface: pygame.Surface) -> None:
		surface.blit(self.image, (self.rect.x, self.rect.y))
