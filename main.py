import pygame
from constants import *
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0), rect=None, special_flags=0)
        pygame.display.flip()
#This is the pythonic way to run main() to ensure it only runs when this file is called and not another file
if __name__ == "__main__":
    main()
