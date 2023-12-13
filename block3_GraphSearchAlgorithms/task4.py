# 4. Implement a solution to solve the maze (лабиринт) problem using BFS.
# # Solving the maze problem using Breadth-First Search (BFS) involves finding a path from the start point to the end point in a maze. 

# In this implementation, the solve_maze function takes a maze, start point, 
# and end point as input and returns the minimum steps required to reach the end point. 
# The BFS algorithm is used to explore the possible paths in the maze.

# The example usage demonstrates creating a maze and finding the minimum steps to reach the end point. 
# You can modify the maze, start_point, and end_point variables to test with different mazes and points. 
# The output will display the minimum steps or indicate if no path is found.

from collections import deque

def solve_maze(maze, start, end):
    if not maze or not maze[0]:
        return None

    rows, cols = len(maze), len(maze[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def is_valid_move(row, col):
        return 0 <= row < rows and 0 <= col < cols and maze[row][col] == 0

    queue = deque([(start[0], start[1], 0)])  # (row, col, steps)
    visited = set()

    while queue:
        current_row, current_col, steps = queue.popleft()

        if (current_row, current_col) == end:
            return steps

        for direction in directions:
            new_row, new_col = current_row + direction[0], current_col + direction[1]

            if is_valid_move(new_row, new_col) and (new_row, new_col) not in visited:
                queue.append((new_row, new_col, steps + 1))
                visited.add((new_row, new_col))

    return None  # No path found

# Example usage:
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1]
]

start_point = (0, 0)
end_point = (4, 4)

steps_to_end = solve_maze(maze, start_point, end_point)

if steps_to_end is not None:
    print(f"Minimum steps to reach the end: {steps_to_end}")
else:
    print("No path found.")
