import pygame

class Apple:
    def __init__(self):
        self.apple = pygame.Rect(250, 150, 10, 10)
        self.color = (255, 0, 0)

    def draw(self, screen):
        pygame.draw.ellipse(screen, self.color, self.apple)
    
    def reset(self):
        self.apple.x, self.apple.y = 250, 150


