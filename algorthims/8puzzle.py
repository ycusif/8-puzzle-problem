# -*- coding: utf-8 -*-
"""8puzzle.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1PHn0qnq4dWc9R58S_MY5mlCpzTqcfye7
"""

import heapq
import ipywidgets as widgets
from IPython.display import display, clear_output
from collections import deque
import time

# Define the goal state for the 8-puzzle
GOAL_STATE = [[1, 0, 3], [8, 2, 4], [7, 6, 5]]

def find_blank_tile(state):
    """Finds the position of the blank tile (0) in the puzzle."""
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Possible moves: Up, Down, Left, Right
offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def generate_successors(state):
    """Generates possible moves from the current state."""
    successors = []
    x, y = find_blank_tile(state)
    for dx, dy in offsets:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            successors.append(new_state)
    return successors

def print_puzzle(state):
    """Prints the puzzle state in a readable format."""
    for row in state:
        print(" ".join(str(cell) if cell != 0 else "_" for cell in row))
    print("\n")

def solve_puzzle(algorithm, initial_state, heuristic=None):
    """Solves the puzzle using the chosen algorithm and measures execution time."""
    clear_output(wait=True)
    print("Initial State:")
    print_puzzle(initial_state)

    start_time = time.time()
    solution = algorithm(initial_state) if not heuristic else algorithm(initial_state, heuristic)
    end_time = time.time()

    if solution:
        print(f"\nSolution Found using {algorithm.__name__}!")
        print_puzzle(solution)
        print(f"Execution Time: {end_time - start_time:.4f} seconds\n")
    else:
        print("No solution found.")

# Breadth-First Search (BFS)
def bfs(initial_state):
    queue = deque([initial_state])
    visited = set()
    while queue:
        state = queue.popleft()
        if state == GOAL_STATE:
            return state
        visited.add(tuple(map(tuple, state)))
        for successor in generate_successors(state):
            if tuple(map(tuple, successor)) not in visited:
                queue.append(successor)

# A* Search
def a_star(initial_state, heuristic):
    priority_queue = [(heuristic(initial_state), 0, initial_state)]
    visited = set()
    while priority_queue:
        _, cost, state = heapq.heappop(priority_queue)
        if state == GOAL_STATE:
            return state
        visited.add(tuple(map(tuple, state)))
        for successor in generate_successors(state):
            if tuple(map(tuple, successor)) not in visited:
                heapq.heappush(priority_queue, (cost + heuristic(successor), cost + 1, successor))

# Example heuristic: Manhattan Distance
def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                # Find the goal position of the current value
                for goal_x in range(3):
                    for goal_y in range(3):
                        if GOAL_STATE[goal_x][goal_y] == value:
                            distance += abs(i - goal_x) + abs(j - goal_y)
                            break  # Break inner loop once found
                    else:
                        continue  # Continue outer loop if not found in inner loop
                    break  # Break outer loop once found in inner loop

    return distance

# Interactive Widgets for Google Colab
def interactive_solver(algorithm):
    initial_state = [[2, 8, 3], [1, 4, 0], [7, 6, 5]]
    heuristic = manhattan_distance if algorithm == a_star else None
    solve_puzzle(algorithm, initial_state, heuristic)

algorithm_selector = widgets.Dropdown(
    options={
        'Breadth-First Search (BFS)': bfs,
        'A* Search (A-Star)': a_star
    },
    description='Algorithm:',
)

run_button = widgets.Button(description='Solve Puzzle', button_style='success')

def on_run_clicked(b):
    interactive_solver(algorithm_selector.value)

run_button.on_click(on_run_clicked)

display(algorithm_selector, run_button)

import heapq
import ipywidgets as widgets
from IPython.display import display, clear_output
from collections import deque
import time

# Define the goal state for the 8-puzzle
GOAL_STATE = [[1, 0, 3], [8, 2, 4], [7, 6, 5]]

def find_blank_tile(state):
    """Finds the position of the blank tile (0) in the puzzle."""
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Possible moves: Up, Down, Left, Right
offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def generate_successors(state):
    """Generates possible moves from the current state."""
    successors = []
    x, y = find_blank_tile(state)
    for dx, dy in offsets:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            successors.append(new_state)
    return successors

