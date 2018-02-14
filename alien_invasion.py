import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from button import Button
import game_functions as gf
from game_stats import GameStats

def run_game():
	# initialize game and create a screen object.
	
	# initialize game
	pygame.init()

	# create game display with 1200 pixels wide and 800 pixels in height
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	# create an instance to store game stats
	stats = GameStats(ai_settings)

	ship = Ship(screen, ai_settings)
	bullets = Group()
	aliens = Group()

	# create a play button
	msg = 'Play'
	play_button = Button(screen, ai_settings, msg)
	
	# create an alient fleet
	gf.create_alien_fleet(screen, ai_settings, aliens, ship)

	# The main loop of the game
	while True:
		gf.check_events(ai_settings, screen, ship, bullets, play_button, stats, aliens)
		if stats.game_active:
			ship.update()
			gf.update_bullets(screen, ai_settings, aliens, ship, bullets)
			gf.update_aliens(stats, aliens, bullets, ship, screen, ai_settings)
		gf.update_screen(ai_settings, screen, ship, bullets, aliens, play_button, stats)
		
run_game()
