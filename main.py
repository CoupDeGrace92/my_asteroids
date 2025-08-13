import pygame
import sys
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pygame.time.Clock()

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    dt = 0


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    players = pygame.sprite.Group()

    Player.containers = (updatable, drawable, players)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (updatable, shots, drawable)

    asteroidfield = AsteroidField()
    main_player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)

    collision = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0), rect=None, special_flags=0)
        updatable.update(dt)
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000
        for asteroid in asteroids:
            collision = main_player.collision_check(asteroid)
            if  collision == True:
                sys.exit("Game Over!")
            


#This is the pythonic way to run main() to ensure it only runs when this file is called and not another file
if __name__ == "__main__":
    main()
