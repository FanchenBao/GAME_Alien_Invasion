import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

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

def get_row_per_screen(ai_settings, alien_height, ship_height):
	# determine how many rows of aliens can fit in one screen
	available_space_y = ai_settings.screen_height - alien_height * 3 - ship_height
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


def create_alien_fleet(screen, ai_settings, aliens, ship):
	# create a default alien which is NOT added to the alien fleet
	default_alien = Alien(screen, ai_settings)
	alien_per_row = get_alien_per_row(ai_settings, default_alien.rect.width)
	row_per_screen = get_row_per_screen(ai_settings, default_alien.rect.height, ship.rect.height)
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

def alien_hit_bottom(aliens):
	for alien in aliens.sprites():
		if alien.rect.bottom >= alien.screen_rect.bottom:
			return True
			break

def update_aliens(stats, aliens, bullets, ship, screen, ai_settings):
	'''Update current position of all aliens'''
	check_fleet_edges(aliens, ai_settings)
	aliens.update()

	# check alien-ship collision
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(stats, aliens, bullets, ship, screen, ai_settings)

	# check whehter alien has hit bottom of screen
	if alien_hit_bottom(aliens):
		# treat it same as if ship got hit
		ship_hit(stats, aliens, bullets, ship, screen, ai_settings)

def ship_hit(stats, aliens, bullets, ship, screen, ai_settings):
	''' what happens when ship is hit by alien'''
	if stats.ship_left > 1:
		# decrease number of ships left
		stats.ship_left -= 1

		# emtpy all aliens and bullets when ship is hit
		aliens.empty()
		bullets.empty()

		# reposition ship
		ship.center = ship.screen_rect.centerx

		# recreate alien fleet
		create_alien_fleet(screen, ai_settings, aliens, ship)

		# give a little pause
		sleep(0.5)
	else:
		stats.game_active = False
		pygame.mouse.set_visible(True)

def check_key_down_event(event, ai_settings, screen, ship, bullets, stats, aliens):
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

	# press "P" to play the game	
	elif event.key == pygame.K_p:
		if not stats.game_active:
			ai_settings.initialize_dynamic_settings()
			# restart or start a new game
			game_restart(stats, aliens, bullets, screen, ai_settings, ship)
			# hide the mouse cursor
			pygame.mouse.set_visible(False)

def check_key_up_event(event, ship):
	# determine action when key is released
	if event.key == pygame.K_RIGHT:
	# set the moving flag to false so that ship stops moving when right arrow key is released
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
	# set the moving flag to false so that ship stops moving when left arrow key is released
		ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets, play_button, stats, aliens):
	# an event loop to monitor user's input (press key or move mouse)
	# The one below checks whether user clicks to close the program.
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		# check whether the event is a key press
		elif event.type == pygame.KEYDOWN:
			check_key_down_event(event, ai_settings, screen, ship, bullets, stats, aliens)
		elif event.type == pygame.KEYUP:
			check_key_up_event(event, ship)
		# check for mouseclick on play button
		# elif event.type == pygame.MOUSEBUTTONDOWN:
		# 	mouse_x, mouse_y = pygame.mouse.get_pos()
		# 	check_play_button(play_button, stats, mouse_x, mouse_y, aliens, bullets, screen, ai_settings, ship)

def check_play_button(play_button, stats, mouse_x, mouse_y, aliens, bullets, screen, ai_settings, ship):
	# click play_button to play the game again
	button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
	if button_clicked:
		# to prevent clicking the button area (without button present) 
		# and restarting the game. Game restarts ONLY when game inactive and mouse click
		if not stats.game_active:
			game_restart(stats, aliens, bullets, screen, ai_settings, ship)
			# hide the mouse cursor
			pygame.mouse.set_visible(False)

def game_restart(stats, aliens, bullets, screen, ai_settings, ship):
	# restart the game by resetting stats and clearing out remnants of previous game
	stats.game_active = True
	stats.reset_stats()
	# empty out any remaining aliens or bullets
	aliens.empty()
	bullets.empty()
	# create new fleet of aliens
	create_alien_fleet(screen, ai_settings, aliens, ship)
	#reposition ship to center
	ship.center = ship.screen_rect.centerx
	

def update_screen(ai_settings, screen, ship, bullets, aliens, play_button, stats):
	# redraw the scren during each pass of the loop
	screen.fill(ai_settings.background_color)
	# draw each bullet BEHIND the ship, so bullet drawn ahead of ship
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	aliens.draw(screen)
	
	# draw the play button only when game is inactive
	if not stats.game_active:
		play_button.draw_button()

	# display the most recently drawn screen.
	pygame.display.flip()

def update_bullets(screen, ai_settings, aliens, ship, bullets):
	# update bullet position and delete extra bullets
	bullets.update()

	# delete bullets that have traveled outside the screen from the Group
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

	check_bullet_alien_collision(screen, ai_settings, bullets, aliens, ship)

def check_bullet_alien_collision(screen, ai_settings, bullets, aliens, ship):
	# check to see whether a bullet has hit an alien. If so, remove both the bullet and alien.
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
	# remove remaining bullets when all aliens are destroyed
	if len(aliens) == 0:
		bullets.empty()

		# level up by increasing speed for every element
		ai_settings.increase_speed()

		create_alien_fleet(screen, ai_settings, aliens, ship)
