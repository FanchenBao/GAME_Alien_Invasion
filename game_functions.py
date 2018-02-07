import sys
import pygame
from bullet import Bullet
from alien import Alien

def fire_bullet(ai_settings, screen, ship, bullets):
	# fire a bullet if the limit is not reached yet
	if len(bullets) < ai_settings.bullet_allowed:
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)

def get_alien_per_row(ai_settings, alien_width):
	# determine how many aliens can fit in one row
	available_space_x = ai_settings.screen_width - alien_width * 2
	alien_per_row = int(available_space_x / (alien_width * 2))
	return(alien_per_row)

def get_row_per_screen(ai_settings, alien_height):
	# determine how many rows of aliens can fit in one screen
	available_space_y = ai_settings.screen_height - alien_height * 3
	row_per_screen = int(available_space_y / (alien_height * 2))
	return(row_per_screen)

def create_alien(screen, ai_settings, number_of_alien, number_of_row, aliens):
	alien = Alien(screen, ai_settings)
	# each new alien is positioned to the right of the previous one with one alien width of space in between
	alien.x = alien.rect.x + number_of_alien * alien.rect.width * 2
	alien_y = alien.rect.y + number_of_row * alien.rect.height * 2
	alien.rect.x = alien.x
	alien.rect.y = alien_y
	aliens.add(alien)


def create_alien_fleet(screen, ai_settings, aliens):
	# create a default alien which is NOT added to the alien fleet
	default_alien = Alien(screen, ai_settings)
	alien_per_row = get_alien_per_row(ai_settings, default_alien.rect.width)
	row_per_screen = get_row_per_screen(ai_settings, default_alien.rect.height)
	# create a full fleet
	for number_of_row in range(row_per_screen):
		for number_of_alien in range(alien_per_row):
			create_alien(screen, ai_settings, number_of_alien, number_of_row, aliens)

def change_fleet_direction(aliens, ai_settings):
	''' change fleet direction and move aliens down'''
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.alien_drop_speed
	ai_settings.fleet_direction *= -1	

def check_fleet_edges(aliens, ai_settings):
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(aliens, ai_settings)
			break

def update_aliens(aliens, ai_settings):
	'''Update current position of all aliens'''
	check_fleet_edges(aliens, ai_settings)
	aliens.update()

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
	

def update_screen(ai_settings, screen, ship, bullets, aliens):
	# redraw the scren during each pass of the loop
	screen.fill(ai_settings.background_color)
	# draw each bullet BEHIND the ship, so bullet drawn ahead of ship
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	aliens.draw(screen)
	# display the most recently drawn screen.
	pygame.display.flip()

def update_bullets(bullets):
	# update bullet position and delete extra bullets
	bullets.update()

	# delete bullets that have traveled outside the screen from the Group
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)