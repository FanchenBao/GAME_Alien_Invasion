import sys

import pygame

from settings import Settings

def run_game():
	# initialize game and create a screen object.
	
	# initialize game
	pygame.init()

	# create game display with 1200 pixels wide and 800 pixels in height
	ai_setting = Settings()
	screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
	pygame.display.set_caption("Alien Invasion")

	# set background color
	background_color = ai_setting.background_color

	# The main loop of the game
	while True:

		# an event loop to monitor user's input (press key or move mouse)
		# The one below checks whether user clicks to close the program.
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		# redraw the scren during each pass of the loop
		screen.fill(background_color)

		# display the most recently drawn screen.
		pygame.display.flip()


run_game()