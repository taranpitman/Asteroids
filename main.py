import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
def main():
    pygame.init()
    tim = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    allAsteroids = pygame.sprite.Group()
    allShots = pygame.sprite.Group()
    Asteroid.containers = (updatable, drawable, allAsteroids)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (allShots, updatable, drawable)
    player = Player((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))
    asteroid_field = AsteroidField()
    dt = 0
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    i = 1
    while i == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for updat in updatable:
            updat.update(dt)
        for drawa in drawable:
            drawa.draw(screen)
        for colli in allAsteroids:
            if colli.collisions(player):
                print("Game over!")
                sys.exit()
            for shots in allShots:
                if colli.collisions(shots):
                    shots.kill()
                    Asteroid.split(colli)
        pygame.display.flip()
        dt = tim.tick(60) / 1000
if __name__ == "__main__":
    main()