def print_puzzle(state):
    """Prints the puzzle state in a readable format."""
    for row in state:
        print(" ".join(str(cell) if cell != 0 else "_" for cell in row))
    print("\n")

def solve_puzzle(algorithm, initial_state, heuristic=None):
    """Solves the puzzle using the chosen algorithm and measures execution time."""
    clear_output(wait=True)
    print("Initial State:")
    print_puzzle(initial_state)

    start_time = time.time()
    solution = algorithm(initial_state) if not heuristic else algorithm(initial_state, heuristic)
    end_time = time.time()

    if solution:
        print(f"\nSolution Found using {algorithm.__name__}!")
        print_puzzle(solution)
        print(f"Execution Time: {end_time - start_time:.4f} seconds\n")
    else:
        print("No solution found.")

# Search Algorithms
def bfs(initial_state):
    queue = deque([initial_state])
    visited = set()
    while queue:
        state = queue.popleft()
        if state == GOAL_STATE:
            return state
        visited.add(tuple(map(tuple, state)))
        for successor in generate_successors(state):
            if tuple(map(tuple, successor)) not in visited:
                queue.append(successor)

def dfs(initial_state):
    stack = [initial_state]
    visited = set()
    while stack:
        state = stack.pop()
        if state == GOAL_STATE:
            return state
        visited.add(tuple(map(tuple, state)))
        for successor in generate_successors(state):
            if tuple(map(tuple, successor)) not in visited:
                stack.append(successor)

def ucs(initial_state):
    priority_queue = [(0, initial_state)]
    visited = set()
    while priority_queue:
        cost, state = heapq.heappop(priority_queue)
        if state == GOAL_STATE:
            return state
        visited.add(tuple(map(tuple, state)))
        for successor in generate_successors(state):
            if tuple(map(tuple, successor)) not in visited:
                heapq.heappush(priority_queue, (cost + 1, successor))

def a_star(initial_state, heuristic):
    priority_queue = [(heuristic(initial_state), 0, initial_state)]
    visited = set()
    while priority_queue:
        _, cost, state = heapq.heappop(priority_queue)
        if state == GOAL_STATE:
            return state
        visited.add(tuple(map(tuple, state)))
        for successor in generate_successors(state):
            if tuple(map(tuple, successor)) not in visited:
                heapq.heappush(priority_queue, (cost + heuristic(successor), cost + 1, successor))

def hill_climbing(initial_state, heuristic):
    current_state = initial_state
    while True:
        neighbors = generate_successors(current_state)
        best_neighbor = min(neighbors, key=heuristic, default=current_state)
        if heuristic(best_neighbor) >= heuristic(current_state):
            return current_state
        current_state = best_neighbor

def greedy_best_first(initial_state, heuristic):
    return a_star(initial_state, heuristic)  # Using A* structure without g(n)

# Example heuristic: Manhattan Distance
def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                # Find the goal position of the current value
                for goal_x in range(3):
                    for goal_y in range(3):
                        if GOAL_STATE[goal_x][goal_y] == value:
                            distance += abs(i - goal_x) + abs(j - goal_y)
                            break  # Break inner loop once found
                    else:
                        continue  # Continue outer loop if not found in inner loop
                    break  # Break outer loop once found in inner loop

    return distance

# Interactive Widgets for Google Colab
algorithm_selector = widgets.Dropdown(
    options={
        'Breadth-First Search (BFS)': bfs,
        'Depth-First Search (DFS)': dfs,
        'Uniform Cost Search (UCS)': ucs,
        'Greedy Best-First Search': lambda x: greedy_best_first(x, manhattan_distance),
        'Hill Climbing': lambda x: hill_climbing(x, manhattan_distance),
        'A* Search (A-Star)': lambda x: a_star(x, manhattan_distance)
    },
    description='Algorithm:',
)

run_button = widgets.Button(description='Solve Puzzle', button_style='success')

def on_run_clicked(b):
    solve_puzzle(algorithm_selector.value, [[2, 8, 3], [1, 4, 0], [7, 6, 5]])

run_button.on_click(on_run_clicked)

display(algorithm_selector, run_button)