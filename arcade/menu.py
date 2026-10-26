
import pygame


class ArcadeMenu:
    def __init__(self):
        self.options = [
            "Snake",
            "Space Defender",
            "Brick Breaker",
            "Quit"
        ]
        self.selected_index = 0

        self.title_font = pygame.font.Font(None, 80)
        self.option_font = pygame.font.Font(None, 42)
        self.subtitle_font = pygame.font.Font(None, 26)

    
    def handle_input(self, action):
        if action == "UP":
            self.selected_index = (
                self.selected_index - 1
            ) % len(self.options)

        elif action == "DOWN":
            self.selected_index = (
                self.selected_index + 1
            ) % len(self.options)

        elif action == "SELECT":
            return self.options[self.selected_index]

        elif action == "BACK":
            return "Quit"

        return None


    def draw(self, screen):
        screen.fill((25, 25, 45))

        title = self.title_font.render(
            "MINI ARCADE", True, (255, 180, 210)
        )
        title_rect = title.get_rect(center=(400, 120))
        screen.blit(title, title_rect)

        subtitle = self.subtitle_font.render(
            "SELECT YOUR GAME", True, (180, 190, 220)
        )
        subtitle_rect = subtitle.get_rect(center=(400, 180))
        screen.blit(subtitle, subtitle_rect)

        for index, option in enumerate(self.options):
            is_selected = index == self.selected_index

            color = (
                (255, 220, 130)
                if is_selected
                else (220, 220, 235)
            )

            prefix = "> " if is_selected else "  "

            text = self.option_font.render(
                prefix + option, True, color
            )

            text_rect = text.get_rect(
                center=(400, 270 + index * 65)
            )

            screen.blit(text, text_rect)
