
grid = []
with open('./2024/12/input.txt', 'r') as f:
    while line := f.readline():
        grid.append(list(line.strip()))

visited = [[0 for j in range(len(grid[i]))]for i in range(len(grid))]


def is_valid(y, x, key, grid):
    if (y < len(grid) and x < len(grid[0]) and x >= 0 and y >= 0):
        if (visited[y][x] == 0 and grid[y][x] == key):
            return True
    return False


def bfs(key, i, j, grid):
    visited[i][j] = key

    x_moves = [0, 0, 1, -1]
    y_moves = [1, -1, 0, 0]

    # checks all four points connected with input[i][j]
    for x_move, y_move in zip(x_moves, y_moves):
        if is_valid(i + y_move, j + x_move, key, grid):
            bfs(key, i + y_move, j + x_move, grid)


def reset_visited():
    for i in range(len(visited)):
        for j in range(len(visited[i])):
            visited[i][j] = 0


def compute_areas(grid):
    areas = set()
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            # checking cell to the right
            key = grid[y][x]
            bfs(key, y, x, grid)
            areas.add(tuple(tuple(x) for x in visited))
            reset_visited()
    return areas


def compute_price(area):
    perimeter = 0
    nb_ones = 0

    for y in range(len(area)):
        for x in range(len(area[y])):
            if area[y][x] != 0:
                nb_ones += 1
                if x + 1 < len(area[y]) and area[y][x+1] == 0:
                    perimeter += 1
                elif x + 1 >= len(area[y]):
                    perimeter += 1

                if x - 1 >= 0 and area[y][x-1] == 0:
                    perimeter += 1
                elif x - 1 < 0:
                    perimeter += 1

                if y + 1 < len(area) and area[y+1][x] == 0:
                    perimeter += 1
                elif y + 1 >= len(area):
                    perimeter += 1

                if y - 1 >= 0 and area[y-1][x] == 0:
                    perimeter += 1
                elif y - 1 < 0:
                    perimeter += 1

    return perimeter * nb_ones


sum_ = 0
for area in compute_areas(grid):
    sum_ += compute_price(area)
print(sum_)