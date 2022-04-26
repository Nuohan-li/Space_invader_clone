import pygame

class AlienBullet(pygame.sprite.Sprite):

    def __init__(self, x, y, alien_bullet_group):
        super().__init__()
        
        self.image = pygame.image.load("resources/red_bullet.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

        self.velocity = 5
        alien_bullet_group.add(self)

    def update(self):
        self.rect.y += self.velocity

        if self.rect.top > 700:
            self.kill()

    