import pygame.font

class Button():
	def __init__(self, screen, ai_settings, msg):
		'''initialize button'''
		self.screen = screen
		self.screen_rect = screen.get_rect()
		# dimension and property of the botton
		self.width = 200
		self.height = 50
		self.button_color = (0, 255, 0)
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 48)

		# position the botom to the center screen
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center

		# put message to the botton
		self.prep_msg(msg)

	def prep_msg(self, msg):
		''' render a msg into an image'''
		self.msg_image = self.font.render(msg, True, self.text_color, 
			self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def draw_button(self):
		''' draw the blank button and then the msg'''
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)
