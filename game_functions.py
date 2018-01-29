import sys
import pygame

def check_events():
	# an event loop to monitor user's input (press key or move mouse)
	# The one below checks whether user clicks to close the program.
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

def update_screen(ai_settings, screen, ship):
	# redraw the scren during each pass of the loop
	screen.fill(ai_settings.background_color)
	ship.blitme()

	# display the most recently drawn screen.
	pygame.display.flip()