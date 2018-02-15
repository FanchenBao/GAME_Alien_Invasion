class Settings():
	''' to store all settings for alien_invasion'''
	def __init__(self):
		''' the static settings'''
		self.screen_height = 700
		self.screen_width = 1050
		self.background_color = (230, 230, 230)
		
		# ship settings	
		self.ship_limit = 3

		# bullet settings
		self.bullet_width = 300
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullet_allowed = 4

		# alien settings
		self.alien_drop_speed = 10
		

		# how quickly the game speeds up
		self.speedup_scale = 1.1

		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		''' the following settings change throughout the game'''
		self.ship_speed = 5
		self.bullet_speed = 4
		self.alien_speed = 4
		# alien fleet moving direction. 1 = move right, -1 = move left
		self.fleet_direction = 1

	def increase_speed(self):
		'''increase speed after each level for all moving objects'''
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale