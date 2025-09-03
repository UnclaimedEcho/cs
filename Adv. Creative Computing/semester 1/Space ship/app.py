import pygame
color = (255,255,255)
clock=pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((800, 640))
run = True
accel=1
upaccel=0
leftright=0
y=0
while run:   
    if y < 580:
        y+=accel
        clock.tick(60)
        if accel<15:
            accel+=0.2     
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_ESCAPE: run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        y-=0.02*upaccel
        upaccel+=0.9
        accel=1
    if keys[pygame.K_w] == False:
        upaccel = 0
        pass
    if y < 580:
        if keys[pygame.K_a]:
            leftright-=2
        if keys[pygame.K_d]:
            leftright+=2
    screen.fill(color)
    pygame.draw.polygon(screen, (0, 255, 255), ((125+leftright,25+y),(115+leftright,50+y),(135+leftright,50+y)))
    pygame.display.flip()