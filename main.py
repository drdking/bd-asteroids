import pygame
#from constants import *
from constants import *
from logger import log_state
from player import *
from asteroid import *
from asteroidfield import *





def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    game_clock = pygame.time.Clock()        # Sets up Game clock and Delta time variables/functions
    dt = 0

    #Defines the screen size
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))


    # Creating Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable) # adds player class to group

    Asteroid.containers = (updatable, drawable, asteroids)

    AsteroidField.containers = (updatable)
    #Creates the player ship
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PALYER_RADIUS)

    a_field = AsteroidField()
    

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #player.update(dt) -- Changed to using Groups
        updatable.update(dt)

        screen.fill("black")

        #player.draw(screen) Updated to containers
        #Iterating over drawable container to draw objects
        for ob in drawable:
            ob.draw(screen)



        pygame.display.flip()

        dt = game_clock.tick(60) / 1000
        # print(dt)    Pauses the game until 1/60th of a second passes




if __name__ == "__main__":
    main()
