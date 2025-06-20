import pygame
from constants import (
  SCREEN_WIDTH,
  SCREEN_HEIGHT,
  ASTEROID_MIN_RADIUS,
  ASTEROID_KINDS,
  ASTEROID_SPAWN_RATE,
  ASTEROID_MAX_RADIUS
)
from player import Player

def main():
  print("Starting Asteroids!")
  pygame.init()
  clock = pygame.time.Clock()
  dt = 0
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  Player.containers = (updatable, drawable)
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

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
    pygame.display.flip()
    dt = clock.tick(60) / 1000

if __name__ == "__main__":
  main()