from circleshape import *
from constants import *
import random
class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)


    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20,50)
        new_left_vector = self.position.rotate(angle)
        new_right_vector = self.position.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        lefty = Asteroid(self.position.x,self.position.y,new_radius)
        righty = Asteroid(self.position.x,self.position.y, new_radius)
        lefty.velocity = new_left_vector *1.2
        righty.velocity = new_right_vector*1.2