import heapq

start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

# Heuristic function
def h(state):
    count = 0
    for i in range(9):
        if state[i] != 0 and state[i] != goal[i]:
            count += 1
    return count

# Generate possible moves
def moves(state):
    result = []
    zero = state.index(0)

    if zero >= 3:  # Up
        new = list(state)
        new[zero], new[zero - 3] = new[zero - 3], new[zero]
        result.append(tuple(new))

    if zero < 6:  # Down
        new = list(state)
        new[zero], new[zero + 3] = new[zero + 3], new[zero]
        result.append(tuple(new))

    if zero % 3 != 0:  # Left
        new = list(state)
        new[zero], new[zero - 1] = new[zero - 1], new[zero]
        result.append(tuple(new))

    if zero % 3 != 2:  # Right
        new = list(state)
        new[zero], new[zero + 1] = new[zero + 1], new[zero]
        result.append(tuple(new))

    return result

# A* algorithm
def a_star(start, goal):
    queue = []
    g = {start: 0}
    parent = {start: None}

    heapq.heappush(queue, (h(start), start))

    while queue:
        f, current = heapq.heappop(queue)

        if current == goal:
            break

        for next_state in moves(current):
            new_g = g[current] + 1

            if next_state not in g or new_g < g[next_state]:
                g[next_state] = new_g
                f = new_g + h(next_state)

                heapq.heappush(queue, (f, next_state))
                parent[next_state] = current

    # Reconstruct solution path
    if goal not in parent:
        return []

    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()
    return path

# Solve the puzzle
solution = a_star(start, goal)

# Display solution
print("Solution:")

for state in solution:
    print(state[0], state[1], state[2])
    print(state[3], state[4], state[5])
    print(state[6], state[7], state[8])
    print()