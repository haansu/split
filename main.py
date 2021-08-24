import pygame as pg
import numpy as np
from game import Game
from colors import Color
from tiles import Tile

# Global Variables
game = Game()
color = Color()

# Logic matrix
tile_prefab = Tile()
logic_matrix = np.zeros_like([[Tile] * int(game.window.height / tile_prefab.height)] * int(game.window.width / tile_prefab.width), dtype = None)
# Why the fuck does python want me to declare a matrix like above??

for i in range(int(game.window.width / tile_prefab.width)):
	for j in range(int(game.window.height / tile_prefab.height)):
		logic_matrix[i][j] = Tile()
		logic_matrix[i][j].x = i * tile_prefab.width
		logic_matrix[i][j].y = j * tile_prefab.height

def main():
	game.window.set_background(color.DARKER_PURPLE)

	while game.running:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				game.running = False

		# Wall rendering
		for array in logic_matrix:
			for elem in array:
				pass

		pg.display.flip()			




if __name__ == '__main__':
	pg.init()
	main()
	pg.quit()
