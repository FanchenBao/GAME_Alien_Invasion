import sys
import pygame

def check_events(ship):
	# an event loop to monitor user's input (press key or move mouse)
	# The one below checks whether user clicks to close the program.
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		# check whether the event is a key press
		elif event.type == pygame.KEYDOWN:
			# check whether the key press is the right arrow key
			if event.key == pygame.K_RIGHT:
				# set the moving flag to true so that ship continues moving right
				ship.moving_right = True
			elif event.key == pygame.K_LEFT:
				# set the moving flag to true so that ship continues moving left
				ship.moving_left = True
		
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
			# set the moving flag to false so that ship stops moving when right arrow key is released
				ship.moving_right = False
			elif event.key == pygame.K_LEFT:
			# set the moving flag to false so that ship stops moving when left arrow key is released
				ship.moving_left = False
	

def update_screen(ai_settings, screen, ship):
	# redraw the scren during each pass of the loop
	screen.fill(ai_settings.background_color)
	ship.blitme()

	# display the most recently drawn screen.
	pygame.display.flip()