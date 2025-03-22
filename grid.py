#grid

import numpy as np

GRID_SIZE = 20

class Cell:
    def __init__(self, x, y, type="neutre"):
        self.x = x
        self.y = y
        self.type = type
        self.phase = np.random.rand() * 2 * np.pi
        self.intensite = 0

    def update(self, t):
        if self.type == "neutre":
            self.intensite = np.sin(t + self.phase)
        elif self.type == "FPS":
            # On mettra une vraie pulsation FPS ici
            self.intensite = self.fps_pulsation(t)

    def fps_pulsation(self, t):
        # Placeholder temporaire : un mix spirale-pulsation
        return np.sin(t + self.phase) * np.cos(t * 0.1 + self.x * 0.3 + self.y * 0.3)
def init_grid():
    grid = [[Cell(x, y) for y in range(GRID_SIZE)] for x in range(GRID_SIZE)]
    
    # On définit quelques nœuds FPS au centre et dans les coins
    fps_coords = [(10,10), (5,5), (15,15)]
    for x, y in fps_coords:
        grid[x][y].type = "FPS"
    
    return grid      
def simulate(grid, steps=100, agent=None):
    for t in range(steps):
        for row in grid:
            for cell in row:
                cell.update(t / 10.0)
        if agent:
            agent.move(grid)
        print("\nStep", t)
        for row in grid:
            print("".join([
                "@" if (cell.x, cell.y) == (agent.x, agent.y) else 
                "#" if cell.intensite > 0 else "." 
                for cell in row
            ]))
import json

def save_grid_state(grid, filename="results/init_states.json"):
    state = []
    for row in grid:
        state.append([
            {
                "x": cell.x,
                "y": cell.y,
                "type": cell.type,
                "phase": cell.phase
            }
            for cell in row
        ])
    with open(filename, "w") as f:
        json.dump(state, f, indent=2)

def load_grid_state(filename="results/init_states.json"):
    with open(filename, "r") as f:
        state = json.load(f)

    grid = []
    for row_data in state:
        row = []
        for cell_data in row_data:
            cell = Cell(cell_data["x"], cell_data["y"], cell_data["type"])
            cell.phase = cell_data["phase"]
            row.append(cell)
        grid.append(row)
    return grid          
if __name__ == "__main__":
    grid = init_grid()
    simulate(grid, steps=50)         