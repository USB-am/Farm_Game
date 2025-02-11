import pygame as pg

import settings
from screens.screen_manager import ScreenManager
from screens.game import GameScreen


pg.init()
pg.font.init()


fps_font = pg.font.SysFont('Consolas', 20)


class Application:
	def __init__(self):
		self.window = pg.display.set_mode(settings.SCREEN_SIZE)
		pg.display.set_caption('Farm Game: v0.2')

		self.screen_manager = ScreenManager()
		self.screen_manager.add_screen(GameScreen())

		self.timer = pg.time.Clock()

	def run(self) -> None:
		RUN = True

		while RUN:
			self.window.fill('black')

			self.screen_manager.current_screen.check_event()
			self.screen_manager.current_screen.update()
			self.screen_manager.current_screen.draw(self.window)

			fps_text = fps_font.render(f'FPS: {int(self.timer.get_fps())}', False, 'orange')
			self.window.blit(fps_text, (0, 0))

			pg.display.flip()
			self.timer.tick(settings.MAX_FPS)
