"""
Developer Notes:

The game resets if the snake collides with the walls and itself.
"""

import pygame
import sys

# Reference: https://en.wikipedia.org/wiki/Snake_(video_game_genre)


# initializes pygame engine
pygame.init() 


# width is the x-coordinate and height is the y-coordinate
# coordinates (0, 0) is regarded as the top left-most corner
width, height = 500, 300
screen = pygame.display.set_mode((width, height))
frames = 60
fps = pygame.time.Clock()


apple = None # pygmae.Rect()


class Snake:
    def __init__(self):
        # React(left, top, width, height) -> Rect
        self.vertebrae = [ pygame.Rect(50, 150, 10, 10) ]
        self.speed = 3    
        self.color = (68, 214, 44)

    def moveUp(self):
        for col in self.vertebrae:        
            col.y -= self.speed

    def moveDown(self):
        for col in self.vertebrae:        
            col.y += self.speed

    def moveLeft(self):
        for col in self.vertebrae: 
            col.x -= self.speed

    def moveRight(self):
        # self.head.x += self.speed
        for col in self.vertebrae: 
            col.x += self.speed

    def draw(self, screen):
        for col in self.vertebrae:        
            pygame.draw.rect(screen, self.color, col)


def main():
    snake = Snake()
    slither = None
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
        if keys[pygame.K_UP] and snake.vertebrae[0].top > 0:
            slither = snake.moveUp
        if keys[pygame.K_DOWN] and snake.vertebrae[0].bottom < height:
            slither = snake.moveDown
        if keys[pygame.K_LEFT] and snake.vertebrae[0].left > 0:
            slither = snake.moveLeft
        if keys[pygame.K_RIGHT] and snake.vertebrae[0].right < width:
            slither = snake.moveRight

        if slither is not None:
            slither()

        snake.draw(screen)
        pygame.display.update()
        fps.tick(frames)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
