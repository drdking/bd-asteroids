import pygame
#from constants import *
from constants import *
from logger import log_state
from player import *


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    game_clock = pygame.time.Clock()        # Sets up Game clock and Delta time variables/functions
    dt = 0


    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PALYER_RADIUS)
    

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        player.update(dt)

        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()

        dt = game_clock.tick(60) / 1000
        # print(dt)                      # Pauses the game until 1/60th of a second passes




if __name__ == "__main__":
    main()
