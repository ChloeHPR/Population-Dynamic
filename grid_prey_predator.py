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

### the next objective is to create a real approach
### a predator will not eat the prey until he doesn't see it
### since we start with a 2D model we will consider the area vision as the proximity to the prey
### if the predator is one case close to the prey, he captures
### if the predator is two cases away from the prey he sees and decides to go in a prefered direction
### more than two cases away -> stay in random mode

def distance(a, b):
    # we want to apply this vision area
    # we use Chebyshev distance between two cases and calculate the max between x and y
    """ 
    here is the idea
    d = 1 → adjacent case (capture zone)
    d = 2 → vision area 
    d > 2 → out of see
    
    """
    return max(abs(a[0] - b[0]), abs(a[1] - b[1]))

