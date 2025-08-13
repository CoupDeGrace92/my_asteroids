from circleshape import CircleShape
import pygame
import random
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)


    def draw(self, screen):
        pygame.draw.circle(screen, (148,92,92), (int(self.position.x),int(self.position.y)), self.radius, 2)


    def update(self,dt):
        self.position += self.velocity*dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20,50)
            self.velocity1 = self.velocity.rotate(angle)
            self.velocity2 = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = self.velocity1*random.uniform(.8,1.5)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2.velocity = self.velocity2*random.uniform(.8,1.5)
