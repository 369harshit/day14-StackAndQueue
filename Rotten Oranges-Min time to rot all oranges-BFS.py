from collections import deque

def minTimeToRotOranges(grid):
    rows = len(grid)
    cols = len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    fresh_count = 0
    queue = deque()

    # Step 1: Find rotten oranges and count fresh oranges
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 2:
                queue.append((i, j))
            elif grid[i][j] == 1:
                fresh_count += 1

    time = 0

    # Step 3: Simulate rotting process
    while queue:
        size = len(queue)
        changed = False

        for i in range(size):
            x, y = queue.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                    grid[nx][ny] = 2
                    queue.append((nx, ny))
                    fresh_count -= 1
                    changed = True

        if changed:
            time += 1

    # Step 4: Check if any fresh oranges remain
    if fresh_count > 0:
        return -1  # Not possible to rot all oranges
    else:
        return time


# Example usage:
grid = [
    [0, 1, 2],
    [0, 1, 2],
    [2, 1, 1]
]

minimum_time = minTimeToRotOranges(grid)
if minimum_time == -1:
    print("Not possible to rot all oranges.")
else:
    print("Minimum time required to rot all oranges:", minimum_time)
