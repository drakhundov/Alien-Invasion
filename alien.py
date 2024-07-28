import random

import pygame

import config


class Alien(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = pygame.image.load("assets/sprites/" + config.ALIEN_SPRITE)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = random.randint(
            self.screen_rect.left, self.screen_rect.right
        )
        self.rect.centery = 10 + self.screen_rect.top + self.rect.height
        self.x = float(self.rect.centerx)
        self.y = float(self.rect.centery)

    def set_pos(self, new_pos, axis="x"):
        if axis == "x":
            self.x = new_pos
            self.rect.centerx = self.x
        elif axis == "y":
            self.y = new_pos
            self.rect.centery = self.y

    def blit(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.x += config.fleet_dir * 0.1
        self.rect.centerx = self.x


def fleet(screen, naliens=3, space=config.FREE_SPACE):
    """
    Creates `naliens` number of aliens with `space` distance in between.
    """
    aliens = pygame.sprite.Group()
    if naliens > (max_naliens := max_aliens_for_screen(screen, space)):
        # If `naliens` number of aliens don't fit in a single row,
        # divide them into several ones.
        # A list of number of aliens at each row.
        # for example, rows = [10, 10] means two rows 10 aliens each.
        rows = []
        while naliens >= max_naliens:
            rows.append(max_naliens)
            naliens -= max_naliens
        rows.append(naliens)
    else:
        # If all aliens fit the screen, put them in a single row.
        rows = [naliens]
    alien_width = (config.SCREEN_WIDTH - space * 2) / max_naliens
    alien_height = ((config.SCREEN_HEIGHT / 2.5) - space * 2.5) / len(rows)
    for row_no, naliens in enumerate(rows):
        for col_no in range(naliens):
            alien = Alien(screen)
            alien.set_pos(space + (alien_width / 2) + (alien_width * col_no), "x")
            alien.set_pos(space / 2 + (alien_height / 2) + (alien_height * row_no), "y")
            aliens.add(alien)
    return aliens


def max_aliens_for_screen(screen, space=config.FREE_SPACE):
    alien = Alien(screen)
    max_count = alien.screen_rect.width // (alien.rect.width + space)
    return max_count if max_count > 1 else -1
