import sys

def read_maze(filename: str) -> list[list[str]]:
    with open(filename, 'r') as file:
        maze = [[]]
        for line in file:
            maze.append(list(line.strip()))
        maze.pop(0)  # remove the first empty list
    return maze


def find_start_and_target(maze: list[list[str]]) -> tuple[int, int]:
    row = []
    for i,row in enumerate(maze):
        for j,ch in enumerate(row):
            if ch=='S':
                starti=i
                startj=j
            if ch=='T':
                targeti=i
                targetj=j
    return ((starti, startj), (targeti,targetj))

def get_neighbors(maze: list[list[str]], position: tuple[int, int]) -> list[tuple[int, int]]:
    rows, cols = len(maze), len(maze[0])
    directions = [(-1,0), (1,0), (0,-1), (0,1)]  # up, down, left, right
    neighbors = []
    for dr, dc in directions:
        nr, nc = position[0] + dr, position[1] + dc
        if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] != '#':
            neighbors.append((nr, nc))
    return neighbors

def bfs(maze: list[list[str]], start: tuple[int, int], target: tuple[int, int]) -> list[tuple[int, int]]:
    from collections import deque
    queue = deque([start])
    visited = set([start])
    parent = {start: None}
    while queue:
        current = queue.popleft()
        if current == target:
            # reconstruct path
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]
        for neighbor in get_neighbors(maze, current):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)
    return [] 

def dfs(maze: list[list[str]], start: tuple[int, int], target: tuple[int, int]) -> list[tuple[int, int]]:
    from collections import deque
    stack =[]
    stack.append(start)
    visited = set([start])
    parent = {start: None}
    while stack:
        current = stack.pop()
        if current == target:
            # reconstruct path
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]
        for neighbor in get_neighbors(maze, current):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                stack.append(neighbor)
    return [] 

def print_maze_with_path(maze: list[list[str]], path: list[tuple[int, int]]) -> None:
    RED = "\033[91m"
    YELLOW = "\033[33m"
    GREEN = "\033[32m"
    RESET = "\033[0m"
    for i, row in enumerate(maze):
        for j, ch in enumerate(row):
            if (i, j) in path:
                if ch == 'S':
                    print(f"{GREEN}S{RESET}", end='')
                elif ch == 'T':
                    print(f"{YELLOW}T{RESET}", end='')
                else:
                    print(f"{RED}*{RESET}", end='')
            else:
                print(ch, end='')
        print()

if __name__=="__main__":
    if len(sys.argv)!=3 : print("Usage: bfs/dfs maze_file")
    mode=sys.argv[1]
    file=sys.argv[2]
    maze=read_maze(file)
    start,target = find_start_and_target(maze)
    if mode == "bfs":
        path = bfs(maze, start, target)
    else:
        path = dfs(maze,start,target)
    print_maze_with_path(maze, path)


