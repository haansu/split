import pygame as pg

class Window:
	def __new__(cls):
		if not hasattr(cls, 'instance'):
			cls.instance = super(Window, cls).__new__(cls)
		return cls.instance

	def __init__(self):
		(self.width, self.height) = (1000, 500)
		self.title = "Split"

		pg.display.set_caption(self.title)
		self.screen = pg.display.set_mode((self.width, self.height))

	def set_title(self, title):
		self.title = title
		pg.display.set_caption(self.title)

	def set_background(self, color):
		self.screen.fill(color)
		pg.display.flip()
		

class Game:
	def __new__(cls):
		if not hasattr(cls, 'instance'):
			cls.instance = super(Game, cls).__new__(cls)
		return cls.instance

	def __init__(self):
		self.running = True
		self.window = Window()
		
		
	
