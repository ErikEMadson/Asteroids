import circleshape
import pygame
import constants
import random

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        deflection = random.uniform(20, 50)
        cw_velocity = 1.2 * self.velocity.rotate(deflection)
        ccw_velocity = 1.2 * self.velocity.rotate(-deflection)
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
        cw_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        ccw_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        cw_asteroid.velocity = cw_velocity
        ccw_asteroid.velocity = ccw_velocity
