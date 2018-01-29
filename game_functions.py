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
				# move ship to the right
				ship.rect.centerx += 1
			elif event.key == pygame.K_LEFT:
				# move ship to the left
				ship.rect.centerx -= 1

def update_screen(ai_settings, screen, ship):
	# redraw the scren during each pass of the loop
	screen.fill(ai_settings.background_color)
	ship.blitme()

	# display the most recently drawn screen.
	pygame.display.flip()