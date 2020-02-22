#Currently not my code
#Obtained from https://techwithtim.net/tutorials/game-development-with-python/pygame-tutorial/pygame-animation/

import pygame
pygame.init()

win = pygame.display.set_mode((500,480))
pygame.display.set_caption("The RISE of BOB")

attackRight = [pygame.image.load('Sprites/player1FaceScreenRight.png'), pygame.image.load('Sprites/p1FRA1.png'), pygame.image.load('Sprites/p1FRA2.png'),
             pygame.image.load('Sprites/p1FRA3.png'), pygame.image.load('Sprites/p1FRA2.png'), pygame.image.load('Sprites/p1FRA1.png'), pygame.image.load('Sprites/player1FaceScreenRight.png')]
attackLeft = [pygame.image.load('Sprites/player1FaceScreenLeft.png'), pygame.image.load('Sprites/p1FLA1.png'), pygame.image.load('Sprites/p1FLA2.png'),
             pygame.image.load('Sprites/p1FLA3.png'), pygame.image.load('Sprites/p1FLA2.png'), pygame.image.load('Sprites/p1FLA1.png'), pygame.image.load('Sprites/player1FaceScreenLeft.png')]
bg = pygame.image.load('bg.jpg')

x = 25
y = 375
width = 40
height = 60
vel = 5

clock = pygame.time.Clock()

isJump = False
jumpCount = 10

preKey = True #True=Right  False=Left
attack = False
left = False
right = False
up = False
down = False
walkCount = 0

def redrawGameWindow():
    global walkCount
    
    win.blit(bg, (0,0))  
    if walkCount + 1 >= 28:
        walkCount = 0
        
    if left:  
        win.blit(pygame.image.load('Sprites/player1FaceScreenLeft.png'), (x,y))
        walkCount += 1                          
    elif right:
        win.blit(pygame.image.load('Sprites/player1FaceScreenRight.png'), (x,y))
        walkCount += 1
    elif up:
        win.blit(pygame.image.load('Sprites/player1FaceScreenRight.png'), (x,y))
        walkCount += 1
    elif down:
        win.blit(pygame.image.load('Sprites/player1FaceScreenRight.png'), (x,y))
        walkCount += 1

    elif attack and preKey:
        win.blit(attackRight[walkCount//4], (x,y))
        walkCount += 1
    elif attack and not preKey:
        win.blit(attackLeft[walkCount//4], (x,y))
        walkCount += 1
    elif preKey:
        win.blit(pygame.image.load('Sprites/player1FaceScreenRight.png'), (x, y))
        walkCount = 0
    else:
        win.blit(pygame.image.load('Sprites/player1FaceScreenLeft.png'), (x, y))
        walkCount = 0
        
    pygame.display.update() 
    


run = True

while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > vel: 
        x -= vel
        left = True
        right = False
        preKey = False

    elif keys[pygame.K_RIGHT] and x < 500 - vel - width:  
        x += vel
        left = False
        right = True
        preKey = True
        
    elif keys[pygame.K_UP] and y > vel:
        y -= vel
        left = False
        right = False
        down = False
        up = True
        attack = True

    elif keys[pygame.K_DOWN] and y < 500 - vel - height:
        y += vel
        left = False
        up = False
        right = False
        down = True
        
    else: 
        left = False
        right = False
        walkCount = 0
        
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            left = False
            right = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else: 
            jumpCount = 10
            isJump = False

    redrawGameWindow()
    
    
pygame.quit()