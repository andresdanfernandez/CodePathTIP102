from collections import deque

# Problem 1
#def next_moves(position, grid):

    #if not grid:
        #return []
    
    #m = len(grid)
    #n = len(grid[0]) if m > 0 else 0
    #row, col = position
    #directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    #safe_moves = []
    
    #for dr, dc in directions:
        #new_row, new_col = row + dr, col + dc

        #if 0 <= new_row < m and 0 <= new_col < n:
            #if grid[new_row][new_col] == 1:
                #safe_moves.append((new_row, new_col))
    
    #return safe_moves

#grid = [
    #[0, 0, 0, 1, 1], 
    #[0, 0, 0, 1, 1], 
    #[1, 1, 1, 0, 0], 
    #[1, 1, 1, 1, 0], 
    #[0, 0, 0, 1, 0],
    #[0, 0, 0, 0, 1]  
#]

#position_1 = (3, 2)
#position_2 = (0, 4)
#position_3 = (0, 1)

#print(next_moves(position_1, grid))
#print(next_moves(position_2, grid))
#print(next_moves(position_3, grid))

# Problem 2

#def can_move_safely(position, grid):
    #if not grid:
        #return False
    
    #m = len(grid)
    #n = len(grid[0]) if m > 0 else 0
    #target = (m - 1, n - 1)
    
    #if grid[target[0]][target[1]] != 1:
        #return False
    
    #start_row, start_col = position
    #if grid[start_row][start_col] != 1:
        #return False
    
    #directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    #visited = set()
    #queue = deque()
    #queue.append((start_row, start_col))
    #visited.add((start_row, start_col))
    
    #while queue:
        #current_row, current_col = queue.popleft()
        #if (current_row, current_col) == target:
            #return True
        
        #for dr, dc in directions:
            #new_row, new_col = current_row + dr, current_col + dc
            #if 0 <= new_row < m and 0 <= new_col < n:
                #if grid[new_row][new_col] == 1 and (new_row, new_col) not in visited:
                    #visited.add((new_row, new_col))
                    #queue.append((new_row, new_col))
    
    #return False

# Problem 3

#def list_all_escape_routes(grid):
    #if not grid:
        #return []
    
    #m = len(grid)
    #n = len(grid[0]) if m > 0 else 0
    #safe_haven = (m - 1, n - 1)
    
    #if grid[safe_haven[0]][safe_haven[1]] != 1:
        #return []
    
    #directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    #visited = set()
    #queue = deque()
    #queue.append(safe_haven)
    #visited.add(safe_haven)
    
    #while queue:
        #current_row, current_col = queue.popleft()
        
        #for dr, dc in directions:
            #new_row, new_col = current_row + dr, current_col + dc
            #if 0 <= new_row < m and 0 <= new_col < n:
                #if grid[new_row][new_col] == 1 and (new_row, new_col) not in visited:
                    #visited.add((new_row, new_col))
                    #queue.append((new_row, new_col))
    
    #escape_routes = [pos for pos in visited if grid[pos[0]][pos[1]] == 1]
    #return sorted(escape_routes)

# Problem 4
#def largest_safe_zone(grid):
    #if not grid:
        #return 0
    
    #m = len(grid)
    #n = len(grid[0]) if m > 0 else 0
    #visited = [[False for _ in range(n)] for _ in range(m)]
    #max_area = 0
    #directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    #for i in range(m):
        #for j in range(n):
            #if grid[i][j] == 1 and not visited[i][j]:
                #queue = deque()
                #queue.append((i, j))
                #visited[i][j] = True
                #current_area = 1
                
                #while queue:
                    #x, y = queue.popleft()
                    #for dx, dy in directions:
                        #nx, ny = x + dx, y + dy
                        #if 0 <= nx < m and 0 <= ny < n:
                            #if grid[nx][ny] == 1 and not visited[nx][ny]:
                                #visited[nx][ny] = True
                                #current_area += 1
                                #queue.append((nx, ny))
                
                #if current_area > max_area:
                    #max_area = current_area
    
    #return max_area

# Problem 5
#def time_to_infect(grid):
    #if not grid:
        #return -1
    
    #m = len(grid)
    #n = len(grid[0]) if m > 0 else 0
    #queue = deque()
    #safe_zones = 0
    #hours = 0
    
    #for i in range(m):
        #for j in range(n):
            #if grid[i][j] == 2:
                #queue.append((i, j))
            #elif grid[i][j] == 1:
                #safe_zones += 1
    
    #if safe_zones == 0:
        #return 0
    
    #directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    #while queue and safe_zones > 0:
        #for _ in range(len(queue)):
            #x, y = queue.popleft()
            #for dx, dy in directions:
                #nx, ny = x + dx, y + dy
                #if 0 <= nx < m and 0 <= ny < n:
                    #if grid[nx][ny] == 1:
                        #grid[nx][ny] = 2  
                        #safe_zones -= 1
                        #queue.append((nx, ny))
        #hours += 1
    
    #return hours if safe_zones == 0 else -1