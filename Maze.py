# import Enemy from enemy
import pygame

def main():
    print("main!")

    # enemy = Enemy(100, 0, 0, pygame.color.red)

    (width, height) = (300, 200)
    screen = pygame.display.set_mode((width, height))
    # pygame.display.flip()
    screen.fill((250, 0, 0))

    # pygame.draw.circle(screen, enemy.color, (enemy.x, enemy.y), enemy.size)
    pygame.draw.circle(screen, (0, 250, 0), [10, 10], 10, 1)




    pygame.display.flip()

    running = True

    # Busy loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


main()