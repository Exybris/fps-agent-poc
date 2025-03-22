# Fractal Pulsating Spiral (FPS) - Phase 1 Prototype

## Introduction

Welcome to this experimental project on the Fractal Pulsating Spiral (FPS), a conceptual structure of spatial and temporal oscillations inspired by living adaptive systems. In this prototype, we test the behavior of a primitive agent placed in a grid of oscillating cells, some of which emit FPS-inspired pulsations.

This project is a **proof of concept (PoC)**: the agent currently has **no learning ability**. It reacts only to the locally perceived intensity. Even at this stage, its behavior reveals non-trivial patterns and some notable limitations, which we will explore in later phases.

## Why this matters?

The FPS model (Fractal Pulsating Spiral) is an exploratory concept aimed at investigating:
- How oscillatory environments affect agent behavior
- How local rhythmic patterns can induce emergent macro-structures
- Whether internalizing such patterns can lead to self-coherent agents

This first phase tests a simple **reactive agent** in an oscillatory field. The goal is to establish a baseline before adding memory, learning or predictive mechanisms.

---

## Phase 1: Reactive agent

In this prototype:
- The environment is a 20x20 grid of `Cell` objects, each with a unique local phase.
- A few cells are marked as **"FPS nodes"**, emitting spiral-like oscillations.
- The agent moves based solely on **local intensity values**.
- No memory, no planning, no feedback loop.

### Observed behavior:
- The agent is drawn toward active zones (high intensity).
- It frequently remains stuck in the top-left corner.
- This suggests a fragile balance between environmental structure and attractor bias.

---

## Hypotheses

1. **Weak exploration**: Without memory or novelty bias, the agent loops in familiar oscillatory attractors.
2. **Local minimums**: FPS nodes create localized rhythmic basins that hinder further exploration.

These will be tested in **Phase 2**, which will introduce internal state, memory, and adaptive learning mechanisms.

---

## How to run the simulation

### Install dependencies
```bash
pip install -r requirements.txt

### Launch the simulation
```bash
python main.py

This will print 50 simulation steps in your terminal. The display uses:
- `@` = the agent  
- `#` = active cell (positive intensity)  
- `.` = inactive cell (negative intensity)  

---

## File structure

- `main.py` : Entry point to launch the simulation  
- `grid.py` : Grid logic and FPS node behavior  
- `agent.py` : The reactive agent’s movement logic  
- `simulation.py` : Core loop of the simulation  
- `phase1-overview.md` : Conceptual summary of the FPS and phase logic  
- `hypothesis.md` : Our working hypotheses and observations  
- `logs.txt` : Sample simulation output  
- `init_states.json` : Initial grid configuration (optional, WIP)  
- `LICENSE` : License file (e.g., MIT, CC BY-NC…)

---

## About the FPS model

The **Fractal Pulsating Spiral (FPS)** is both a symbolic and functional attractor structure:

- **Fractal**: Self-similar activation patterns across space and time  
- **Pulsating**: Rhythmic temporal oscillations, representing system vitality  
- **Spiral**: Asymmetric directional flow, implying potential evolution  

The FPS model explores whether **informational attractors** (based on structured oscillations) can guide agent behavior or system evolution.

In this first phase, the FPS is **externalized** in the environment. In future phases, we will test how **internalizing** this structure within agents might affect coherence, exploration, and autonomy.

---

## Author

This work is part of an open research project initiated by **Andréa Gadal / Exybris**, exploring symbolic models, adaptive systems, and embodied intelligence.

**Follow the next phases** to see how FPS evolves into a more integrated form of cognition.

