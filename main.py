import sys
import pygame
from constants import *  
from player import Player 
from asteroid import Asteroid  
from asteroidfield import AsteroidField  
import circleshape

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
    asteroid_field = AsteroidField()  

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

        for i in asteroids:
            if i.collision(player):
                print("Game Over")
                sys.exit()

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
