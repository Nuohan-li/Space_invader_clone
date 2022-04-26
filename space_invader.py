import pygame
import player
import game

# initialize pygame
pygame.init()

# set display 
win_width = 1200
win_height = 700
display_surface = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Space Invader")

# set FPS and clock
FPS = 60
clock = pygame.time.Clock()

# sprite groups
player_bullet_group = pygame.sprite.Group()
alien_bullet_group = pygame.sprite.Group()

player_group = pygame.sprite.Group()
player_ship = player.Player(player_bullet_group)
player_group.add(player_ship)

# creating alien group, alien objects will be added by game's start_new_level function, as aliens will become
# stronger as level goes on
alien_group = pygame.sprite.Group()

game_obj = game.Game(player_ship, alien_group, player_bullet_group, alien_bullet_group, display_surface)
game_obj.start_new_level()

# main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # check if space is pressed, player will fire if it is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_ship.fire()
        
            if event.key == pygame.K_ESCAPE:
                running = False


    # drawing each groups on the display 
    display_surface.fill((0,0,0))

    # update() will be called on each of the sprite contained in the group, in this case, Player.update will be called
    # see https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Group.update
    player_group.update()
    player_group.draw(display_surface)

    alien_group.update()
    alien_group.draw(display_surface)

    player_bullet_group.update()
    player_bullet_group.draw(display_surface)

    alien_bullet_group.update()
    alien_bullet_group.draw(display_surface)

    game_obj.update()
    game_obj.draw()
    # update the game display and tick clock
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()