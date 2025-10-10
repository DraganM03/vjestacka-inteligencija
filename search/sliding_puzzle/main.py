from sliding_puzzle import SlidingPuzzle

sp = SlidingPuzzle((4,1,2,6,9,8,7,5), (1,2,3,6,9,8,7,4))

print(sp.get_actions(sp.start))
print(sp.get_actions(sp.goal))