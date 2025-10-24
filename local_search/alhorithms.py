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
    

# def simulated_annealing(problem, initial_temp, cooling_rate):
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