import	pygame as pg
from	colors import Color

color = Color()

class Ball:
	def __init__(self):
		self.x = 0.0
		self.y = 0.0
		self.rad = 20
		self.color = color.CYAN

	def draw(self, surface):
		pg.draw.circle(surface, self.color, (self.x, self.y), self.rad)