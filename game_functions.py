'''
Author: Fanchen Bao
Date: 02/18/2018

Description:
Main function module for the game
'''

import sys
import pygame
from bullet import Bullet
from alien import Alien
from reward_stats import RewardStats
from reward import Reward
from missile import Missile
from shield import Shield
from time import sleep
from random import sample

def check_offensive_reward(reward_flag, ai_settings):
	# increase number of bullets allowed to coexist on the screen at the same time
	if reward_flag == "I":
		ai_settings.bullet_allowed += 1
	# increase number of projectiles per shot
	if reward_flag == "M":
		if ai_settings.projectile_number < ai_settings.max_projectile:
			ai_settings.projectile_number += 1
	# set number of bullets allowed to basically unlimited, very rare reward
	if reward_flag == "U":
		ai_settings.bullet_allowed = 1000000

def check_defensive_reward(reward_flag, stats, score_board, ai_settings, shields, screen, ship):
	# increase life
	if reward_flag == "L":
		stats.ship_left += 1
		score_board.prep_ships()
	# make a shield
	if reward_flag == "S":
		if ai_settings.shield_number < ai_settings.max_shield:
			ai_settings.shield_number += 1
			create_shield(shields, screen, ai_settings, ship)

def create_reward(screen, ai_settings, reward_flag, rewards, alien):
	# create a new reward at the same position where a designated alien is hit
	reward = Reward(screen, ai_settings, reward_flag)
	reward.rect.x = alien.rect.x
	reward.y = alien.rect.y
	reward.rect.y = reward.y
	rewards.add(reward)

def update_rewards(ship, rewards, ai_settings, stats, score_board, shields, screen):
	# update reward position and delete reward when it hits ship or disappears off the screen
	rewards.update()

	# delete rewards that have traveled outside the screen from the Group
	for reward in rewards.copy():
		if reward.rect.top >= reward.screen_rect.bottom:
			rewards.remove(reward)

	check_reward_ship_collision(ship, rewards, ai_settings, stats, score_board, shields, screen)

def check_reward_ship_collision(ship, rewards, ai_settings, stats, score_board, shields, screen):
	# check whether a reward has hit the ship
	# record the reward
	reward = pygame.sprite.spritecollideany(ship, rewards)
	if reward:
		check_offensive_reward(reward.reward_flag, ai_settings)
		check_defensive_reward(reward.reward_flag, stats, score_board, ai_settings, shields, screen, ship)
		# remove the reward that has hit the ship
		rewards.remove(reward)

def create_shield(shields, screen, ai_settings, ship):
	# create shield based on how many S reward player has collected
	shield = Shield(screen, ai_settings, ship)
	# shield is set right above the ship
	shield.rect.y = ship.rect.y - 15 * ai_settings.shield_number
	shields.add(shield)

def update_shields(shields, missiles, ai_settings, aliens):
	# update shield position and its behavior once got hit by missile
	shields.update()

	collisions_missile_shield = pygame.sprite.groupcollide(missiles, shields, True, True)
	if collisions_missile_shield:
		ai_settings.shield_number -= 1

	collisions_alien_shield = pygame.sprite.groupcollide(aliens, shields, False, True)
	if collisions_alien_shield:
		ai_settings.shield_number -= 1


def fire_bullet(ai_settings, screen, ship, bullets):
	# fire a bullet if the limit is not reached yet and when open_fire is true
	if ai_settings.open_fire:
		if len(bullets) == 0:
			# when there is no bullet, create one no matter what
			create_bullet(ai_settings, bullets, screen, ship)
		elif len(bullets) < ai_settings.bullet_allowed:
			# when there are already bullets, next bullet doesn't fire 
			# until the previous one is 10 pixels above the ship
			for bullet in bullets.sprites():
				if (ship.rect.top - bullet.rect.bottom) < 10:
					return
			create_bullet(ai_settings, bullets, screen, ship)

