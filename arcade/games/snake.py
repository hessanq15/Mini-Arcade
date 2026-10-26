
import pygame
import random


class Snake:
    def __init__(self):
        self.cell_size = 25
        self.snake = [(10, 10), (9, 10), (8, 10)]
        self.direction = (1, 0)
        self.next_direction = self.direction
        self.move_delay = 150
        self.last_move = pygame.time.get_ticks()
        self.score = 0
        self.score_font = pygame.font.Font(None, 36)
        self.food = self.spawn_food()
        self.game_over = False
        self.game_over_font = pygame.font.Font(None, 64)


    
    def spawn_food(self):
        columns = 800 // self.cell_size
        rows = 600 // self.cell_size

        empty_cells = [
            (x, y)
            for x in range(columns)
            for y in range(rows)
            if (x, y) not in self.snake
        ]

        if not empty_cells:
            return None

        return random.choice(empty_cells)



    def handle_input(self, action):

        if self.game_over:
            if action == "SELECT":
                self.__init__()
                return
            
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

        if self.game_over:
            return
        
        now = pygame.time.get_ticks()

        if now - self.last_move < self.move_delay:
            return

        self.last_move = now
        self.direction = self.next_direction

        head_x, head_y = self.snake[0]
        dx, dy = self.direction

        new_head = (head_x + dx, head_y + dy)

        
        columns = 800 // self.cell_size
        rows = 600 // self.cell_size

        x, y = new_head

        if x < 0 or x >= columns or y < 0 or y >= rows:
            self.game_over = True
            return

        growing = new_head == self.food

        if growing:
            body = self.snake
        else:
            body = self.snake[:-1]

        if new_head in body:
            self.game_over = True
            return


        
        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.score += 10
            self.food = self.spawn_food()
        else:
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

        
        if self.food is not None:
            food_x, food_y = self.food

            food_rect = pygame.Rect(
                food_x * self.cell_size,
                food_y * self.cell_size,
                self.cell_size - 2,
                self.cell_size - 2,
            )

            pygame.draw.rect(
                screen,
                (255, 210, 120),
                food_rect,
                border_radius=8,
            )

        score_text = self.score_font.render(
            f"Score: {self.score}", True, (255, 255, 255)
        )

        screen.blit(score_text, (20, 20))

        
        if self.game_over:
            overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
            overlay.fill((15, 15, 30, 190))
            screen.blit(overlay, (0, 0))

            title = self.game_over_font.render(
                "GAME OVER", True, (255, 180, 210)
            )

            message = self.score_font.render(
                f"Final score: {self.score}", True, (255, 255, 255)
            )

            restart = self.score_font.render(
                "Press Enter to play again", True, (220, 220, 235)
            )

            screen.blit(title, title.get_rect(center=(400, 230)))
            screen.blit(message, message.get_rect(center=(400, 300)))
            screen.blit(restart, restart.get_rect(center=(400, 360)))


