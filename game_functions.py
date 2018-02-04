import sys
import pygame
from bullet import Bullet

def fire_bullet(ai_settings, screen, ship, bullets):
	# fire a bullet if the limit is not reached yet
	if len(bullets) < ai_settings.bullet_allowed:
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)

def check_key_down_event(event, ai_settings, screen, ship, bullets):
	# determine action when key is pushed down
	if event.key == pygame.K_RIGHT:
		# set the moving flag to true so that ship continues moving right
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		# set the moving flag to true so that ship continues moving left
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		# create new bullet each time spacebar is pressed
		fire_bullet(ai_settings, screen, ship, bullets)
	elif event.key == pygame.K_q:
		sys.exit()

def check_key_up_event(event, ship):
	# determine action when key is released
	if event.key == pygame.K_RIGHT:
	# set the moving flag to false so that ship stops moving when right arrow key is released
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
	# set the moving flag to false so that ship stops moving when left arrow key is released
		ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
	# an event loop to monitor user's input (press key or move mouse)
	# The one below checks whether user clicks to close the program.
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		# check whether the event is a key press
		elif event.type == pygame.KEYDOWN:
			check_key_down_event(event, ai_settings, screen, ship, bullets)
		elif event.type == pygame.KEYUP:
			check_key_up_event(event, ship)
	

def update_screen(ai_settings, screen, ship, bullets):
	# redraw the scren during each pass of the loop
	screen.fill(ai_settings.background_color)
	# draw each bullet BEHIND the ship, so bullet drawn ahead of ship
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	# display the most recently drawn screen.
	pygame.display.flip()

def update_bullets(bullets):
	# update bullet position and delete extra bullets
	bullets.update()

	# delete bullets that have traveled outside the screen from the Group
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)