import pygame

from .. import Entity
from config import BLOCK_SIZE, PLAYER_CONTROL


class Hero(Entity):
	def __init__(self, platforms: pygame.sprite.Group, position: tuple):
		size = (int(BLOCK_SIZE.width  * 1.2),
		        int(BLOCK_SIZE.height * 1.2))

		super().__init__(position, size)

		self.platforms = platforms
		self.vec = pygame.Vector2((0, 0))
		self.move_speed = 3

	def update(self) -> None:
		self.check_events()

	def draw(self, *args) -> None:
		print(f'Hero.draw has args={args}')

	def check_events(self) -> None:
		pressed = pygame.key.get_pressed()
		get_control = PLAYER_CONTROL.get

		up    = pressed[get_control('up',    False)]
		left  = pressed[get_control('left',  False)]
		down  = pressed[get_control('down',  False)]
		right = pressed[get_control('right', False)]

		if any((up, left, down, right)):
			self.move(up, left, down, right)
		else:
			self.vec.x = 0
			self.vec.y = 0

	def move(self, up: bool, left: bool, down: bool, right: bool) -> None:
		if up:
			self.vec.y = self.move_speed
		if left:
			self.vec.x = self.move_speed
		if down:
			self.vec.y = -self.move_speed
		if right:
			self.vec.x = -self.move_speed

		self.rect.left += self.vec.x
		self.collide(self.vec.x, 0, self.platforms)
		self.rect.top  += self.vec.y
		self.collide(0, self.vec.y, self.platforms)

	def collide(self, xvec, yvec, blocks):
		for block in blocks:
			if pygame.sprite.collide_rect(self, block):
				if xvec > 0:
					self.rect.right = block.rect.left
				if xvec < 0:
					self.rect.left = block.rect.right
				if yvec > 0:
					self.rect.bottom = block.rect.top
				if yvec < 0:
					self.rect.top = block.rect.bottom