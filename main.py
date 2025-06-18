import pygame
from constants import (
  SCREEN_WIDTH,
  SCREEN_HEIGHT,
  ASTEROID_MIN_RADIUS,
  ASTEROID_KINDS,
  ASTEROID_SPAWN_RATE,
  ASTEROID_MAX_RADIUS
)

def main():
  print("Starting Asteroids!")
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  # game loop
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    screen.fill("black")
    pygame.display.flip()

if __name__ == "__main__":
  main()