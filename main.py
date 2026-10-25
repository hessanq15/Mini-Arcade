
import pygame


def main():
    pygame.init()

    screen = pygame.display.set_mode((700, 600))
    pygame.display.set_caption("Mini Arcade")

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((25, 25, 45))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
