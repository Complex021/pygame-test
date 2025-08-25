import pygame
from constants import *
from player import *
def main():
    pygame.init
    black = pygame.Color('black')
    dt = 0
    clock = pygame.time.Clock()
    PlayerCharacter = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 )  
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, black)
        PlayerCharacter.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 100
      
if __name__ == "__main__":
    main()
