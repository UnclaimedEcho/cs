import pygame
import random
clock=pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((800, 800))
black = (0,0,0)
red = (255, 0, 0)
white = (255,255,255)
run=True
def drawdice(number):
    #dice rectangle
    pygame.draw.rect(screen, red, pygame.Rect(50, 50, 700, 700))
    if number%2:
        #odd center circle
        pygame.draw.circle(screen, white,[400,400],50,50)
    if number > 1:
        #top left and bottom right
        pygame.draw.circle(screen, white,[250,250],50,50)
        pygame.draw.circle(screen, white,[550,550],50,50)
    if number > 3:
        #top right and bottom left
        pygame.draw.circle(screen, white,[250,550],50,50)
        pygame.draw.circle(screen, white,[550,250],50,50)
    
    if number == 6:
        #center side dots
        pygame.draw.circle(screen, white,[250,400],50,50)
        pygame.draw.circle(screen, white,[550,400],50,50)

number = 1
while run:   
    clock.tick(60)
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_ESCAPE: run = False
            if event.key == pygame.K_SPACE:
                #sets the numnber to a random number OTHER than the current one.
                oldnum = number
                while oldnum == number:
                    number = random.randint(1,6)  

    drawdice(number)

    pygame.display.flip()