from collections import deque

class ModelBasedAgent:

    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

        self.start = None
        self.goal = None

        for r in range(self.rows):
            for c in range(self.cols):
                if grid[r][c] == 'S':
                    self.start = (r, c)
                elif grid[r][c] == 'G':
                    self.goal = (r, c)

        self.position = self.start
        self.known_obstacles = set()
        self.visited = []
        self.complete_path = []

    def display_grid(self):
        print("\nGrid Environment:")
        for row in self.grid:
            print(" ".join(row))

    def get_neighbors(self, position):
        r, c = position

        directions = [
            (-1, 0),  # Up
            (1, 0),   # Down
            (0, -1),  # Left
            (0, 1)    # Right
        ]

        neighbors = []

        for dr, dc in directions:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < self.rows and 0 <= nc < self.cols:
                neighbors.append((nr, nc))

        return neighbors

    def perceive(self):
        # Discover nearby obstacles
        for cell in self.get_neighbors(self.position):
            r, c = cell

            if self.grid[r][c] == '#':
                self.known_obstacles.add(cell)

    def find_path(self):
        # Find path using BFS
        queue = deque()
        queue.append((self.position, [self.position]))

        visited = {self.position}

        while queue:
            current, path = queue.popleft()

            if current == self.goal:
                return path

            for neighbor in self.get_neighbors(current):
                if neighbor in visited:
                    continue

                if neighbor in self.known_obstacles:
                    continue

                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

        return None

    def run(self):
        self.visited = [self.position]

        while self.position != self.goal:
            self.perceive()

            path = self.find_path()

            if path is None:
                print("\nGoal cannot be reached!")
                return

            next_position = path[1]
            r, c = next_position

            if self.grid[r][c] == '#':
                self.known_obstacles.add(next_position)
                continue

            self.position = next_position
            self.visited.append(self.position)

        self.complete_path = self.visited.copy()

        self.display_grid()

        print("\nGoal Reached!")
        print("Complete Path:", self.complete_path)
        print("Visited Cells:", self.visited)


# Main program
grid = [
    "S...",
    ".##.",
    "...#",
    "...G"
]

agent = ModelBasedAgent(grid)
agent.run()