import pygame
import numpy as np
pygame.init()
screen = pygame.display.set_mode((800,800))
FPS = 60
run = True
clock = pygame.time.Clock()
color = (255,255,255)
color1 = (0,0,0)
gravity = 9.8
stiffness = 400
flag=0


vertices = ((375,50),(425,50),(425,100),(375,100))
vectors = [(0.0,0.0),(0.0,0.0),(0.0,0.0),(0.0,0.0)]
dyt = 0
# 0,1 is top
# 2,3 are bottom

def updateVectors(vectors,vertices,dyt, flag):
    odistance = 50
    force = (odistance + (vertices[1][1] - vertices[2][1]))/odistance * stiffness
    vectors = np.array(vectors)
    vertices = np.array(vertices)
    dyt = ((gravity - force)/FPS)

    print("dy,force: ", dyt,force)

    #stage 1
    # vertices[1][1] is top
    if (vertices[1][1] < 700):
        print("moving")
        for x in range(4):
            vectors[x][1] = vectors[x][1] + dyt
            print("vectors1: ",vectors[x][1])
            vertices[x][1] = vertices[x][1] + vectors[x][1]
            print("vertices1: ",vertices[x][1])
            flag=0
    
    #stage 2
    elif (vertices [1][1] >= 700) and vertices[1][1] <= vertices[2][1]+5:
        if (vertices[1][1]<=vertices[2][1]+5):
            for y in range(2):
                vectors[y][1] = vectors[y][1] + dyt
                print("vectors2: ",vectors[y][1])
                vertices[y][1] = vertices[y][1] + vectors[y][1]
                print("vertices2: ",vertices[y][1]) 
                vectors[y+2][1] += dyt
        else:
            print('zeroing')
            for i in range(4):
                vectors[i][1] = 0
            flag=1

    #stage 3
    elif (abs(vertices [1][1] - vertices[2][1]) >= 50) and (flag==1):
        print("rising")
        for i in range(4):
            vectors[i][1] = vectors[i][1] + dyt
            print("vectors3: ",vectors[i][1])
            vertices[i][1] = vertices[i][1] + vectors[i][1]
            print("vertices3: ",vertices[i][1]) 

    return vectors, vertices, dyt, flag

odistance = 50
# force = (odistance-(vertices[1][1]-vertices[2][1]))/odistance * stiffness

while run:  
    clock.tick(FPS)
    screen.fill(color1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_ESCAPE:
                run = False

    pygame.draw.polygon(screen,color,vertices)
    vectors, vertices, dyt, flag = updateVectors(vectors,vertices,dyt, flag)

    pygame.display.flip()
    pygame.display.update()