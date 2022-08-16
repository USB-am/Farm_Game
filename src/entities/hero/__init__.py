import time
from os import path, walk

import pygame

from .. import support, Entity
from config import BLOCK_SIZE, PLAYER_CONTROL, PLAYER_SIZE, CHARACTER_WALK_UP, \
	CHARACTER_WALK_LEFT, CHARACTER_WALK_DOWN, CHARACTER_WALK_RIGHT


class Hero(Entity):
	sprites = {
		'up':    support.get_sprites_from_folder(CHARACTER_WALK_UP,    PLAYER_SIZE),
		'left':  support.get_sprites_from_folder(CHARACTER_WALK_LEFT,  PLAYER_SIZE),
		'down':  support.get_sprites_from_folder(CHARACTER_WALK_DOWN,  PLAYER_SIZE),
		'right': support.get_sprites_from_folder(CHARACTER_WALK_RIGHT, PLAYER_SIZE)}

	def __init__(self, platforms: pygame.sprite.Group, position: tuple):
		super().__init__(position, BLOCK_SIZE.size)

		self.image = self.sprites['down'][0]

		self.platforms = platforms
		self.vec = pygame.Vector2((0, 0))
		self.move_speed = 5

		self.direction = 'down'
		self.last_animation = 0
		self._animation_count = 0

	@property
	def animation_count(self) -> int:
		return self._animation_count

	@animation_count.setter
	def animation_count(self, value: int) -> int:
		self._animation_count += 1

		self._animation_count = self._animation_count % len(
			self.sprites[self.direction])

	def update(self) -> None:
		self.check_events()

	def check_events(self) -> None:
		pressed = pygame.key.get_pressed()
		get_control = PLAYER_CONTROL.get

		up    = pressed[get_control('up',    False)]
		left  = pressed[get_control('left',  False)]
		down  = pressed[get_control('down',  False)]
		right = pressed[get_control('right', False)]
		run   = pressed[get_control('run',   False)]

		if any((up, left, down, right)):
			self.move(up, left, down, right, run)

			self.animation_count += 1

		self.animation()

	def move(self, up: bool, left: bool, down: bool, right: bool, run: bool=False) -> None:
		if up:
			self.vec.y = -self.move_speed
			self.direction = 'up'
		if left:
			self.vec.x = -self.move_speed
			self.direction = 'left'
		if down:
			self.vec.y = self.move_speed
			self.direction = 'down'
		if right:
			self.vec.x = self.move_speed
			self.direction = 'right'
		if run:
			self.vec.x *= 2
			self.vec.y *= 2

		self.rect.left += self.vec.x
		self.collide(self.vec.x, 0, self.platforms)
		self.rect.top  += self.vec.y
		self.collide(0, self.vec.y, self.platforms)

		if not (left or right):
			self.vec.x = 0
		if not (up or down):
			self.vec.y = 0

	def animation(self) -> None:
		now_time = time.time()

		if now_time - self.last_animation > .35:
			self.last_animation = now_time
			sprite = self.sprites[self.direction][self.animation_count]
			self.image = sprite

	def collide(self, xvec, yvec, blocks):
		for block in blocks:
			if pygame.sprite.collide_rect(self, block) and not block.fantom:
				if xvec > 0:
					self.rect.right = block.rect.left
				if xvec < 0:
					self.rect.left = block.rect.right
				if yvec > 0:
					self.rect.bottom = block.rect.top
				if yvec < 0:
					self.rect.top = block.rect.bottom