import pygame

import config


def update(screen, ship, bullets, aliens):
    screen.fill(config.BG_COLOR)
    ship.update()
    ship.blit()
    for bullet in bullets.sprites():
        bullet.update()
        bullet.blit()
    pygame.sprite.groupcollide(bullets, aliens, True, True)
    for alien in aliens.sprites():
        if alien.rect.right > alien.screen_rect.right:
            config.fleet_dir = -1
        elif alien.rect.left < alien.screen_rect.left:
            config.fleet_dir = 1
        alien.update()
        alien.blit()
    pygame.display.flip()
