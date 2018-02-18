class Settings():
	''' to store all settings for alien_invasion'''
	def __init__(self):
		''' the static settings'''
		self.screen_height = 700
		self.screen_width = 1050
		self.background_color = (230, 230, 230)

		# bullet settings
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		# maximum projectiles allowed per shot
		self.max_projectile = 5
		# set the distance between the projectles fired at the same time
		self.between_projectile = 7

		# alien settings
		self.alien_drop_speed = 10

		# how quickly the game speeds up
		self.speedup_scale = 1.1

		# how many points to scale up for alien
		self.score_scale = 1.5

		# reward settings
		self.reward_speed = 2

		self.initialize_dynamic_settings()

		# reset settings related to rewards
		self.reset_reward_settings()

	def reset_reward_settings(self):
		self.bullet_allowed = 1000
		# how many projectiles shot out with one spacebar press
		self.projectile_number = 1
		self.ship_limit = 3

	def initialize_dynamic_settings(self):
		''' the following settings change throughout the game'''
		self.ship_speed = 4
		self.bullet_speed = 4
		self.alien_speed = 3
		# alien fleet moving direction. 1 = move right, -1 = move left
		self.fleet_direction = 1

		# how many points earned shooting down one alien
		self.alien_points = 50

	def increase_speed(self):
		'''increase speed after each level for all moving objects'''
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale
		self.alien_points = int(self.score_scale * self.alien_points)