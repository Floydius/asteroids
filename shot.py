from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.x = x
        self.y = y
    
    def draw(self,screen):
        self.screen = screen
        pygame.draw.circle(self.screen,"white",self.position,self.radius,1)

    def update(self,dt):
        self.dt = dt
        self.position += (self.velocity * self.dt)