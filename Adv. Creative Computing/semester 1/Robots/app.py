import pygame
import time

pygame.init()
screen = pygame.display.set_mode((800, 640))
color = (0,100,255)
run = True

class robot():
    def __init__(self, screen, x, y, color, movecord):
        pygame.draw.rect(screen, color, pygame.Rect(x, y, 80, 80),5)
        pygame.draw.rect(screen, color, pygame.Rect(x+15, y+80, 5, 40))
        pygame.draw.rect(screen, color, pygame.Rect(x+60, y+80, 5, 40))
        pygame.draw.rect(screen, color, pygame.Rect(x+15, y+20, 10, 10))
        pygame.draw.rect(screen, color, pygame.Rect(x+55, y+20, 10, 10))
        pygame.draw.rect(screen, color, pygame.Rect(x+35, y+40, 10, 10))
        pygame.draw.rect(screen, color, pygame.Rect(x+15, y+55, 50, 10), 3)
        pygame.draw.rect(screen, color, pygame.Rect(x-20, y+50+movecord, 20, 10))
        pygame.draw.rect(screen, color, pygame.Rect(x+80, y+50+movecord, 20, 10))

class cloud():
    def __init__(self, screen, x, y, movecord):
        pygame.draw.rect(screen, (255,255,255), pygame.Rect(x+2*movecord, y, 100, 40))
        pygame.draw.rect(screen, (255,255,255), pygame.Rect(x+20+2*movecord, y-20, 30, 20))

class robot_head(robot):
    def __init__(self, screen, x, y, color, movecord):
        super().__init__(screen, x, y, color, movecord)
        pygame.draw.rect(screen, color, pygame.Rect(x+20-movecord, y-30, 5, 30))
        pygame.draw.rect(screen, color, pygame.Rect(x+55+movecord, y-30, 5, 30))

movecord=0
bounce=True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_ESCAPE: run = False
    screen.fill(color)
    pygame.draw.rect(screen, (0,255,0), pygame.Rect(0, 500, 1000, 1000))
    robot1 = robot(screen, 200, 400 , (0,0,0), movecord)
    cloud1 = cloud(screen, 200,  100, movecord)
    robot2 = robot(screen, 400, 400 , (255,0,0), movecord)
    robot3 = robot_head(screen, 600, 400 , (0,255,255), movecord)
    if bounce==True:
        movecord+=1
    if bounce==False:
        movecord-=1
    if movecord == 10:
        bounce=False
    if movecord == 0:
        bounce=True
    pygame.display.flip()
    time.sleep(0.05)