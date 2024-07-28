import pygame
from pygame.sprite import Sprite

import config


class Bullet(Sprite):
    def __init__(self, screen, ship):
        Sprite.__init__(self)
        self.screen = screen
        self.rect = pygame.Rect(
            0, 0, config.BULLET_SCREEN_WIDTH, config.BULLET_SCREEN_HEIGHT
        )
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.speed = 2
        # vertical
        self.pos = float(self.rect.centery)

    def blit(self):
        pygame.draw.rect(self.screen, config.BULLET_COLOR, self.rect)

    def update(self):
        self.pos -= self.speed
        self.rect.centery = self.pos
        if self.pos <= 0:
            self.kill()
