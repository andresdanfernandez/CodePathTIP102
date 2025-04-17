"""Problem 1: Battle Moves
You are in the midst of a battle with another neighboring kingdom and need to decide your next move. You have an m x n matrix battle representing a map of the battlefield where each cell holds either an X or an O. Xs represent your kingdom's captured territory and Os represent the opposing kingdom's territory.

Given the row and column of your current position in the battle and a list of tuples past_moves of the form (row, column) representing moves you've already taken in battle, implement a function next_moves() that returns a list of tuples representing valid next moves.

From your current row and column position, you may move to any (row, column) index that is horizontally or vertically adjacent such that row and column are both valid indices in grid and part of your kingdom's captured territory. In this battle, you are not allowed to repeat moves, so any past_moves[i] should not be included in your output list.

def next_moves(battle, row, column, past_moves):
    pass
Example Usage:

battle = [
     (0)  (1)  (2)  (3)  (4)
    ['X', 'O', 'O', 'X', 'X'], # Row 0
    ['O', 'O', 'O', 'X', 'X'], # Row 1
    ['X', 'X', 'X', 'O', 'O'], # Row 2
    ['X', 'X', 'X', 'X', 'O'], # Row 3
    ['O', 'O', 'O', 'X', 'O']  # Row 4
]

position_1 = (3, 2)
position_2 = (0, 4)
position_3 = (0, 1)

print(next_moves(battle, 3, 2, []))
print(next_moves(battle, 3, 2, [(2, 2), (3, 3), (0, 0)]))
print(next_moves(battle, 0, 4, []))
print(next_moves(battle, 0, 0, []))
Example Output:

[(3, 1), (3, 3), (2, 2)]
Example 1 Explanation: The cell to the left, right, and one up from (3, 2) all have 
value X and thus are valid moves. The cell one down from (3, 2) has value O and is thus 
invalid.

[(3, 1)]
Example 2 Explanation: Possible moves are [(3, 1), (3, 3), (2, 2)], but (3, 3) and (2,2)
are in the past_moves list, therefore the only possible next move is (3, 1)

[(0, 3), (1,4)]
Example 3 Explanation: Moving in the upwards or rightwards direction from position
(0, 4) moves us outside the bounds of the battlefield. Leftwards and downwards
both result in valid moves. 

[]
Example 4 Explanation: Moving left, right, up, or down would either result in moving
into enemy territory or going out of bounds. Thus we return an empty list.
"""

# Understand:
#         * Given an adjacency matrix
#         * We want to move to a grid cell that holds 'X' 
#         * We are also given a list of tuples that are positions in the grid we cannot move to
#         * Output is a list of tuples

# Match:
#        * Traversal -> directions [(-1,0),(1,0),(0,-1),(0,1)]
#        * 

# Plan:

#position_1 = (3, 2)
#position_2 = (0, 4)
#position_3 = (0, 1)

'''
battle = [
     (0)  (1)  (2)  (3)  (4)
    ['X', 'O', 'O', 'X', 'X'], # Row 0
    ['O', 'O', 'O', 'X', 'X'], # Row 1
    ['X', 'X', 'X', 'O', 'O'], # Row 2
    ['X', 'X', 'X', 'X', 'O'], # Row 3
    ['O', 'O', 'O', 'X', 'O']  # Row 4
]
'''

# next_moves(battle, 3, 2, [])


#     if not battle:
#              return []
#     rows = len(battle) -> 5
#     cols = len(battle[0]) ->5
#
#     result = []
#     visited = set(past_moves)
#     directions = [(-1,0),(1,0),(0,-1),(0,1)]
#
#
#    
#     for dr, dc in directions:
#       nr, nc = row + dr, col + dc
#       if 0 <= nr < rows and 0 <= nc < cols:
#           if battle[nr][nc] == 'X' and (nr, nc) not in visited:
#                   visited.add((nr, nc))
#                   result.append((nr, nc))
#     return result

# Implement:

def next_moves(battle, row, col, past_moves):
    if not battle:
        return []
    rows = len(battle)
    cols = len(battle[0]) 

    result = []
    visited = set(past_moves)
    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    for dr, dc in directions:
        nr, nc = row + dr, col + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            if battle[nr][nc] == 'X' and (nr, nc) not in visited:
                visited.add((nr, nc))
                result.append((nr, nc))

    return result

battle = [
     
    ['X', 'O', 'O', 'X', 'X'], # Row 0
    ['O', 'O', 'O', 'X', 'X'], # Row 1
    ['X', 'X', 'X', 'O', 'O'], # Row 2
    ['X', 'X', 'X', 'X', 'O'], # Row 3
    ['O', 'O', 'O', 'X', 'O']  # Row 4
]

position_1 = (3, 2)
position_2 = (0, 4)
position_3 = (0, 1)

print(next_moves(battle, 3, 2, []))
print(next_moves(battle, 3, 2, [(2, 2), (3, 3), (0, 0)]))
print(next_moves(battle, 0, 4, []))
print(next_moves(battle, 0, 0, []))

