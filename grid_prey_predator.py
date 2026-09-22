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


### we are going to separate 
def deplacer_proie(px, py):
    """
    The prey moves randomly in it 8 neighbour cases 
    we put a constraint on the side of the grid with min/max
    """
    nx = px + random.choice([-1, 0, 1])
    ny = py + random.choice([-1, 0, 1])
    nx = max(0, min(N - 1, nx))
    ny = max(0, min(N - 1, ny))
    return nx, ny


def deplacer_pred(ex, ey):
    """
    The predator has 3 kind of moves depending on the distance with the prey:
    
    - out of zone (d > 2) : random move
    - vision area (d <= 2) : the pred can get closer to the prey
    - capture zone(d <= 1) : géré dans la boucle principale (capture)
    """
    if not proies:
        return ex, ey

    # We are looking for the closest prey
    cible = min(proies, key=lambda p: distance((ex, ey), p))
    px, py = cible
    d = distance((ex, ey), cible)

    if d <= 2:
        # vision area (the prey can get closer, one case by one)
        nx = ex
        ny = ey
        if px > ex: nx += 1
        elif px < ex: nx -= 1
        if py > ey: ny += 1
        elif py < ey: ny -= 1
    else:
        # out of zone (random move)
        nx = ex + random.choice([-1, 0, 1])
        ny = ey + random.choice([-1, 0, 1])

    nx = max(0, min(N - 1, nx))
    ny = max(0, min(N - 1, ny))
    return nx, ny

def afficher(tour):
    """
    Show the grid 
    O = prey   X = predator    . = empty case
    if mare than one agent by case, the priority is given to the pred
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Tour {tour} | Proies restantes : {len(proies)}\n")

    for row in range(N):
        for col in range(N):
            if   any(col == ex and row == ey for ex, ey in preds):  print(" X", end="")
            elif any(col == px and row == py for px, py in proies): print(" O", end="")
            else:                                                    print(" .", end="")
        print()
    print()

tour = 0

while True:

    afficher(tour)

    # stop condition
    if not proies:
        print("Every prey has been captured")
        break

    time.sleep(VITESSE)

    # Prey can move
    proies[:] = [deplacer_proie(px, py) for px, py in proies]

    # We remove the captured prey
    proies[:] = [p for p in proies if p not in preds]

    # predators move
    preds[:] = [deplacer_pred(ex, ey) for ex, ey in preds]

    # we remove captured prey after the predator move
    proies[:] = [p for p in proies if p not in preds]

    tour += 1
