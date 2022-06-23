import pygame, sys
from bullet import Bullet

def events(screen, gun, bullets):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    gun.mright = True
                elif event.key == pygame.K_LEFT:
                    gun.mleft = True
                elif event.key == pygame.K_UP:
                    gun.mup = True
                elif event.key == pygame.K_DOWN:
                    gun.mdown = True
                elif event.key == pygame.K_SPACE:
                    new_bullet = Bullet(screen, gun)
                    bullets.add(new_bullet)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    gun.mright = False
                elif event.key == pygame.K_LEFT:
                    gun.mleft = False
                elif event.key == pygame.K_UP:
                    gun.mup = False
                elif event.key == pygame.K_DOWN:
                    gun.mdown = False

def update(bg_color, screen, gun, bullets):
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    pygame.display.flip()
