from config import WINDOW_HEIGHT, WINDOW_WIDTH


class Ball:
    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        # these variables are for keeping track of our velocity on both the
        # X and Y axis, since the ball can move in two dimensions
        self.dy = 0
        self.dy = 0

    def collides(self, paddle):
        # first, check to see if the left edge of either is farther to the right
        # than the right edge of the other
        if self.x > paddle.x + paddle.width or paddle.x > self.x + self.width:
            return False

        # then check to see if the bottom edge of either is higher than the top
        # edge of the other
        if self.y > paddle.y + paddle.height or paddle.y > self.y + self.height:
            return False

        return True

    def reset(self):
        self.x = WINDOW_WIDTH / 2 - 2
        self.y = WINDOW_HEIGHT / 2 - 2
        self.dx = 0
        self.dy = 0
