import pygame

import alien
import config
import events
import game
from ship import Ship


def main():
    pygame.init()
    screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
    pygame.display.set_caption(config.TITLE)
    ship = Ship(screen)
    bullets = pygame.sprite.Group()
    aliens_count = alien.max_aliens_for_screen(screen, config.FREE_SPACE)
    aliens = alien.fleet(screen, aliens_count)
    while True:
        events.check(screen, ship, bullets)
        if not aliens:
            aliens_count += 1
            aliens = alien.fleet(screen, aliens_count)
        game.update(screen, ship, bullets, aliens)


main()
