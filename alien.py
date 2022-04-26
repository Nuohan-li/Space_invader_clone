import random
import pygame
import alien_bullet

# a class to model the aliens 
class Alien(pygame.sprite.Sprite):

    def __init__(self, x, y, velocity, alien_bullet_group, image_url):
        super().__init__()
        self.image = pygame.image.load(image_url)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.starting_x = x
        self.starting_y = y

        self.direction = 1
        self.velocity = velocity
        self.alien_bullet_group = alien_bullet_group

        self.shoot_sound = pygame.mixer.Sound("resources/alien_fire.wav")
    
    # update the aliens
    def update(self):

        # if direction = 1, then aliens will move to the right, if direction = -1, then they will move to the left
        self.rect.x += self.direction * self.velocity

        # randomly fire a bullet
        if random.randint(0, 1000) > 998:
            self.shoot_sound.play()
            self.fire()

    # fire a bullet 
    def fire(self):
        alien_bullet.AlienBullet(self.rect.centerx, self.rect.bottom, self.alien_bullet_group)
    

    # reset alien position
    def reset(self):
        self.rect.topleft = (self.starting_x, self.starting_y)
        self.direction = 1 