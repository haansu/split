import pygame as pg
from colors import Color

color = Color()

class Tile:
	def __init__(self):
		(self.width, self.height) = (50, 50)
		self.x = 0
		self.y = 0
		self.color = color.WHITE
		self.filled = False

	def draw(self, surface):
		pg.draw.rect(surface, self.color, pg.Rect(self.x, self.y, self.width, self.height))