def create_bullet(ai_settings, bullets, screen, ship):
	x_position = (ai_settings.projectile_number-1) * (-ai_settings.between_projectile)
	for projectile in range(ai_settings.projectile_number):
		new_bullet = Bullet(ai_settings, screen, ship, x_position)
		bullets.add(new_bullet)
		x_position += 2 * ai_settings.between_projectile

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

def create_alien(screen, ai_settings, number_of_alien, number_of_row, aliens, alien_count):
	alien = Alien(screen, ai_settings)
	# each new alien is positioned to the right of the previous one with one alien width of space in between
	alien.x = alien.rect.x + number_of_alien * alien.rect.width * 2
	alien_y = alien.rect.y + number_of_row * alien.rect.height * 2
	alien.rect.x = alien.x
	alien.rect.y = alien_y
	# each alien has a different tag number
	alien.number = alien_count
	aliens.add(alien)

def create_alien_fleet(screen, ai_settings, aliens, ship, stats):
	# create a default alien which is NOT added to the alien fleet
	default_alien = Alien(screen, ai_settings)
	alien_per_row = get_alien_per_row(ai_settings, default_alien.rect.width)
	#max_row_per_screen = get_row_per_screen(ai_settings, default_alien.rect.height, ship.rect.height)
	
	row_per_screen = ai_settings.rows_each_level(stats)
	total_alien = alien_per_row * row_per_screen
	alien_count = 0
	# create a full fleet
	for number_of_row in range(row_per_screen):
		for number_of_alien in range(alien_per_row):
			create_alien(screen, ai_settings, number_of_alien, number_of_row, aliens, alien_count)
			alien_count += 1
	# create an instance of reward_stats, based on the game level
	if stats.level >= 4:
		reward_stats = RewardStats(stats.level)

		# find the aliens that will carry the reward
		designated_aliens = sample(range(total_alien), reward_stats.number_of_reward)
		for alien in aliens:
			if alien.number in designated_aliens:
				alien.reward_flag = reward_stats.assign_reward()

def change_fleet_direction(aliens, ai_settings):
	''' change fleet direction and move aliens down'''
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.alien_drop_speed
	ai_settings.fleet_direction *= -1	

def check_fleet_edges(aliens, ai_settings, screen, missiles):
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(aliens, ai_settings)
			fire_missile(missiles, ai_settings, aliens, screen)
			break

def fire_missile(missiles, ai_settings, aliens, screen):
	# create a missle that is fired by a randomly selected alien
	# reassign numbers so that all aliens are in the pool for random selection for firing missle
	reassign_alien_number(aliens)
	
	# do not change the missile_number parameter in settings, use a proxy to accept changes
	missile_number = ai_settings.missile_number
	
	# if number of alien is smaller than missile number, make missile number always 1 smaller than alien number
	if len(aliens) < missile_number:
		missile_number = len(aliens) - 1
	# choose randomly the number of aliens to fire missile
	designated_aliens = sample(range(len(aliens)), missile_number)

	for alien in aliens.sprites():
		# find the designated alien
		if alien.number in designated_aliens:
			if len(missiles) < missile_number:
				# make the missile
				missile = Missile(ai_settings, screen, alien)
				missiles.add(missile)

def reassign_alien_number(aliens):
	count = 0
	for alien in aliens.sprites():
		alien.number = count
		count += 1

def update_missiles(stats, aliens, bullets, ship, screen, ai_settings, score_board, rewards, missiles, shields):
	missiles.update()
	# delete missiles that have traveled outside the screen from the Group
	for missile in missiles.copy():
		if missile.rect.top >= missile.screen_rect.bottom:
			missiles.remove(missile)
			stats.score += ai_settings.missile_points
			score_board.prep_score()

	check_missile_ship_collision(stats, aliens, bullets, ship, screen, ai_settings, score_board, rewards, missiles, shields)

