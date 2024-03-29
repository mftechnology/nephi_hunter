import pyray
from nephi_hunter.constants import ANIMAL_IMAGE
from nephi_hunter.game.casting.actor import Actor
"""
class Animals(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("images/animal" + str(random.randint(1, 5)) + ".png")
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]
		self.move_counter = 0
		self.move_direction = 1

	def update(self):
		self.rect.x += self.move_direction
		self.move_counter += 1
		if abs(self.move_counter) > 75:
			self.move_direction *= -1
			self.move_counter *= self.move_direction

	def get_body(self):
		#get position on the body image
		return self.rect.center
"""

class Animals(Actor):

	def __init__(self):
		super().__init__()

		self.image = pyray.image.load(ANIMAL_IMAGE)