'''

Problem 2: Castle Path
Your kingdom is represented by an m x n matrix kingdom. Each square in the matrix represents a different town in the kingdom. You wish to travel from a starting position town to the castle, however several towns have been overrun by bandits.

Towns that are safe to travel through are marked with Xs and towns with dangerous bandits are marked with Os.

Given your current town and the castle location as tuples in the form (row, column), return a list of tuples representing the shortest path from your town to the castle without traveling through any towns with bandits. you may return any path. If no such path exists, return None.

From any town in the grid you may move to the neighboring towns up, down, left, or right. You may not move out of bounds of the kingdom.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity.

def path_to_castle(kingdom, town, castle):
    pass
Example Usage:

grid = [
    ['X', 'O', 'X', 'X', 'O'], # Row 'O'
    ['X', 'X', 'X', 'X', 'O'], # Row 1
    ['O', 'O', 'X', 'X', 'O'], # Row 2
    ['X', 'O', 'X', 'X', 'X']  # Row 3
]

town_1 = (0, 0)
town_2 = (0, 4)
town_3 = (3, 0)

print(path_to_castle(town_1, grid))
print(path_to_castle(town_2, grid))
print(path_to_castle(town_3, grid))

Example Output:

start  
  |     |
  v     v
[0, 0, (10)]
Example 1 Explanation: Can follow the path (0, 0) -> (1, 0) -> (1, 1) -> (1, 2) -> 
(2, 2) -> (3, 2) -> (3, 3) -> (3, 4)

True
Example 2 Explanation: Although we start in an unsafe position, we can immediately
arrive in a safe position and from there safely travel to the bottom right corner (3, 4).

False
'''

# Understand:
# Given a grid (kingdom)
# Given a starting position (town)
# Given an ending position (castle)
# find all paths to castle and return the shortest one
# output: shortest list of tuples


# Match:
# DFS -> stack iterative


# Plan:
# path_to_castle(kingdom, town, castle)

# direction is in this order (down, right, up ,left)

# grid = [
#     ['X', 'O', 'X', 'X', 'O'], # Row 'O'
#     ['X', 'X', 'O', 'X', 'O'], # Row 1
#     ['O', 'O', 'X', 'X', 'O'], # Row 2
#     ['X', 'O', 'X', 'X', 'X']  # Row 3
# ]

# grid = [
#     ['X', 'O', 'X', 'X', 'O'], # Row 'O'
#     ['X', 'O', '0', 'X', 'O'], # Row 1
#     ['X', 'O', 'X', 'X', 'O'], # Row 2
#     ['X', 'X', 'X', 'O', 'X']  # Row 3
# ]

# town_1 = (0, 0)
# town_2 = (0, 4)
# town_3 = (3, 0)


# while
# Stack = [(0, 0)]
# Visited = ()


# Traversal -> manages up, down, left, right:
#  nr, nc
#  check if its in bounds
#  is our nr, nc == X and not in visited
#  add to the stack 
#  add to visited


# Implement:

def path_to_castle(town, kingdom):
    if not kingdom:
        return []
    
    rows = len(kingdom)
    cols = len(kingdom[0])


    r, c = town
    cr, cc = rows - 1, cols - 1

    directions = [(1, 0), (0, 1), (-1, 0), (1, 0)]
    visited = set()

    # [1, 2] -> 


    def dfs(r, c):
        stack = [(r, c)]
        visited.add((r, c))

        while stack:
            row, col = stack.pop()
            if (rows, cols) == (cr, cc):
                return visited.add(rows, cols)
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if kingdom[nr][nc] == 'X' and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        stack.append((nr, nc))


    dfs(r, c)
    return list(sorted(visited))


grid = [
    ['1', 'O', '1', 'X', 'O'], # Row 'O'
    ['1', '1', '1', '1', 'O'], # Row 1
    ['O', 'O', '1', '1', 'O'], # Row 2
    ['X', 'O', 'X', '1', '1']  # Row 3
]

town_1 = (0, 0)
town_2 = (0, 4)
town_3 = (3, 0)

print(path_to_castle(town_1, grid))
#print(path_to_castle(town_2, grid))
#print(path_to_castle(town_3, grid))

from collections import deque

# Helper function to get valid neighboring towns
def get_neighbors(position, kingdom, visited):
    row, col = position
    moves = [
        (row + 1, col),  # down
        (row - 1, col),  # up
        (row, col + 1),  # right
        (row, col - 1)   # left
    ]
    
    neighbors = []
    for r, c in moves:
        if (0 <= r < len(kingdom)
            and 0 <= c < len(kingdom[0])
            and kingdom[r][c] == 'X'
            and (r, c) not in visited):
            neighbors.append((r, c))
    
    return neighbors

# Main function to find the path to the castle
def path_to_castle(kingdom, town, castle):
    if town == castle:
        return [town]
    
    # Initialize BFS queue and visited set
    queue = deque([(town, [town])])  # (current position, path so far)
    visited = set([town])
    
    while queue:
        current_position, path = queue.popleft()
        
        # Get all valid neighboring towns (marked 'X' and not visited)
        for neighbor in get_neighbors(current_position, kingdom, visited):
            if neighbor == castle:
                return path + [neighbor]  # Return the full path if we reach the castle
            
            # If not the castle, add to the queue and mark as visited
            visited.add(neighbor)
            queue.append((neighbor, path + [neighbor]))
    
    # If BFS completes without finding the castle, return None
    return None