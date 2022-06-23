import pygame

class Gun():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load()
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False
        self.mup = False
        self.mdown = False

    def output(self):
        self.screen.blit(self.image, self.rect)

    def update_gun(self):
       if self.mright and self.rect.right < self.screen_rect.right:
           self.rect.centerx += 1
       if self.mleft and self.rect.left > self.screen_rect.left:
           self.rect.centerx -= 1
       if self.mup and self.rect.top > self.screen_rect.top:
           self.rect.centery -= 1
       if self.mdown and self.rect.bottom < self.screen_rect.bottom:
           self.rect.centery += 1
