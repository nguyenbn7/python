import pygame

from config import WINDOW_HEIGHT


class Paddle:

    def __init__(self, x, y, width, height) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.dy = 0

    def update(self, dt: float):
        self.y = (
            max(0, self.y + self.dy * dt)
            if self.y < 0
            else min(WINDOW_HEIGHT - self.height, self.y + self.dy * dt)
        )

    def render(self, screen: pygame.surface.Surface):
        pygame.draw.rect(
            screen, "white", pygame.Rect(self.x, self.y, self.width, self.height)
        )
