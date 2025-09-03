import numpy as np
import math 
import pygame
black = (0,0,0)
green = (0,255,0)
clock=pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((800, 800))
run = True
dyt = 0
force = 0

# 120 FPS 4000 Stiffness
# 60 FPS 2000 Stiffness
# 30 FPS 1100 Stiffness
# 10 FPS 350 Stiffness

FPS = 10
stiffness = 350


bottom = [1,2]
top = [0,3]
vectors = [(0.0,0.0),(0.0,0.0),(0.0,0.0),(0.0,0.0)]
vertices = [(375,20),(375,70),(425,70), (425,20)]
OriginalHeight = vertices[2][1]-vertices[0][1]
state = 'moving'
check = False

def updateVectors(vectors,vertices, dyt,stiffness, force, top, OriginalHeight, state, check):
    vectors = np.array(vectors)
    vertices = np.array(vertices)
    Height = abs(vertices[2][1]-vertices[0][1])
    dyt = (9.8/FPS) 
    
    if state == 'moving':
        if vertices[1][1] < 700:
            check = True
        for i in range(len(vertices)):
            vectors[i][1] = vectors[i][1] + dyt 
            vertices[i][1] = vertices[i][1] + vectors[i][1] - force/FPS
        if vertices[1][1] >= 700 and vertices[0][1] < 705 and check == True:
            state = 'condensing'
            check = False

    elif state == "expanding":
        #stop
        if Height == 47:
            for i in top:
                vertices[i][1] = vertices[1][1] - 50
            state = 'done'
        elif Height < OriginalHeight:
            print("Height:", Height)
            for i in top:
                vertices[i][1] = vertices[1][1] - 50
            vectors = [(0.0,0.0),(0.0,0.0),(0.0,0.0),(0.0,0.0)]
            force = abs((((OriginalHeight - Height)/OriginalHeight) * stiffness))
        if Height == OriginalHeight:
            state = 'moving'

    elif state == 'condensing':

        for i in top:
            vectors[i][1] = vectors[i][1] + dyt
            vertices[i][1] = vertices[i][1] + vectors[i][1] - force/FPS
        for i in bottom:
            vectors[i][1] = 0
        if vertices[0][1] >= 705:
            for i in top:
               vectors[i][1] = 0
        if Height <= OriginalHeight:
            state = 'expanding'

    if Height < 50 and state != 'done':
        print('Compressed')
    return vertices, vectors, dyt,force, state, check
    

while run:
    clock.tick(FPS)
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: run = False

    vertices, vectors, dyt, force, state, check = updateVectors(vectors,vertices, dyt,stiffness,force, top, OriginalHeight,state,check)

    screen.fill(black)
    pygame.draw.rect(screen,green,pygame.Rect(0,702,800,100))
    pygame.draw.polygon(screen, (0, 255, 255), (vertices))
    pygame.display.update()