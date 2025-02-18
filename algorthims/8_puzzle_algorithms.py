import heapq
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

# Breadth-First Search (BFS)
def bfs(initial_state):
    queue = deque([(initial_state, [])])
    visited = set()
    while queue:
        state, path = queue.popleft()
        if state == GOAL_STATE:
            return path + [state]
        visited.add(tuple(map(tuple, state)))
        for successor in generate_successors(state):
            if tuple(map(tuple, successor)) not in visited:
                queue.append((successor, path + [state]))
    return None

# Depth-First Search (DFS)
def dfs(initial_state):
    stack = [(initial_state, [])]
    visited = set()
    while stack:
        state, path = stack.pop()
        if state == GOAL_STATE:
            return path + [state]
        visited.add(tuple(map(tuple, state)))
        for successor in generate_successors(state):
            if tuple(map(tuple, successor)) not in visited:
                stack.append((successor, path + [state]))
    return None

# Uniform Cost Search (UCS)
def ucs(initial_state):
    priority_queue = [(0, initial_state, [])]
    visited = set()
    while priority_queue:
        cost, state, path = heapq.heappop(priority_queue)
        if state == GOAL_STATE:
            return path + [state]
        visited.add(tuple(map(tuple, state)))
        for successor in generate_successors(state):
            if tuple(map(tuple, successor)) not in visited:
                heapq.heappush(priority_queue, (cost + 1, successor, path + [state]))
    return None

# A* Search
def a_star(initial_state, heuristic):
    priority_queue = [(heuristic(initial_state), 0, initial_state, [])]
    visited = set()
    while priority_queue:
        _, cost, state, path = heapq.heappop(priority_queue)
        if state == GOAL_STATE:
            return path + [state]
        visited.add(tuple(map(tuple, state)))
        for successor in generate_successors(state):
            if tuple(map(tuple, successor)) not in visited:
                heapq.heappush(priority_queue, (cost + heuristic(successor), cost + 1, successor, path + [state]))
    return None

# Example heuristic: Manhattan Distance
def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_x, goal_y = divmod(GOAL_STATE.index(value), 3)
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance
