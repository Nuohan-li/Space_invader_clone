import pygame
import player_bullet

# a class to model the player space ship
class Player(pygame.sprite.Sprite):

    def __init__(self, player_bullet_group):
        super().__init__()
        self.player_bullet_group = player_bullet_group

        # load the player ship image, and get the rectangle containing the image to set x,y coordinates
        self.image = pygame.image.load("resources/player.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = 600
        self.rect.bottom = 700

        self.lives = 5
        self.velocity = 5

        self.shoot_sound = pygame.mixer.Sound("resources/player_fire.wav")

        
    # update the player
    def update(self):
        keys = pygame.key.get_pressed()

        # move the player ship to the left if left or right key is pressed, and making sure that the player will not 
        # cross the border
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT] and self.rect.right < 1200:
            self.rect.x += self.velocity

    # fire a bullet 
    def fire(self):
        # restrict the number a bullet on sreen at same time 
        if len(self.player_bullet_group) < 10:
            self.shoot_sound.play()
            player_bullet.PlayerBullet(self.rect.centerx, self.rect.centery, self.player_bullet_group)

    # reset player position
    def reset(self):
        self.rect.centerx = 600
    