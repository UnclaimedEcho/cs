import numpy as np
import pygame
color = (0,0,0)
clock=pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((800, 800))

run = True


thrust = 850000
weight = 850000
numvertices = 3
dyt = 0
FPS = 30
def updatevectors(vectors,vertices, weight, thrust, dyt):
    
    if weight>10000:
        weight-=5000
    thrust+=1000
    vectors = np.array(vectors)
    vertices = np.array(vertices)
    dyt = dyt-((thrust/weight)/(FPS/2))
    if thrust>weight:
        for i in range(numvertices):
            #vectors[i][0] = vectors[i][0]+dxt
            vectors[i][1] = vectors[i][1]+dyt
            #vertices[i][0] = vertices[i][0]+vectors[i][0]
            vertices[i][1] = vertices[i][1]+vectors[i][1]
            #vertices[i][1] = vertices[i][1]+dyt
    return vertices, vectors, weight, thrust, dyt

vectors = [(0,0),(0,0),(0,0)]
vertices = [(390,780),(410,780),(400,760)]
vertices = np.array(vertices)
vectors = np.array(vectors)
fall=False
resetted=False
accel = 1
while run: 
    clock.tick(FPS)  
    flamevert = vertices.copy()
    flamevert[0][0] = 395
    flamevert[1][0] = 405
    flamevert[2][1] = flamevert[1][1]+20
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: run = False
    keys = pygame.key.get_pressed()
    # if keys[pygame.K_w]:
    #     thrust = 950000
    # else:
    #     thrust = 550000
    screen.fill(color)
    pygame.draw.rect(screen, (0,255,0), pygame.Rect(0, 780, 1000, 1000))
    pygame.draw.polygon(screen, (0, 255, 255), (vertices))
    pygame.draw.circle(screen, (255,100,0), (100, 100), 50)
    pygame.draw.circle(screen, (200,200,200), (700, 150), 30)
    if vertices[0][1]>100:
        vertvectlist = updatevectors(vectors, vertices, weight, thrust, dyt)
    #    else:
    #        fall = True
    # elif vertices[0][1] < 780:
    #     if accel<15:
    #         accel+=0.2  
    #     for x in vertices:
    #         x[1]+=accel
    # elif vertices[0][1] > 760 and resetted == False:
    #     print('aaa')
    #     accel=1
    #     vectors = [(0,0),(0,0),(0,0)]
    #     vertices = [(390,780),(410,780),(400,760)]
    #     dyt=0
    #     thrust = 850000
    #     weight = 850000
    #     fall=False
    #     resetted = True
        
    if vertices[0][1] < 780 and vertices[0][1]>100 and fall == False:
        pygame.draw.polygon(screen, (255, 0, 0), (flamevert))
    vertices = vertvectlist[0]
    vectors = vertvectlist[1]
    weight = vertvectlist[2]
    thrust = vertvectlist[3]
    dyt = vertvectlist[4]
    if dyt>1:
        dyt+=1
    pygame.display.flip()