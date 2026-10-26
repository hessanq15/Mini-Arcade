
import pygame


class SpaceDefender:
    def __init__(self):
        self.player = pygame.Rect(375, 520, 50, 35)
        self.player_speed = 6

        self.bullets = []
        self.bullet_speed = 8
        self.last_shot = 0
        self.shoot_delay = 250

        self.move_left = False
        self.move_right = False

        self.enemies = []

        for row in range(2):
            for column in range(6):
                enemy = pygame.Rect(
                    100 + column * 100,
                    70 + row * 60,
                    40,
                    30
                )
                self.enemies.append(enemy)

        self.enemy_speed = 2
        self.enemy_direction = 1

        self.score = 0
        self.score_font = pygame.font.Font(None, 36)

    def handle_input(self, action, pressed=True):
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

    def update(self):
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
            enemy.x += self.enemy_speed * self.enemy_direction

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
            f"Score: {self.score}",
            True,
            (255, 255, 255)
        )

        screen.blit(score_text, (20, 20))
