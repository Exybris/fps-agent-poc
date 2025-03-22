# Hypotheses – FPS Phase 1

This document outlines the core hypotheses driving our first exploration of the FPS environment using a purely reactive agent.

---

## Initial Conditions

- Grid: 20x20 cells, each with oscillatory behavior (sinusoidal intensity)
- FPS Nodes: Special cells with structured spiral-like pulsation
- Agent: No memory, no internal dynamics — reacts only to current local intensity

---

## Hypothesis 1 — Local Attractor Traps

**Statement:**  
> Without memory or noise, the agent tends to remain in high-intensity zones, especially near initial FPS nodes.

**Rationale:**  
Due to the sinusoidal nature of intensity, local peaks can act as attractors. The agent lacks exploration mechanisms to escape these.

**Expected behavior:**  
- Loops or slow drift in confined regions  
- Preference for first-encountered active zones

---

## Hypothesis 2 — Lack of Temporal Coherence

**Statement:**  
> The agent cannot synchronize with oscillatory patterns because it lacks internal temporal awareness.

**Rationale:**  
Even if FPS nodes pulse coherently, the agent does not retain past information to detect rhythm or match phase.

**Expected behavior:**  
- Incoherent movement across the grid  
- Failure to anticipate or exploit rhythmic opportunities

---

## Hypothesis 3 — Minimal Environmental Feedback

**Statement:**  
> The environment influences the agent, but the agent does not alter the environment in return.

**Rationale:**  
This one-way interaction limits system complexity and prevents self-reinforcing behaviors.

**Expected behavior:**  
- No signs of co-evolution  
- Static attractors dominate over time

---

## Next Steps to Test

To confirm or refute these hypotheses, Phase 2 will introduce:
- Memory buffers and novelty-seeking heuristics
- Internal rhythmic models
- Basic feedback mechanisms into the environment

These additions will allow us to assess whether FPS can become a **true attractor of behavior**, rather than just a static influence.

---

## Phase 1 Status

All hypotheses remain active, pending comparative results in subsequent phases.  
This reactive baseline offers a necessary control condition for future agent evolution.

---