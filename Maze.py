# import Enemy from enemy
import pygame
import sys
from level import Level

def parse_config():
    with open('./config.cfg', 'r') as config_file:
        lines = config_file.read().split('\n')
        lines = lines[:len(lines)-1]
        print(lines)
        return { l.split('=')[0]:l.split('=')[1] for l in lines }

def main():
    print("main!")

    try:
        configs = parse_config()
    except:
        print("Error parsing config file: " + str(sys.exc_info()[0]))
        return

    # enemy = Enemy(100, 0, 0, pygame.color.red)
    pygame.init()

    (width, height) = (int(configs["resolutionX"]), int(configs["resolutionY"]))
    screen = pygame.display.set_mode((width, height))

    pygame.display.flip()

    running = True

    (x, y) = (240, 80)

    s = pygame.image.load('Sprites/player1FaceScreenLeft.png')
    bg = pygame.image.load('./bg_test.png')

    clock = pygame.time.Clock()
    level = Level()
    level.parse("map1.json")

    # Busy loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        x1, y1 = x, y
        if keys[pygame.K_LEFT]:
            x1 = x - 1
        elif keys[pygame.K_RIGHT]:
            x1 = x + 1
        elif keys[pygame.K_UP]:
            y1 = y - 1
        elif keys[pygame.K_DOWN]:
            y1 = y + 1

        if (level.is_point_in_path([x1,y1])):
            x = x1
            y = y1

        screen.blit(bg, (0,0))
        screen.blit(s, (x,y))
        pygame.display.flip()
        clock.tick(60)

main()
pygame.quit()
