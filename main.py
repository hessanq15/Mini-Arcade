
import pygame

from arcade.games.snake import Snake
from arcade.games.space_defender import SpaceDefender
from arcade.menu import ArcadeMenu
from arcade.input_manager import InputManager


def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Mini Arcade")

    clock = pygame.time.Clock()
    menu = ArcadeMenu()
    input_manager = InputManager()

    current_game = None
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                continue

            action = input_manager.get_action(event)

            if current_game is None:
                selection = menu.handle_input(action)

                if selection == "Quit":
                    running = False
                elif selection == "Snake":
                    current_game = Snake()
                elif selection == "Space Defender":
                    current_game = SpaceDefender()
                elif selection is not None:
                    print(f"Selected game: {selection}")

            else:
                if action == "BACK":
                    current_game = None

                elif isinstance(current_game, SpaceDefender):
                    if action is not None:
                        current_game.handle_input(action)

                    released = input_manager.get_release(event)

                    if released is not None:
                        current_game.handle_input(released, False)

                elif action is not None:
                    current_game.handle_input(action)

        if current_game is None:
            menu.draw(screen)
        else:
            current_game.update()
            current_game.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