def check_missile_ship_collision(stats, aliens, bullets, ship, screen, ai_settings, score_board, rewards, missiles, shields):
	# check to see whether a missile has hit the ship
	if pygame.sprite.spritecollideany(ship, missiles):
		ship_hit(stats, aliens, bullets, ship, screen, ai_settings, score_board, rewards, missiles, shields)

def alien_hit_bottom(aliens):
	for alien in aliens.sprites():
		if alien.rect.bottom >= alien.screen_rect.bottom:
			return True
			break

def update_aliens(stats, aliens, bullets, ship, screen, ai_settings, score_board, rewards, missiles, shields):
	'''Update current position of all aliens'''
	check_fleet_edges(aliens, ai_settings, screen, missiles)
	aliens.update()

	# check alien-ship collision
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(stats, aliens, bullets, ship, screen, ai_settings, score_board, rewards, missiles, shields)

	# check whehter alien has hit bottom of screen
	if alien_hit_bottom(aliens):
		# treat it same as if ship got hit
		ship_hit(stats, aliens, bullets, ship, screen, ai_settings, score_board, rewards, missiles, shields)

def ship_hit(stats, aliens, bullets, ship, screen, ai_settings, score_board, rewards, missiles, shields):
	''' what happens when ship is hit by alien'''
	# decrease number of ships left
	stats.ship_left -= 1
	
	if stats.ship_left > 0:
		

		# emtpy all aliens and bullets and rewards and missiles when ship is hit
		aliens.empty()
		bullets.empty()
		rewards.empty()
		missiles.empty()
		shields.empty()

		# reposition ship
		ship.center = ship.screen_rect.centerx

		# decrease ship counts on top left corner
		score_board.prep_ships()

		# recreate alien fleet
		create_alien_fleet(screen, ai_settings, aliens, ship, stats)

		# reset all rewards when ship gets hit
		ai_settings.reset_reward_settings()
		# reset ship, alien, and bullet, otherwise when ship hit at high level, 
		# one cannot win with the remaining lives when all rewards are reset 
		ai_settings.initialize_dynamic_settings()

		# give a little pause
		sleep(0.5)
	else:
		stats.game_active = False
		pygame.mouse.set_visible(True)

		# to show there is no ship left
		score_board.prep_ships()

def check_key_down_event(event, ai_settings, screen, ship, bullets, stats, aliens, score_board, filename, rewards, missiles):
	# determine action when key is pushed down
	if event.key == pygame.K_RIGHT:
		# set the moving flag to true so that ship continues moving right
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		# set the moving flag to true so that ship continues moving left
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		# create bullets when spacebar is pressed down
		ai_settings.open_fire = True
	elif event.key == pygame.K_q:
		# save high score and then quit
		record_high_score(stats.high_score, filename)
		sys.exit()

	# press "P" to play the game	
	elif event.key == pygame.K_p:
		if not stats.game_active:
			# restart or start a new game
			game_restart(stats, aliens, bullets, screen, ai_settings, ship, score_board, rewards, missiles)
			# hide the mouse cursor
			pygame.mouse.set_visible(False)

def check_key_up_event(event, ship, ai_settings):
	# determine action when key is released
	if event.key == pygame.K_RIGHT:
	# set the moving flag to false so that ship stops moving when right arrow key is released
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
	# set the moving flag to false so that ship stops moving when left arrow key is released
		ship.moving_left = False
	elif event.key == pygame.K_SPACE:
		# stop firing bullets when spacebar is lifted
		ai_settings.open_fire = False

