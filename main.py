import pygame
from constants import *  # Ensure constants like SCREEN_WIDTH, SCREEN_HEIGHT are defined here
from player import Player  # Ensure the Player class is defined in player.py
from asteroid import Asteroid  # Ensure the Asteroid class is defined in asteroid.py
from asteroidfield import AsteroidField  # Ensure asteroidfield.py is accessible and correctly implemented


def main():
    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Sprite groups for update and draw management
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # Assign sprite groups to classes
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()  # Ensure this works after adjustments in asteroidfield.py

    Player.containers = (updatable, drawable)

    # Create a player instance at the center of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Delta time for frame-rate independent updates
    dt = 0

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Exit the game when the window is closed
                return

        # Update all updatable objects
        for obj in updatable:
            obj.update(dt)

        # Clear the screen
        screen.fill("black")

        # Draw all drawable objects
        for obj in drawable:
            obj.draw(screen)

        # Flip the display to show the updated frame
        pygame.display.flip()

        # Limit the frame rate to 60 FPS and calculate delta time
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
