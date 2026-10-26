
import pygame


class Snake:
    def __init__(self):
        self.cell_size = 25
        self.snake = [(10, 10), (9, 10), (8, 10)]
        self.direction = (1, 0)
        self.next_direction = self.direction
        self.move_delay = 150
        self.last_move = pygame.time.get_ticks()

    def handle_input(self, action):
        directions = {
            "UP": (0, -1),
            "DOWN": (0, 1),
            "LEFT": (-1, 0),
            "RIGHT": (1, 0),
        }

        if action in directions:
            new_direction = directions[action]

            if new_direction != (
                -self.direction[0],
                -self.direction[1],
            ):
                self.next_direction = new_direction

    def update(self):
        now = pygame.time.get_ticks()

        if now - self.last_move < self.move_delay:
            return

        self.last_move = now
        self.direction = self.next_direction

        head_x, head_y = self.snake[0]
        dx, dy = self.direction

        new_head = (head_x + dx, head_y + dy)

        self.snake.insert(0, new_head)
        self.snake.pop()

    def draw(self, screen):
        screen.fill((25, 25, 45))

        for index, (x, y) in enumerate(self.snake):
            color = (255, 180, 210) if index == 0 else (160, 220, 180)

            rect = pygame.Rect(
                x * self.cell_size,
                y * self.cell_size,
                self.cell_size - 2,
                self.cell_size - 2,
            )

            pygame.draw.rect(screen, color, rect, border_radius=5)
