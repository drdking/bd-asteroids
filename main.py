import pygame
#from constants import *
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    game_clock = pygame.time.Clock()        # Sets up Game clock and Delta time variables/functions
    dt = 0


    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    #screen_size = (SCREEN_WIDTH, SCREEN_HEIGHT)

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        pygame.display.flip()

        dt = game_clock.tick(60) / 1000
        # print(dt)                      # Pauses the game until 1/60th of a second passes




if __name__ == "__main__":
    main()
