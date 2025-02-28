import pygame
from config import snake_width, snake_height, snake_speed, green

class Snake:
    def __init__(self) -> None:
        # React(left, top, width, height) -> Rect
        self.snake: list[pygame.Rect] = []

        self.width: int = snake_width
        self.height: int = snake_height
        self.speed: int = snake_speed    
        self.color: tuple[int] = green

        self.snake.append(pygame.Rect(50, 150, snake_width, snake_height))

    def getHead(self):
        return self.snake[0]

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
        """
        updates the snake's position by "self.speed" number of pixels up;
        call self.update() before updating the body, this insures that each
        square inherits the previous squares position prior to updating the 
        head
        """
        self.update()
        self.snake[0].y -= self.speed        

    def moveDown(self):
        """
        updates the snake's position by "self.speed" number of pixels down;
        call self.update() before updating the body, this insures that each
        square inherits the previous squares position prior to updating the 
        head
        """
        self.update()
        self.snake[0].y += self.speed

    def moveLeft(self):
        """
        updates the snake's position by "self.speed" number of pixels to the left;
        call self.update() before updating the body, this insures that each
        square inherits the previous squares position prior to updating the 
        head
        """
        self.update()
        self.snake[0].x -= self.speed

    def moveRight(self):
        """
        updates the snake's position by "self.speed" number of pixels to the right;
        call self.update() before updating the body, this insures that each
        square inherits the previous squares position prior to updating the 
        head
        """
        self.update()
        self.snake[0].x += self.speed

    def add(self, direction: str):
        """
        increases the size of the snake; the placement of the new rectangle will depend on the direction
        of the last rectangle in the snake array (i.e. if the tail is moving right, the new rectangle will be 
        placed on the left side of that rectangle)
        """
        snakeTail = self.snake[-1]
        newSnakeTail = pygame.Rect(snakeTail.left, snakeTail.top, self.width, self.height) # can you make a copy of the reference 

        if direction == 'u':
            newSnakeTail.top += self.height
        elif direction == 'd':
            newSnakeTail.top -= self.height
        elif direction == 'l':
            newSnakeTail.left += self.width
        elif direction == 'r':
            newSnakeTail.left -= self.width
        
        self.snake.append(newSnakeTail)   


    def update(self):
        """
        updates each individual square with the previous squares position
        (i.e. square[i] inherits square[i - 1] x and y coordinates)
        """
        x_curr, y_curr = self.snake[0].x, self.snake[0].y

        for current in self.snake[1:]:
            x_prev, y_prev = current.x, current.y
            current.x, current.y = x_curr, y_curr
            x_curr, y_curr = x_prev, y_prev


    def collision(self) -> bool:
        """
        checks whether the snake collides with itself and returns True; False otherwise
        """
        snakeHead = self.getHead()

        for i in range(1, len(self.snake)):
            if snakeHead.x == self.snake[i].x and snakeHead.y == self.snake[i].y:
                return True

        return False


    def draw(self, screen) -> None:
        """
        iterates through self.snake and draws each individual square onto 
        the given screen
        """
        for current in self.snake:
            pygame.draw.rect(screen, self.color, current)


    def reset(self):
        """
        resets the snake's head to it's initial starting position; deleting 
        1 to n squares, this ensures that the players progress is reset
        """
        del self.snake[1:]

        snakeHead = self.getHead()
        snakeHead.x, snakeHead.y = 50, 150

