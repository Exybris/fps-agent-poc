def run_simulation(grid, steps=100, agent=None, display=True):
    """
    Run the FPS grid simulation.

    Args:
        grid (list): 2D list of Cell objects (from grid.py)
        steps (int): Number of simulation steps
        agent (Agent, optional): The reactive agent
        display (bool): If True, prints each step to terminal. If False, logs output in a list.

    Returns:
        list: A list of grid snapshots (as strings), always returned.
    """
    logs = []

    for t in range(steps):
        # Update cells
        for row in grid:
            for cell in row:
                cell.update(t / 10.0)

        # Move agent
        if agent:
            agent.move(grid)

        snapshot = []
        for row in grid:
            line = "".join([
                "@" if (cell.x, cell.y) == (agent.x, agent.y) else
                "#" if cell.intensite > 0 else "."
                for cell in row
            ])
            if display:
                print(line)
            snapshot.append(line)

        logs.append(snapshot)  

        if display:
            print(f"\nStep {t}")

    return logs 
def save_logs(logs, filename="results/logs.txt"):
    with open(filename, "w") as f:
        for step, snapshot in enumerate(logs):
            f.write(f"Step {step}\n")
            f.write("\n".join(snapshot))
            f.write("\n\n")  