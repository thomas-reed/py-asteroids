import pygame
import sys
from constants import (
  SCREEN_WIDTH,
  SCREEN_HEIGHT,
  ASTEROID_MIN_RADIUS,
  ASTEROID_KINDS,
  ASTEROID_SPAWN_RATE,
  ASTEROID_MAX_RADIUS
)
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
  print("Starting Asteroids!")
  pygame.init()
  clock = pygame.time.Clock()
  dt = 0
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()

  Player.containers = (updatable, drawable)
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

  Shot.containers = (shots, updatable, drawable)

  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = (updatable)
  asteroid_field = AsteroidField()

  # game loop
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    screen.fill("black")
    for obj in drawable:
      obj.draw(screen)
    for obj in updatable:
      obj.update(dt)
    for asteroid in asteroids:
      for shot in shots:
        if shot.collides_with(asteroid):
          asteroid.split()
          shot.kill()
      if asteroid.collides_with(player):
        print("Game Over!")
        sys.exit(0)

    pygame.display.flip()
    dt = clock.tick(60) / 1000

if __name__ == "__main__":
  main()