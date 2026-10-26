
import pygame

from arcade.score_manager import ScoreManager


class SpaceDefender:
    def __init__(self):
        self.player = pygame.Rect(375, 520, 50, 35)
        self.player_speed = 6

        self.move_left = False
        self.move_right = False

        self.bullets = []
        self.bullet_speed = 8
        self.last_shot = 0
        self.shoot_delay = 250

        self.score = 0
        self.lives = 3
        self.wave = 1
        self.game_over = False

        self.score_manager = ScoreManager()
        self.high_score = self.score_manager.get_high_score("Space Defender")

        self.score_font = pygame.font.Font(None, 32)
        self.title_font = pygame.font.Font(None, 64)

        self.enemies = []
        self.enemy_direction = 1
        self.enemy_speed = 2

        self.create_wave()

    def create_wave(self):
        self.enemies = []
        self.enemy_direction = 1
        self.enemy_speed = 2 + (self.wave - 1) * 0.5

        for row in range(2):
            for column in range(6):
                enemy = pygame.Rect(
                    100 + column * 100,
                    70 + row * 60,
                    40,
                    30
                )
                self.enemies.append(enemy)

    def handle_input(self, action, pressed=True):
        if self.game_over:
            if action == "SELECT" and pressed:
                self.__init__()
            return

        if action == "LEFT":
            self.move_left = pressed

        elif action == "RIGHT":
            self.move_right = pressed

        elif action == "SELECT" and pressed:
            self.shoot()

    def shoot(self):
        now = pygame.time.get_ticks()

        if now - self.last_shot < self.shoot_delay:
            return

        bullet = pygame.Rect(
            self.player.centerx - 3,
            self.player.top - 15,
            6,
            15
        )

        self.bullets.append(bullet)
        self.last_shot = now

    def lose_life(self):
        self.lives -= 1

        if self.lives <= 0:
            self.game_over = True
            self.score_manager.save_score("Space Defender", self.score)
            self.high_score = self.score_manager.get_high_score("Space Defender")
        else:
            self.bullets.clear()
            self.create_wave()

    def update(self):
        if self.game_over:
            return

        if self.move_left:
            self.player.x -= self.player_speed

        if self.move_right:
            self.player.x += self.player_speed

        self.player.clamp_ip(pygame.Rect(0, 0, 800, 600))

        for bullet in self.bullets[:]:
            bullet.y -= self.bullet_speed

            if bullet.bottom < 0:
                self.bullets.remove(bullet)

        for enemy in self.enemies:
            enemy.x += int(self.enemy_speed * self.enemy_direction)

        if self.enemies:
            hit_edge = any(
                enemy.right >= 800 or enemy.left <= 0
                for enemy in self.enemies
            )

            if hit_edge:
                self.enemy_direction *= -1

                for enemy in self.enemies:
                    enemy.y += 20

        for bullet in self.bullets[:]:
            for enemy in self.enemies[:]:
                if bullet.colliderect(enemy):
                    self.bullets.remove(bullet)
                    self.enemies.remove(enemy)
                    self.score += 10
                    break

        if any(enemy.bottom >= self.player.top for enemy in self.enemies):
            self.lose_life()
            return

        if not self.enemies:
            self.wave += 1
            self.bullets.clear()
            self.create_wave()

    def draw(self, screen):
        screen.fill((16, 22, 41))

        pygame.draw.rect(
            screen,
            (163, 221, 196),
            self.player,
            border_radius=8
        )

        for bullet in self.bullets:
            pygame.draw.rect(
                screen,
                (249, 212, 108),
                bullet,
                border_radius=3
            )

        for enemy in self.enemies:
            pygame.draw.rect(
                screen,
                (245, 155, 185),
                enemy,
                border_radius=6
            )

        score_text = self.score_font.render(
            f"Score: {self.score}", True, (255, 255, 255)
        )
        lives_text = self.score_font.render(
            f"Lives: {self.lives}", True, (255, 255, 255)
        )
        wave_text = self.score_font.render(
            f"Wave: {self.wave}", True, (255, 255, 255)
        )
        best_text = self.score_font.render(
            f"Best: {self.high_score}", True, (255, 255, 255)
        )

        screen.blit(score_text, (20, 20))
        screen.blit(lives_text, (20, 55))
        screen.blit(wave_text, (680, 20))
        screen.blit(best_text, (680, 55))

        if self.game_over:
            overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
            overlay.fill((10, 10, 25, 200))
            screen.blit(overlay, (0, 0))

            title = self.title_font.render(
                "GAME OVER", True, (255, 180, 210)
            )
            final_score = self.score_font.render(
                f"Final score: {self.score}", True, (255, 255, 255)
            )
            restart = self.score_font.render(
                "Press Enter to play again", True, (220, 220, 235)
            )

            screen.blit(title, title.get_rect(center=(400, 230)))
            screen.blit(final_score, final_score.get_rect(center=(400, 300)))
            screen.blit(restart, restart.get_rect(center=(400, 360)))
