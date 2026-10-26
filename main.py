
import pygame

from arcade.menu import ArcadeMenu
from arcade.input_manager import InputManager


def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Mini Arcade")

    clock = pygame.time.Clock()
    menu = ArcadeMenu()
    input_manager = InputManager()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                continue

            action = input_manager.get_action(event)
            selection = menu.handle_input(action)

            if selection == "Quit":
                running = False

            elif selection is not None:
                print(f"Selected game: {selection}")

        menu.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
