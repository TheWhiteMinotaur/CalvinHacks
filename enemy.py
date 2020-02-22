# Currently not my code
# Obtained from https://techwithtim.net/tutorials/game-development-with-python/pygame-tutorial/pygame-animation/

import pygame

pygame.init()

win = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('transparent-sprite-enemy-8.gif')]
walkLeft = [pygame.image.load('transparent-sprite-enemy-8.gif')]
walkUp = [pygame.image.load('transparent-sprite-enemy-8.gif')]
walkDown = [pygame.image.load('transparent-sprite-enemy-8.gif')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('transparent-sprite-enemy-8.gif')

x = 50
y = 200
width = 10
height = 20
vel = 5

clock = pygame.time.Clock()

isJump = False
jumpCount = 10

left = False
right = False
up = False
down = False
walkCount = 0


def redrawGameWindow():
    global walkCount

    win.blit(bg, (0, 0))
    if walkCount + 1 >= 27:
        walkCount = 0

    if left:
        win.blit(walkLeft[0], (x, y))
        walkCount += 1
    elif right:
        win.blit(walkRight[0], (x, y))
        walkCount += 1
    elif up:
        win.blit(walkUp[0], (x, y))
        walkCount += 1
    elif down:
        win.blit(walkDown[0], (x,y))
        walkCount += 1
    else:
        win.blit(char, (x, y))
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

    elif keys[pygame.K_RIGHT] and x < 500 - vel - width:
        x += vel
        left = False
        right = True

    elif keys[pygame.K_UP] and y > vel:
        y -= vel
        left = False
        right = False
        up = True

    elif keys[pygame.K_DOWN] and y < 500 - vel - height:
        y += vel
        left = False
        right = False
        up = False
        down = True

    else:
        left = False
        right = False
        up = False
        down = False
        walkCount = 0

    if not (isJump):
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











# def Enemy():
#     def __init__(self, health, sX, sY, color, size):
#         super(health)
#
#         self.health = health
#         self.x = sX
#         self.y = sY
#         self.color = color
#         self.size = size
#
#         # pygame.draw.circle(0,self.color, {self.x, self.y}, size)
