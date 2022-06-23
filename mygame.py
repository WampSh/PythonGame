import pygame, controls
from bullet import Bullet
from gun import Gun
from pygame.sprite import Group
def run():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("space oddity")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    while True:
        controls.events(screen, gun, bullets)
        gun.update_gun()
        bullets.update()
        controls.update(bg_color, screen, gun, bullets)

run()
