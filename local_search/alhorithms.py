# ===================== HILL CLIMBING =====================
def hill_climbing(problem):

    current_state = problem.start

    while True:

        best_successor = None
        best_score = -1         # initial value that cant be reached

        actions = problem.get_actions(current_state)
        successors = [problem.get_successor(current_state, action) for action in actions]

        for successor in successors:

            successor_score = problem.get_score(successor)

            if successor_score > best_score:
                best_successor = successor
                best_score = successor_score

            if best_score > problem.get_score(current_state):
                current_state = best_successor
            else:
                break

        return current_state
    
# ==================== SIMULATED ANNEALING ====================
# as time(t) passes the /(T) drops
#     ^
#   T |.
#     | &
#     |  *-...________
#     +----------------> time
# 
#   T = a+e^(-b*t)
#   delta = score(successor) - score(current)
#   delta > 0 -> current = successor
#   delta <= 0 -> current = successor with probability p = e^(delta/T)
# =============================================================
import math
import random

def get_temp(t, a=30, b=0.005, limit=1e-6):  #1e-6 = 10^-6
    T = a * math.exp(-b * t)
    if T < limit:
        T = 0.0
    return T

def simulated_annealing(problem):
    current_state = problem.start
    t = 0 # time

    while True:

        T = get_temp(t)
        if T == 0.0:
            break

        actions = problem.get_actions(current_state)
        successors = [problem.get_successor(current_state, action) for action in actions]

        # random successor
        successor_state = random.choice(successors)

        curr_score = problem.get_score(current_state)
        succ_score = problem.get_score(successor_state)

        delta = succ_score - curr_score

        if delta > 0:
            current_state = successor_state
        else:
            p = math.exp(delta / T)
            if random.uniform(0,1) <= p:
                current_state = successor_state
            # else: do nothing, stay in current state

        t += 1
        
    return current_state
