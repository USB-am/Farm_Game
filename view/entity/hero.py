from . import Entity


class Hero(Entity):
	''' Персонаж '''

	MOVE_SPEED = 5

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

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

		if not any((self.up, self.down, self.left, self.right)):
			self.xvel = 0
			self.yvel = 0

		self.rect.x += self.xvel
		self.rect.y += self.yvel
