from n_queens import NQueens
from alhorithms import hill_climbing, simulated_annealing


nq = NQueens(4)

print(nq.start)
# nq.print_state(nq.start)

# print(nq.get_actions(nq.start))

# actions = nq.get_actions(nq.start)
# nq.print_state(nq.get_successor(nq.start, actions[0]))

# print(nq.get_score(nq.start))
hc = hill_climbing(nq)
print("\nHill Climbing solution:", nq.get_score(hc))
nq.print_state(hc)

sa = simulated_annealing(nq)
print("\nSimulated Annealing solution:", nq.get_score(sa))
nq.print_state(sa)