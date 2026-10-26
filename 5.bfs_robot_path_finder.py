
from collections import deque

def bfs(grid, start, goal):
    rows = len(grid)
    cols = len(grid[0])

    queue = deque([(start, [start])])
    visited = [start]
    visited_set = {start}

    directions = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]

    while queue:
        current, path = queue.popleft()

        if current == goal:
            print("\nAll Visited Nodes:")
            print(visited)

            print("\nShortest Path:")
            print(path)

            print("\nGoal Reached!")
            print("Total Moves:", len(path) - 1)
            return

        r, c = current

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            neighbor = (nr, nc)

            if (0 <= nr < rows and
                0 <= nc < cols and
                grid[nr][nc] != '#' and
                neighbor not in visited_set):

                visited_set.add(neighbor)
                visited.append(neighbor)
                queue.append((neighbor, path + [neighbor]))

    print("Goal Not Reached!")
    print("All Visited Nodes:", visited)


grid = [
    ['S', '.', '.', '#', '.'],
    ['.', '#', '.', '#', '.'],
    ['.', '.', '.', '#', '.'],
    ['#', '#', '.', '.', '.'],
    ['.', '.', '.', '.', 'G']
]

start = (0, 0)
goal = (4, 4)

print("Starting from:", start)
bfs(grid, start, goal)
