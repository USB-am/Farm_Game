import pygame

from config import SCREEN


class Camera(pygame.sprite.LayeredUpdates):
	def __init__(self, target: pygame.sprite.Sprite, world_size: pygame.Rect):
		super().__init__()

		self.target = target
		if self.target:
			self.add(self.target)
		self.world_size = world_size

		self.cam = pygame.Vector2((0, 0))

	def update(self):
		super().update()

		if self.target:
			x = -self.target.rect.center[0] + SCREEN.width  / 2
			y = -self.target.rect.center[1] + SCREEN.height / 2
			self.cam += (pygame.Vector2((x, y)) - self.cam) * .5
			self.cam.x = max(
				-(self.world_size.width - SCREEN.width),
				min(0, self.cam.x))
			self.cam.y = max(
				-(self.world_size.height - SCREEN.height),
				min(0, self.cam.y))

	def draw(self, parent):
		spritedict = self.spritedict
		parent_blit = parent.blit
		dirty = self.lostsprites
		self.lostsprites = []
		dirty_append = dirty.append
		init_rect = self._init_rect

		for sprite in self.sprites():
			rec = spritedict[sprite]
			newrect = parent_blit(sprite.image, sprite.rect.move(self.cam))

			if rec is init_rect:
				dirty_append(newrect)
			else:
				if newrect.colliderect(rec):
					dirty_append(newrect.union(rec))
				else:
					dirty_append(newrect)
					dirty_append(rec)

			spritedict[sprite] = newrect

		return dirty