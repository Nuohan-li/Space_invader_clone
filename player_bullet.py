import pygame

class PlayerBullet(pygame.sprite.Sprite):

    """
        initialize the initial position of bullets fired by player, the bullet will be fired from the 
        center of the player and the position will be updated as the player moves, hence the x and y 
        of the bullet will be set to the player's current x, y position
    """
    def __init__(self, ship_x, ship_y, bullet_group):
        super().__init__()
        
        self.image = pygame.image.load("resources/green_bullet.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = ship_x
        self.rect.centery = ship_y

        self.velocity = 15  
        bullet_group.add(self)

    def update(self):
        self.rect.y -= self.velocity

        if self.rect.bottom < 0:
            self.kill()
    