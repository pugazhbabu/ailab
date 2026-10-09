import heapq

# Manhattan Distance
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# A* Search Algorithm
def a_star(grid, start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start))

    came_from = {}
    g_cost = {start: 0}

    while open_list:
        _, current = heapq.heappop(open_list)

        # Check Goal
        if current == goal:
            path = []

            while current in came_from:
                path.append(current)
                current = came_from[current]

            path.append(start)
            return path[::-1]

        row, col = current

        # Up, Down, Left, Right
        directions = [(1, 0), (-1, 0),
                      (0, 1), (0, -1)]

        for dr, dc in directions:
            nr = row + dr
            nc = col + dc

            # Check Valid Position
            if (0 <= nr < len(grid) and
                0 <= nc < len(grid[0]) and
                grid[nr][nc] == 0):

                neighbor = (nr, nc)
                new_cost = g_cost[current] + 1

                if (neighbor not in g_cost or
                    new_cost < g_cost[neighbor]):

                    g_cost[neighbor] = new_cost

                    f_cost = new_cost + heuristic(neighbor, goal)

                    heapq.heappush(open_list, (f_cost, neighbor))
                    came_from[neighbor] = current

    return None


# Main Program
# 0 = Free Path, 1 = Obstacle
grid = [
    [0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 6)

path = a_star(grid, start, goal)

print("Start:", start)
print("Goal:", goal)

if path:
    print("Shortest Path:")
    print(path)
    print("Path Length:", len(path) - 1)
else:
    print("No path found")
