import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius
    
    def draw(self,screen):
        self.screen = screen
        pygame.draw.circle(self.screen,"white",self.position,self.radius,2)

    def update(self,dt):
        self.dt = dt
        self.position += (self.velocity * self.dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            split_angle = random.uniform(20,50)
            split_vector_1 = self.velocity.rotate(split_angle)
            split_vector_2 = self.velocity.rotate(-split_angle)
            split_radius = self.radius - ASTEROID_MIN_RADIUS
            split_asteroid_1 = Asteroid(self.position[0],self.position[1],split_radius)
            split_asteroid_1.velocity = split_vector_1 * 1.2
            split_asteroid_2 = Asteroid(self.position[0],self.position[1],split_radius)
            split_asteroid_2.velocity = split_vector_2 * 1.2
        