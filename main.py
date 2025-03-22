# main.py

from grid import init_grid, load_grid_state, save_grid_state
from agent import Agent
from simulation import run_simulation, save_logs

if __name__ == "__main__":
    # Option 1 : Grille aléatoire (par défaut)
    # grid = init_grid()

    # Option 2 : Grille figée
    grid = load_grid_state(filename="data/init_states.json")

    # Sauvegarde l'état initial dans init_states.json
    # save_grid_state(grid, filename="data/init_states.json")

    agent = Agent(0, 0)
    logs = run_simulation(grid, steps=50, agent=agent, display=True)
    save_logs(logs)
    print("Logs saved ✅")