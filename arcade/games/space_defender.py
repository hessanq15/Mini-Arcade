
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
            15,
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

    def draw(self, screen):
        screen.fill((16, 22, 41))

        pygame.draw.rect(
            screen, (163, 221, 196), self.player,
            border_radius=8
        )

        for bullet in self.bullets:
            pygame.draw.rect(
                screen, (249, 212, 108), bullet,
                border_radius=3
            )
