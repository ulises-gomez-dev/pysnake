"""
Developer Notes:

The game resets if the snake collides with the walls and itself.
Snake needs to detect whether it collided with itself.
"""

import pygame
import sys
import random
from config import width, height, frames
from src.snake import Snake
from src.apple import Apple

# Reference: https://en.wikipedia.org/wiki/Snake_(video_game_genre)


# initializes pygame engine
pygame.init() 


# width is the x-coordinate and height is the y-coordinate
# coordinates (0, 0) is regarded as the top left-most corner
screen = pygame.display.set_mode((width, height))
fps = pygame.time.Clock()


def main():
    snake = Snake()
    apple = Apple()
    slither = None
    direction = None
    # we need to set the current direction because snake can't go the opposite direction

    running = True
    while running:
        # draw all our elements
        # update everything
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and snake.getTop() > 0 and direction != 'd':
            slither = snake.moveUp
            direction = 'u'

        if keys[pygame.K_DOWN] and snake.getBottom() < height and direction != 'u':
            slither = snake.moveDown
            direction = 'd'

        if keys[pygame.K_LEFT] and snake.getLeft() > 0 and direction != 'r':
            slither = snake.moveLeft
            direction = 'l'

        if keys[pygame.K_RIGHT] and snake.getRight() < width and direction != 'l':
            slither = snake.moveRight
            direction = 'r'

        if snake.getTop() <= 0 or snake.getBottom() >= height or snake.getLeft() <= 0 or snake.getRight() >= width or snake.collision():
            # resets game 
            snake.reset() # use inheritance to update apple when snake resets
            apple.reset()
            slither = None
            direction = None

        if slither is not None:
            slither()

        snake.draw(screen)
        apple.draw(screen)

        snakeHead = snake.getHead()
        if snakeHead.colliderect(apple.apple):
            snake.add(direction)
            # make snake grow 3 times faster
            # snake.add(direction)
            # snake.add(direction)

            apple.apple.x = random.randrange(10, width - 10, 10)
            apple.apple.y = random.randrange(10, height - 10, 10)

        pygame.display.update()
        fps.tick(frames)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
