#agent.py

class Agent:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, grid):
        max_intensite = grid[self.x][self.y].intensite
        next_x, next_y = self.x, self.y

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = self.x + dx, self.y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                    if grid[nx][ny].intensite > max_intensite:
                        max_intensite = grid[nx][ny].intensite
                        next_x, next_y = nx, ny

        self.x, self.y = next_x, next_y