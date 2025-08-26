import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
def main():
    pygame.init
    updateables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updateables, drawables)
    Asteroid.containers = (asteroids, updateables, drawables)
    AsteroidField.containers = (updateables)
    field = AsteroidField()
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
        updateables.update(dt)
        pygame.Surface.fill(screen, black)
        for entity in drawables:
            entity.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
      
if __name__ == "__main__":
    main()
