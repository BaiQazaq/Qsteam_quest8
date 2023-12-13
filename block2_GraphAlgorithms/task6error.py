# 6. Implement a graph-based solution for the river crossing problem.
# The river crossing problem involves transporting a group of people and items across a river using a boat. 
# The challenge is to find a sequence of moves that safely transports everyone and everything across the river. 
# A common variant is the missionary and cannibal problem, where missionaries and cannibals must be transported 
# across the river without ever having more cannibals than missionaries on either side.

# This code uses a state-space search to find a sequence of moves for the missionary and cannibal problem. 
# The State class represents a state in the problem, and the get_successors function generates valid successor states. 
# The breadth_first_search function performs a breadth-first search to find the solution path, 
# and the construct_path function reconstructs the path from the initial state to the goal state.

# The output will display the sequence of moves required to solve the missionary and cannibal problem, 
# or indicate that no solution was found.

