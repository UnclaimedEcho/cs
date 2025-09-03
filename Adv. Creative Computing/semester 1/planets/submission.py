import pygame
import numpy as np
import math
pygame.init()
WIDTH = 800
HEIGHT = 800
G = 6.67e-11
AUSCALE = 745000000

black = (0,0,0)

screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
FPS = 60
run = True

class Mars:
  def __init__(self):
    self.mass = 6.39e23
    self.distance = 2.37e11
    self.name = 'mars'
    self.vectors = np.array([0.0, 24077.0])
    self.vertices = np.array([-2.37e11, 0])
    self.color = (255,120,0)
    self.radius = 30

class Earth:
  def __init__(self):
    self.mass = 5.97e24
    self.distance = 1.49e11
    self.name = 'earth'
    self.vectors = np.array([29784,0])
    self.vertices = np.array([0 , -1.49e11])
    self.color = (0,255,200)
    self.radius = 15

class Sun:
  def __init__(self):
    self.mass = 1.99e30
    self.distance = 0
    self.name = 'sun'
    self.vectors = np.array([0.0 , 0.0])
    self.vertices = np.array([0,0])
    self.color = (255,255,204)
    self.radius = 80

mars = Mars()
sun = Sun()
earth = Earth()


planets = [sun, earth,mars]

def updatevectors(planets):
    for i in planets:
        for j in planets:
            if i != j:
                r = math.sqrt((i.vertices[0] - j.vertices[0]) ** 2 + (i.vertices[1] - j.vertices[1]) ** 2)
                force = (G * i.mass * j.mass) / r ** 2
                angle = math.atan2((i.vertices[1] - j.vertices[1]),(i.vertices[0] - j.vertices[0]))
                j.vectors[0] += ((math.cos(angle)*force)/j.mass) * 58800
                j.vectors[1] += ((math.sin(angle)*force)/j.mass) * 58800

        i.vertices[0] = i.vertices[0] + i.vectors[0] * 58800
        i.vertices[1] = i.vertices[1] + i.vectors[1] * 58800
    return planets

def drawplanets(screen, planets):
    for i in planets:
        pygame.draw.circle(screen, i.color , ((i.vertices[0]/AUSCALE) + WIDTH/2 , (i.vertices[1]/AUSCALE) + HEIGHT/2), i.radius)

while run:
    clock.tick(FPS)
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
    planets = updatevectors(planets)
    drawplanets(screen, planets)
    pygame.display.flip()