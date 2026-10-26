import pygame


class InputManager:
    def __init__(self):
        self.key_bindings = {
            pygame.K_UP: "UP",
            pygame.K_DOWN: "DOWN",
            pygame.K_LEFT: "LEFT",
            pygame.K_RIGHT: "RIGHT",
            pygame.K_SPACE: "SELECT",
            pygame.K_RETURN: "SELECT",
            pygame.K_ESCAPE: "BACK",
        }

    def get_action(self, event):
        if event.type != pygame.KEYDOWN:
            return None

        return self.key_bindings.get(event.key, None)

    def get_release(self, event):
        if event.type != pygame.KEYUP:
            return None

        return self.key_bindings.get(event.key)