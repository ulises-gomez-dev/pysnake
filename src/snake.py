import pygame

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

