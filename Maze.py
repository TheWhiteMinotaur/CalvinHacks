# import Enemy from enemy
import pygame

def parse_config():
    with open('config.cfg', 'r') as config_file:
        lines = config_file.read().split('\n')
        return [l.split('=') for l in lines]

def main():
    print("main!")

    try:
        configs = parse_config()
    except:
        print("Error parsing config file.")
        return

    # enemy = Enemy(100, 0, 0, pygame.color.red)

    (width, height) = (str(configs[0]), str(configs[1]))
    screen = pygame.display.set_mode((width, height))

    pygame.display.flip()

    running = True

    # Busy loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

main()
