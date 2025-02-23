"""
Developer Notes:

The game resets if the snake collides with the walls and itself.
"""

import pygame
import sys
import random

# Reference: https://en.wikipedia.org/wiki/Snake_(video_game_genre)


# initializes pygame engine
pygame.init() 


# width is the x-coordinate and height is the y-coordinate
# coordinates (0, 0) is regarded as the top left-most corner
width, height = 500, 300
screen = pygame.display.set_mode((width, height))
frames = 60
fps = pygame.time.Clock()


class Snake:
    def __init__(self):
        # React(left, top, width, height) -> Rect
        self.head = []
        self.speed = 3    
        self.color = (68, 214, 44)

        self.head.append(pygame.Rect(50, 150, 10, 10))

    def getHead(self):
        return self.head[0]

    def getTop(self):
        snakeHead = self.getHead()
        return snakeHead.top

    def getBottom(self):
        snakeHead = self.getHead()
        return snakeHead.bottom
        
    def getLeft(self):
        snakeHead = self.getHead()
        return snakeHead.left

    def getRight(self):
        snakeHead = self.getHead()
        return snakeHead.right

    def moveUp(self):
        self.update()
        self.head[0].y -= self.speed        

    def moveDown(self):
        self.update()
        self.head[0].y += self.speed

    def moveLeft(self):
        self.update()
        self.head[0].x -= self.speed

    def moveRight(self):
        self.update()
        self.head[0].x += self.speed

    def add(self, direction):
        snakeTail = self.head[-1]
        newSnakeTail = pygame.Rect(snakeTail.left, snakeTail.top, 10, 10) # can you make a copy of the reference 

        if direction == 'u':
            newSnakeTail.top += 10
        elif direction == 'd':
            newSnakeTail.top -= 10
        elif direction == 'l':
            newSnakeTail.left += 10
        elif direction == 'r':
            newSnakeTail.left -= 10
        
        self.head.append(newSnakeTail)   


    def update(self):
        x_curr, y_curr = self.head[0].x, self.head[0].y
        for current in self.head[1:]:
            x_prev, y_prev = current.x, current.y
            current.x, current.y = x_curr, y_curr
            x_curr, y_curr = x_prev, y_prev


    def draw(self, screen):
        for current in self.head:
            pygame.draw.rect(screen, self.color, current)

    def reset(self):
        del self.head[1:]

        snakeHead = self.getHead()
        snakeHead.x, snakeHead.y = 50, 150


class Apple:
    def __init__(self):
        self.apple = pygame.Rect(250, 150, 10, 10)
        self.color = (255, 0, 0)

    def draw(self, screen):
        pygame.draw.ellipse(screen, self.color, self.apple)
    
    def reset(self):
        self.apple.x, self.apple.y = 250, 150

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

        if snake.getTop() <= 0 or snake.getBottom() >= height or snake.getLeft() <= 0 or snake.getRight() >= width:
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

            apple.apple.x = random.randrange(0, 500, 10)
            apple.apple.y = random.randrange(0, 300, 10)

        pygame.display.update()
        fps.tick(frames)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
