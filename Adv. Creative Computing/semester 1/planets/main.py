import numpy as np
import math
import pygame

black = (0,0,0)
white = (255,255,255)

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 800))
run = True
FPS = 60

class earth:
  def __init__(self):
    self.mass = 5.972 * math.pow(10,24)
    # self.mass = 5
    self.name = 'Earth'
    self.vectors = np.array([(1*1e5,0)])
    self.vertices = np.array([(400 * 1e5,0*1e5)])
    self.color = (0,255,200)
    self.radius = 10

class mars:
  def __init__(self):
    self.mass = 6.39 * math.pow(10,23)
    # self.mass = 5

    self.name = 'Mars'
    self.vectors = np.array([(0, 1*1e5)])
    self.vertices = np.array([(100*1e5,100*1e5)])
    self.color = (255,120,0)
    self.radius = 20

class sun:
  def __init__(self):
    self.mass = 1.989 * math.pow(10,30)
    # self.mass = 5
    self.name = 'Sun'
    self.vectors = np.array([(0,0)])
    self.vertices = np.array([(400 * 1e5,400*1e5)])
    self.color = (255,255,204)
    self.radius = 80

Earth = earth()
Sun = sun()
Mars = mars()

planets = [Sun, Earth, Mars]
planetPairs = [(Earth,Mars),(Earth,Sun),(Mars,Sun)]

# planets = [Sun, Mars]
# planetPairs = [(Mars,Sun)]

G = 6.67 * math.pow(10,-11)

# AU = 149597871
# SCALE = 250/AU

def drawplanet(planet):
   pygame.draw.circle(screen, planet.color, (planet.vertices[0][0] / 1e5, planet.vertices[0][1] / 1e5), planet.radius)


def updatePlanet(planet1, planet2, G):
  angle = math.atan2((planet1.vertices[0][1] - planet2.vertices[0][1]),(planet1.vertices[0][0] - planet2.vertices[0][0]))
  r = math.sqrt(math.pow((planet1.vertices[0][0] - planet2.vertices[0][0]),2) + math.pow((planet1.vertices[0][1] - planet2.vertices[0][1]),2))
  force = ((G * planet1.mass * planet2.mass) / math.pow(r,2))

  planet1X = -(math.cos(angle) * force) / planet1.mass / FPS
  planet1Y = -(math.sin(angle) * force) / planet1.mass / FPS
  planet2X = (math.cos(angle) * force) / planet2.mass / FPS
  planet2Y = (math.sin(angle) * force) / planet2.mass / FPS
  


  # print(planet1.vectors[0][0],planet1.vectors[0][1], planet2.vectors[0][0], planet2.vectors[0][1])

  planet1.vectors[0][0] += planet1X
  planet1.vectors[0][1] += planet1Y
  planet2.vectors[0][0] += planet2X
  planet2.vectors[0][1] += planet2Y

  # print(planet1.vectors[0][0],planet1.vectors[0][1], planet2.vectors[0][0], planet2.vectors[0][1])

  planet1.vertices[0][0] += planet1.vectors[0][0]
  planet1.vertices[0][1] += planet1.vectors[0][1]
  planet2.vertices[0][0] += planet2.vectors[0][0]
  planet2.vertices[0][1] += planet2.vectors[0][1]

  print(planet1.vertices[0], planet2.vertices[0])
  # print(planet2.name, planet2.vertices)
  return(planet1.vectors, planet2.vectors, planet1.vertices, planet2.vertices)


# print(math.pow(4,2))
# for pair in planetPairs:
#     updatePlanet(pair,G)

while run:
    clock.tick(FPS)
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: run = False

    screen.fill(black)


    for pair in planetPairs:
        planet1 = pair[0]
        planet2 = pair[1]
        planet1.vectors, planet2.vectors, planet1.vertices, planet2.vertices = updatePlanet(planet1, planet2, G)

    for planet in planets:
        drawplanet(planet)
    
    # drawplanet(Sun)
    # drawplanet(Mars)
    # drawplanet(Earth)

    # print(Mars.vertices[0])
    pygame.display.update()

    # r = sq((verticeEart[0][0] - verticeMars[0][0])^2 + (verticeEart[0][1] - verticeMars[0][1])^2)
    # force = ((G * M1 * M2) / r^2)
    # yValue = sin0 * force/M1
    # xValue = cos0 * force/M1
    # vectorEarth[0][0] += xValue
    # vectorEarth[0][1] += yValue
    # verticeEarth[0][0] += vectorEarth[0][1]
    # verticeEarth[0][1] += vectorEarth[0][1]
    # G = 6.67 * 10^-11
    # angle = arctan((Earthy-Marsy)/(Earthx - Marsx))