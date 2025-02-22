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


# React(left, top, width, height) -> Rect
snakeHead = pygame.Rect(250, 150, 10, 10)
apple = None # pygmae.Rect()


def main():
    running = True
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            snakeHead.y -= 5
        if keys[pygame.K_DOWN]:
            snakeHead.y += 5
        if keys[pygame.K_LEFT]:
            snakeHead.x -= 5
        if keys[pygame.K_RIGHT]:
            snakeHead.x += 5

        pygame.draw.rect(screen, (68, 214, 44), snakeHead)
        pygame.display.update()
        fps.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
