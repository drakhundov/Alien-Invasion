import pygame
import config


class Ship:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load(config.SHIP_SPRITE)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 10
        self.direction = 0
        self.speed = 1
        # horizontal
        self.pos = float(self.rect.centerx)
        self.bullets_allowed = 1

    def blit(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        new_pos = self.pos + self.speed * self.direction
        size = self.rect.SCREEN_WIDTH / 2
        if size < new_pos < self.screen_rect.right - size:
            self.pos = new_pos
            self.rect.centerx = self.pos
