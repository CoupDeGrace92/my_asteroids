from circleshape import CircleShape
import pygame
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = SHOT_RADIUS
        self.position = pygame.Vector2(self.x,self.y)
        self.velocity_vector = pygame.Vector2(0,0)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,0), (int(self.position.x),int(self.position.y)), self.radius, 2)


    def update(self,dt):
        self.position += self.velocity_vector *dt
