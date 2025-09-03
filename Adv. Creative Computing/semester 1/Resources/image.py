# importing required library
import pygame

# activate the pygame library .
pygame.init()
X = 800
Y = 800

screen = pygame.display.set_mode((X, Y))

# set the pygame window name
pygame.display.set_caption('image')

# create a surface object, image is drawn on it.
imp = pygame.image.load("./meme.png").convert()
imp = pygame.transform.scale(imp, (100, 100))
# Using blit to copy content from one surface to other
screen.blit(imp, (500, 500))

# paint screen one time
pygame.display.flip()
status = True
while (status):

# iterate over the list of Event objects
# that was returned by pygame.event.get() method.
	for i in pygame.event.get():

		# if event object type is QUIT
		# then quitting the pygame
		# and program both.
		if i.type == pygame.QUIT:
			status = False

# deactivates the pygame library
pygame.quit()
