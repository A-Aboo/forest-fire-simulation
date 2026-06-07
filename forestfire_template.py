#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Calipsomulator - a simple CA and Agent-based simulator
# 2026, nb@su
# 
# GUI: curseur, z, shift+z, d, shift+d, reset, shift-reset
#

import random
import numpy as np

try:
    from numba import njit
except ImportError:
    print ("[WARNING] Numba not available.")
    def njit(*args, **kwargs):
        def wrapper(f):
            return f
        return wrapper
#from numba import njit

import calipsolib

# =-=-= Defining cell types

EMPTY = 0
TREE = 1
FIRE = 2

colors = {
    EMPTY: (255, 255, 255),
    TREE:  (40, 200, 40),
    FIRE:  (255, 40, 40),
}

# =-=-= simulation parameters

params = {
    "density": 0.55,
}

# =-=-= user-defined agents

def make_agents(params): 
    return []

# =-=-= user-defined callular automata

def init_simulation(params):
    density = params["density"]
    dx = params["dx"]
    dy = params["dy"]

    grid = np.zeros((dx, dy), dtype=np.uint8)
    newgrid = np.empty((dx, dy), dtype=np.uint8)

    
    for x in range(dx):
        for y in range(dy):
            if random.random() < density:
                grid[x,y] = 1
    #Fire init 
    grid[dx // 2, dy // 2] = FIRE          
    grid[dx // 4, dy // 4] = FIRE          
    grid[3 * dx // 4, 3 * dy // 4] = FIRE  

    return grid, newgrid

@njit(cache=True)
def count_neighbours4(grid, x, y):
    dx, dy = grid.shape
    count = 0

    if x > 0 and grid[x - 1, y] == FIRE:
        count += 1

    if x < dx - 1 and grid[x + 1, y] == FIRE:
        count += 1

    if y > 0 and grid[x, y - 1] == FIRE:
        count += 1

    if y < dy - 1 and grid[x, y + 1] == FIRE:
        count += 1

    return count


@njit(cache=True)
def count_neighbours8(grid, x, y):
    dx, dy = grid.shape
    count = 0

    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):

            if i == x and j == y:
                continue

            if i >= 0 and i < dx and j >= 0 and j < dy:
                if grid[i, j] == FIRE:
                    count += 1

    return count


@njit(cache=True)
def ca_step(grid, newgrid):
    dx, dy = grid.shape
    for x in range(dx):
        for y in range(dy):
            # EMPTY stays EMPTY
            if grid[x, y] == EMPTY:
                newgrid[x, y] = EMPTY

            # FIRE becomes EMPTY
            elif grid[x, y] == FIRE:
                newgrid[x, y] = EMPTY

            # TREE burns if it has at least one FIRE neighbour
            elif grid[x, y] == TREE:
                fire_neighbours = count_neighbours4(grid, x, y)

                if fire_neighbours > 0:
                    newgrid[x, y] = FIRE
                else:
                    newgrid[x, y] = TREE

# =-=-= run

if __name__ == "__main__":
    calipsolib.run(
        params=params, # user-defined
        init_simulation=init_simulation, # user-defined
        ca_step=ca_step, # user-defined
        make_agents=make_agents, # user-defined
        colors=colors,
        dx=100, # CA width
        dy=100, # CA height
        display_dx=600,
        display_dy=600,
        title="Forest Fire CA", 
        verbose=True, # display stuff (can be used by user)
        fps=60 # steps per seconds (default: 60)
    )
