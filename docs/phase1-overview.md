# Phase 1 Overview — FPS Prototype

## What is FPS?

The **Fractal Pulsating Spiral (FPS)** is a conceptual framework representing a dynamic, self-coherent structure.  
It blends **fractal spatial patterns**, **temporal pulsations**, and **spiral asymmetry** to model emergent organization and attractor-driven evolution.

In this project, FPS is encoded as **oscillatory nodes** in a 2D grid environment.

---

## Objective of Phase 1

This phase aims to observe how a **simple reactive agent** behaves in a structured oscillatory field, without any memory, prediction, or adaptation.

We want to establish a baseline:
- Can the agent be "attracted" to the FPS nodes?
- Does it exhibit local looping or stagnation?
- Are emergent patterns visible even without learning?

---

## Agent Capabilities

In Phase 1:
- The agent perceives **only local intensity** (sinusoidal signal of the cell it's on).
- It **moves greedily** toward the highest neighboring intensity.
- It has **no internal state**, no memory, and no randomness.

This setup allows us to test **pure reactivity** in an environment with implicit structure.

---

## Early Observations

- The agent frequently gets **stuck** in the top-left region.
- It often **orbits local maxima**, unable to explore far.
- Certain **FPS nodes** seem to generate minor attractor patterns.
- Overall behavior lacks robustness and exploration capacity.

---

## Implications

These behaviors suggest that:
- FPS nodes can induce subtle guidance even in primitive agents.
- Without novelty-seeking or memory, agents fall into **behavioral minima**.
- Future phases should introduce internal oscillation matching, adaptive weights, and memory.

---

## What's Next?

**Phase 2** will explore:
- Agents with internal rhythmic states
- Memory-enhanced navigation
- Reward or coherence-based feedback

We aim to study whether agents can **resonate** with FPS structures rather than merely reacting to them.

---