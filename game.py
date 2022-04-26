
import alien
import pygame

# class to help contorl and update the game
class Game():

    def __init__(self, player_ship, alien_group, player_bullet_group, alien_bullet_group, display_surface):
        # set game data
        self.level = 1
        self.score = 0
        pygame.init()
        
        self.player_ship = player_ship
        self.alien_group = alien_group
        self.player_bullet_group = player_bullet_group
        self.alien_bullet_group = alien_bullet_group
        self.display_surface = display_surface

        # set sound and music 
        self.new_level_sound = pygame.mixer.Sound("resources/new_round.wav")
        self.breach_sound = pygame.mixer.Sound("resources/breach.wav")
        self.alien_hit_sound = pygame.mixer.Sound("resources/alien_hit.wav")
        self.player_hit_sound = pygame.mixer.Sound("resources/player_hit.wav")

        # set font
        self.font = pygame.font.Font(pygame.font.get_default_font(), 20)


    # update the game
    def update(self):
       """ 
            For each iteration of the loop, the following needs to be checked:
            1. shift aliens down?
            2. check collision
            3. check level completion
       """
       self.move_aliens()
       self.check_collisions()
       self.check_level_completion()

    # draw the HUB and other information on display
    def draw(self):
        white = (255, 255, 255)

        # set text in HUB
        score = self.font.render("Score: " + str(self.score), True, white)
        score_rect = score.get_rect()
        score_rect.centerx = 600
        score_rect.top = 10

        level = self.font.render("Level: " + str(self.level), True, white)
        level_rect = level.get_rect()
        level_rect.topleft = (20, 10)

        life = self.font.render("Life: " + str(self.player_ship.lives), True, white)
        life_rect = level.get_rect()
        life_rect.topleft = (1100, 10)

        # draw HUB
        self.display_surface.blit(score, score_rect)
        self.display_surface.blit(level, level_rect)
        self.display_surface.blit(life, life_rect)

        pygame.draw.line(self.display_surface, white, (0, 50), (1200, 50), 4)
        pygame.draw.line(self.display_surface, white, (0, 600), (1200, 600), 4)
        
    # aliens will be moving horizontally until they hit the border of the game, they will then move down
    # and starting move in the opposite horizontal direction
    def move_aliens(self):
        shift = False

        # if aliens touch the border then move them down and change direction
        for alien in self.alien_group.sprites():
            if alien.rect.left <= 0 or alien.rect.right >= 1200:
                shift = True
        
        # shift aliens down
        if shift:
            breach = False
            # aliens will be shifted down more as the level increases
            for alien in self.alien_group.sprites():
                alien.rect.y += 8 * self.level

                # reverse direction
                alien.direction = -1 * alien.direction
                alien.rect.x += alien.direction * alien.velocity

                # check if aliens breached the defense line
                if alien.rect.bottom >= 600:
                    breach = True
            
            if breach:
                self.breach_sound.play()
                self.player_ship.lives -= 1
                self.check_player_died()

    """
        check collision between the following
        1. player and alien bullet
        2. player and alien 
        3. alien and player bullet
    """
    def check_collisions(self):
        if pygame.sprite.groupcollide(self.player_bullet_group, self.alien_group, True, True):
            self.alien_hit_sound.play()
            self.score += 1
        if pygame.sprite.spritecollide(self.player_ship, self.alien_bullet_group, True):
            self.player_hit_sound.play()
            self.player_ship.lives -= 1
            self.check_player_died()

    # check if the player has completed the current level
    def check_level_completion(self):
        if not (self.alien_group):
            self.level += 1
            self.start_new_level()

    # start a new game
    def start_new_level(self):

        # place the enemy fleets
        for i in range(11):
            for j in range(5):
                if j == 1:
                    alien_obj = alien.Alien(64 + i*64, 64 + j*64, self.level, self.alien_bullet_group, "resources/green.png")
                    self.alien_group.add(alien_obj)
                if j == 2:
                    alien_obj = alien.Alien(64 + i*64, 64 + j*64, self.level, self.alien_bullet_group, "resources/red.png")
                    self.alien_group.add(alien_obj)
                if j == 3:
                    alien_obj = alien.Alien(64 + i*64, 64 + j*64, self.level, self.alien_bullet_group, "resources/yellow.png")
                    self.alien_group.add(alien_obj)
                if j == 4:
                    alien_obj = alien.Alien(64 + i*64, 64 + j*64, self.level, self.alien_bullet_group, "resources/extra.png")
                    self.alien_group.add(alien_obj)

        self.new_level_sound.play()

    # check if player died
    def check_player_died(self):
        if self.player_ship.lives <= 0:
            self.player_bullet_group.empty()
            self.alien_bullet_group.empty()
            self.player_ship.reset()
            self.reset_game()

            for alien in self.alien_group:
                alien.reset()

    def reset_game(self):
        self.player_bullet_group.empty()
        self.alien_bullet_group.empty()
        self.score = 0
        self.level = 1

        self.alien_group.empty()

        self.player_ship.lives = 5
        self.player_ship.reset()

        