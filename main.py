import	pygame 	as pg
import	numpy 	as np
import	copy
from 	game 	import Game
from 	colors 	import Color
from 	tiles 	import Tile
from	ball	import Ball

# Global Variables
game 			= Game()
color 			= Color()
ball			= Ball()
velocity		= 3


# Logic matrix
tile_prefab 	= Tile()
logic_width		= int(game.window.width / tile_prefab.width)
logic_height 	= int(game.window.height / tile_prefab.height)
logic_matrix 	= np.zeros_like([[Tile] * logic_height] * logic_width, dtype = None)
# Why the fuck does python want me to declare a matrix like above??

# Clock
clock			= pg.time.Clock()

def main():
	game.window.set_background(color.DARKER_PURPLE)

	# Ball configure
	ball.x = game.window.width / 2
	ball.y = game.window.height / 2


	speed_x = 1
	speed_y = 1
	direction_x = speed_x * velocity
	direction_y = speed_y * velocity

	# Initialising the logic matrix
	for i in range(logic_width):
		for j in range(logic_height):
			logic_matrix[i][j]   = copy.deepcopy(tile_prefab)
			logic_matrix[i][j].x = i * tile_prefab.width
			logic_matrix[i][j].y = j * tile_prefab.height

	# Setting default drawn tiles
	for i in range(logic_width):
		logic_matrix[i][0].filled = True
		logic_matrix[i][logic_height - 1].filled = True

	for i in range(logic_height):
		logic_matrix[0][i].filled = True
		logic_matrix[logic_width - 1][i].filled = True

	split_counter = 1

	split_vertical		= False
	split_horizontal	= False

	# Defines skipped frames until new tile is drawn
	skipper = 5
	in_skipper = skipper

	# Logic matrix inddices from mouse position
	idx_x = 0
	idx_y = 0

	# Game loop
	while game.running:
		game.window.fill(color.DARKER_PURPLE)
		# Checking events
		for event in pg.event.get():
			if event.type == pg.QUIT:
				game.running = False
			if event.type == pg.MOUSEBUTTONUP:
				(pos_x, pos_y) = pg.mouse.get_pos()

				# Transforms mouse position into logic matrix indices
				if split_vertical == False and split_horizontal == False:
					idx_y = int(pos_y / tile_prefab.height)
					idx_x = int(pos_x / tile_prefab.width)

					# Vertical split
					if event.button == 1:
						if logic_matrix[idx_x][idx_y].filled == False:
							split_vertical = True
							logic_matrix[idx_x][idx_y].filled = True

					# Horizontal split split
					if event.button == 3:
						if logic_matrix[idx_x][idx_y].filled == False:
							split_horizontal = True
							logic_matrix[idx_x][idx_y].filled = True

		if split_vertical or split_horizontal:
			skipper -= 1

		if split_vertical and skipper == 1:
			if idx_y + split_counter < logic_height - 1:
				logic_matrix[idx_x][idx_y + split_counter].filled = True

			if idx_y - split_counter > 0:
				logic_matrix[idx_x][idx_y - split_counter].filled = True
			
			if split_counter + idx_y > logic_height - 1 and idx_y - split_counter <= 0:
				split_counter = 0
				split_vertical = False

			split_counter += 1

			if skipper == 1:
				skipper = in_skipper

		
		if split_horizontal and skipper == 1:
			if idx_x + split_counter < logic_width - 1:
				logic_matrix[idx_x + split_counter][idx_y].filled = True

			if idx_x - split_counter > 0:
				logic_matrix[idx_x - split_counter][idx_y].filled = True

			if split_counter + idx_x > logic_width - 1 and idx_x - split_counter <= 0:
				split_counter = 0
				split_horizontal = False

			split_counter += 1

			if skipper == 1:
				skipper = in_skipper

		for array in logic_matrix:
			for elem in array:
				if elem.filled:
					elem.draw(game.window.screen)


		# Ball logic
		ball.x = ball.x + direction_x
		ball.y = ball.y + direction_y
		
		ball_up		= ball.y - ball.rad
		ball_down	= ball.y + ball.rad
		ball_left	= ball.x - ball.rad
		ball_right	= ball.x + ball.rad

		if direction_x > 0 and logic_matrix[int(ball_right / tile_prefab.width)][int(ball.y / tile_prefab.height)].hovered(ball_right, ball.y) and logic_matrix[int(ball_right / tile_prefab.width)][int(ball.y / tile_prefab.height)].filled == True:
			direction_x *= -1

		if direction_x < 0 and logic_matrix[int(ball_left / tile_prefab.width)][int(ball.y / tile_prefab.height)].hovered(ball_left, ball.y) and logic_matrix[int(ball_left / tile_prefab.width)][int(ball.y / tile_prefab.height)].filled == True:
			direction_x *= -1

		if direction_y > 0 and logic_matrix[int(ball.x / tile_prefab.width)][int(ball_down / tile_prefab.height)].hovered(ball.x, ball_down) and logic_matrix[int(ball.x / tile_prefab.width)][int(ball_down / tile_prefab.height)].filled == True:
			direction_y *= -1

		if direction_y < 0 and logic_matrix[int(ball.x / tile_prefab.width)][int(ball_up / tile_prefab.height)].hovered(ball.x, ball_up) and logic_matrix[int(ball.x / tile_prefab.width)][int(ball_up / tile_prefab.height)].filled == True:
			direction_y *= -1


		ball.draw(game.window.screen)
		pg.display.flip()
		clock.tick(60)

if __name__ == '__main__':
	pg.init()
	main()
	pg.quit()
