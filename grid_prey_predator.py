import random
import time
import os


N          = 3   # grid size 
NB_PROIES  = 2   # number of initial prey
NB_PREDS   = 1    # number of initial predators

# We want to create a small grid to initiate the process

def placer_agent():
    # return a random position in the grid
    return (random.randint(0, N - 1), random.randint(0, N - 1))

# On put prey and predator randomly
proies = [placer_agent() for _ in range(NB_PROIES)]
preds  = [placer_agent() for _ in range(NB_PREDS)]