def check_events(ai_settings, screen, ship, bullets, play_button, stats, aliens, score_board, filename, rewards, missiles):
	# an event loop to monitor user's input (press key or move mouse)
	# The one below checks whether user clicks to close the program.
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			# save high score and then quit
			record_high_score(stats.high_score, filename)
			sys.exit()
		# check whether the event is a key press
		elif event.type == pygame.KEYDOWN:
			check_key_down_event(event, ai_settings, screen, ship, bullets, stats, aliens, score_board, filename, rewards, missiles)
		elif event.type == pygame.KEYUP:
			check_key_up_event(event, ship, ai_settings)


		# check for mouseclick on play button
		# elif event.type == pygame.MOUSEBUTTONDOWN:
		# 	mouse_x, mouse_y = pygame.mouse.get_pos()
		# 	check_play_button(play_button, stats, mouse_x, mouse_y, aliens, bullets, screen, ai_settings, ship)

def record_high_score(high_score, filename):
	'''record high score in a separate file so that each new game starts with a previous high score'''
	str_high_score = str(high_score)
	with open(filename, 'w') as file_object:
		file_object.write(str_high_score) 

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

def game_restart(stats, aliens, bullets, screen, ai_settings, ship, score_board, rewards, missiles):
	# restart the game by resetting stats and clearing out remnants of previous game
	stats.game_active = True
	
	# reset all the stats
	stats.reset_stats()
	ai_settings.reset_reward_settings()
	ai_settings.initialize_dynamic_settings()

	# reset all the scoreboard images
	prep_scoreboard_images(score_board)

	# empty out any remaining aliens, bullets, rewards, or missiles
	aliens.empty()
	bullets.empty()
	rewards.empty()
	missiles.empty()

	# create new fleet of aliens
	create_alien_fleet(screen, ai_settings, aliens, ship, stats)
	#reposition ship to center
	ship.center = ship.screen_rect.centerx

def prep_scoreboard_images(score_board):
	score_board.prep_score()
	score_board.prep_level()
	score_board.prep_ships()
	
def update_screen(ai_settings, screen, ship, bullets, aliens, play_button, stats, score_board, rewards, missiles, shields):
	# redraw the scren during each pass of the loop
	screen.fill(ai_settings.background_color)
	# draw each bullet BEHIND the ship, so bullet drawn ahead of ship
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	aliens.draw(screen)
	rewards.draw(screen)
	for missile in missiles.sprites():
		missile.draw_missile()
	shields.draw(screen)
	
	# draw the play button only when game is inactive
	if not stats.game_active:
		play_button.draw_button()

	score_board.show_score()

	# display the most recently drawn screen.
	pygame.display.flip()

def update_bullets(screen, ai_settings, aliens, ship, bullets, stats, score_board, rewards, missiles):
	# update bullet position and delete extra bullets
	bullets.update()

	# delete bullets that have traveled outside the screen from the Group
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

	check_bullet_alien_collision(screen, ai_settings, bullets, aliens, ship, stats, score_board, rewards, missiles)

def check_bullet_alien_collision(screen, ai_settings, bullets, aliens, ship, stats, score_board, rewards, missiles):
	# check to see whether a bullet has hit an alien. If so, remove both the bullet and alien.
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
	if collisions:
		for aliens in collisions.values():
			# calculate score
			stats.score += ai_settings.alien_points * len(aliens)
			score_board.prep_score()

			for alien in aliens:
				if alien.reward_flag:
					create_reward(screen, ai_settings, alien.reward_flag, rewards, alien)
		check_high_score(stats, score_board)	

	# remove remaining bullets when all aliens are destroyed
	if len(aliens) == 0:
		bullets.empty()
		rewards.empty()
		missiles.empty()

		# level up by increasing speed for every element
		ai_settings.increase_speed()

		# update level information
		stats.level += 1
		score_board.prep_level()

		# update alien missile information
		if ai_settings.missile_number < ai_settings.max_missile:
			ai_settings.missile_number += 1

		create_alien_fleet(screen, ai_settings, aliens, ship, stats)

		# give a little pause
		sleep(0.5)

def check_high_score(stats, score_board):
	if stats.score > stats.high_score:
		stats.high_score = stats.score
		score_board.prep_high_score()

