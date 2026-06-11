# Forest Fire Cellular Automaton

A forest fire simulation implemented in Python using Cellular Automata. The project models how a fire spreads through a forest based on local interactions between neighboring cells.

## Overview

The forest is represented as a two-dimensional grid where each cell can be in one of three states:

* **Empty** – no tree is present.
* **Tree** – a healthy tree.
* **Fire** – a burning tree.

The simulation begins with a randomly generated forest and several ignition points. At each step, the state of every cell is updated simultaneously according to simple rules.

## Simulation Rules

1. An empty cell remains empty.
2. A burning tree becomes an empty cell.
3. A tree catches fire if at least one of its orthogonal neighbors is burning.
4. Otherwise, the tree remains unchanged.

The current implementation uses a **4-neighbor model**, meaning fire can spread only up, down, left, and right.

## Algorithm

The simulation is based on a Cellular Automaton (CA).

To ensure correct updates, two grids are maintained:

* the current state of the forest;
* the next state being computed.

During each iteration, the next state is calculated from the current state. Once all cells have been processed, the two grids are swapped.

This approach guarantees that all updates occur simultaneously and prevents newly updated cells from influencing the same iteration.

## 

* Python 3
* NumPy
* Pygame
* Numba (optional)

NumPy is used for efficient grid storage and manipulation, while Pygame provides real-time visualization. Numba can be used to accelerate the computation of simulation steps.

## Initial Configuration

The forest is generated using a density parameter that controls the proportion of cells initially occupied by trees.

Three independent fire sources are placed in different regions of the map at the start of the simulation, allowing multiple fire fronts to develop simultaneously.

## Running the Project

Install the required dependencies:

```bash
pip install pygame numpy numba
```

Run the simulation:

```bash
python3 forest_fire.py
```

## Example

At the beginning of the simulation, most cells contain trees. As the fire propagates through neighboring cells, clusters of trees burn and disappear, leaving empty areas behind. The process continues until no burning cells remain.

## Project Goal

This project demonstrates how complex large-scale behavior can emerge from a small set of local rules. It also serves as an introduction to Cellular Automata, simulation techniques, and scientific visualization in Python.

