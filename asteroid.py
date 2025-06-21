import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)

  def draw(self, screen):
    pygame.draw.circle(
      screen,
      "white",
      self.position,
      self.radius,
      2
    )

  def update(self, dt):
    self.position += self.velocity * dt

  def split(self):
    self.kill()
    if self.radius == ASTEROID_MIN_RADIUS:
      return
    split_angle = random.uniform(10, 60)
    new_speed = random.uniform(1.1, 1.5)
    vect1 = self.velocity.rotate(split_angle)
    vect2 = self.velocity.rotate(-split_angle)
    new_radius = self.radius - ASTEROID_MIN_RADIUS
    asteroid1 = Asteroid(
      self.position.x,
      self.position.y,
      new_radius
    )
    asteroid1.velocity = vect1 * 1.3
    asteroid2 = Asteroid(
      self.position.x,
      self.position.y,
      new_radius
    )
    asteroid2.velocity = vect2 * 1.3

