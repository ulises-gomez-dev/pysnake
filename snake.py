import pygame
import sys

# Reference: https://en.wikipedia.org/wiki/Snake_(video_game_genre)


# initializes pygame engine
pygame.init() 


# width is the x-coordinate and height is the y-coordinate
# coordinates (0, 0) is regarded as the top-left most corner
width, height = 500, 300
screen = pygame.display.set_mode((width, height))
fps = pygame.time.Clock()


apple = None # pygmae.Rect()


class Snake:
    def __init__(self):
        # React(left, top, width, height) -> Rect
        self.head = pygame.Rect(250, 150, 10, 10)
        self.body = [ self.head ]
        self.speed = 5    

    def moveUp(self):
        self.head.y -= self.speed

    def moveDown(self):
        self.head.y += self.speed

    def moveLeft(self):
        self.head.x -= self.speed

    def moveRight(self):
        self.head.x += self.speed


def main():
    snake = Snake()

    running = True
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and snake.head.top > 0:
            snake.moveUp()
        if keys[pygame.K_DOWN] and snake.head.bottom < height:
            snake.moveDown()
        if keys[pygame.K_LEFT] and snake.head.left > 0:
            snake.moveLeft()
        if keys[pygame.K_RIGHT] and snake.head.right < width:
            snake.moveRight()

        pygame.draw.rect(screen, (68, 214, 44), snake.head)
        pygame.display.update()
        fps.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
