# ===================== HILL CLIMBING =====================
def hill_climbing(problem):

    curr_state = problem.start

    while True:

        best_successor = None
        best_score = -1         # initial value that cant be reached

        actions = problem.get_actions(curr_state)
        successors = [problem.get_successor(curr_state, action) for action in actions]

        for successor in successors:

            successor_score = problem.get_score(successor)

            if successor_score > best_score:
                best_successor = successor
                best_score = successor_score

            if best_score > problem.get_score(curr_state):
                curr_state = best_successor
            else:
                break

        return curr_state
    
# ==================== SIMULATED ANNEALING ====================
# as t(ime) passes the T(emperature) drops
#     ^
#   T |.
#     | &
#     |  *-...________
#     +----------------> time
# 
#   T = a+e^(-b*t)
#   delta = score(succ) - score(curr)
#   delta > 0 -> curr = succ
#   delta <= 0 -> curr = succ with probability p = e^(delta/T)
# =============================================================
import math

def get_temp(t, a=30, b=0.005, limit=1e-6):  #1e-6 = 10^-6
    T = a * math.exp(-b * t)
    if T < limit:
        T = 0.0
    return T

# def simulated_annealing(problem, initial_temp, cooling_rate):
