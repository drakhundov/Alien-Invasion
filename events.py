import sys

import pygame

from bullet import Bullet

right = [pygame.K_RIGHT, pygame.K_d]
left = [pygame.K_LEFT, pygame.K_a]


def keydown(key, screen, ship, bullets):
    if key in right:
        ship.direction = 1
    if key in left:
        ship.direction = -1
    if key == pygame.K_SPACE and ship.bullets_allowed > len(bullets):
        bullet = Bullet(screen, ship)
        bullets.add(bullet)
    if key == pygame.K_q:
        sys.exit()


def keyup(key, ship):
    if key in left + right:
        ship.direction = 0


def check(screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            keydown(event.key, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            keyup(event.key, ship)
