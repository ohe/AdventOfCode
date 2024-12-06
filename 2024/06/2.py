caret_direction = {
    '^': (0, -1),
    '>': (1, 0),
    'v': (0, 1),
    '<': (-1, 0)
}


def move(grid, caret_pos):
    caret = grid[caret_pos[1]][caret_pos[0]]
    out_of_grid = False
    dir_ = caret_direction[caret]

    if caret_pos[1] + dir_[1] < 0 or caret_pos[0] + dir_[0] < 0:
        out_of_grid = True
        return caret_pos, out_of_grid

    try:
        if grid[caret_pos[1] + dir_[1]][caret_pos[0] + dir_[0]] == '#':
            grid[caret_pos[1]][caret_pos[0]] = next(turn(caret))
        else:
            grid[caret_pos[1]][caret_pos[0]] = 'o'
            grid[caret_pos[1] + dir_[1]][caret_pos[0] + dir_[0]] = caret
            caret_pos = (caret_pos[0] + dir_[0], caret_pos[1] + dir_[1])
    except IndexError:
        out_of_grid = True
    return caret_pos, out_of_grid


def turn(caret):
    caret_shape = list(caret_direction.keys())
    while True:
        caret = caret_shape[(caret_shape.index(caret) + 1) % 4]
        yield caret


grid = []
with open('2024/06/input.txt') as f:
    while grid_line := f.readline().strip():
        grid.append([e for e in grid_line])

# Look at initial caret position
for y, row in enumerate(grid):
    for x, col in enumerate(row):
        if col == '^':
            init_caret_coord = (x, y)
            break

caret_coord = init_caret_coord
nb_possible_loops = 0
positions = set([('^', init_caret_coord)])

# Brute force
for y, row in enumerate(grid):
    for x, col in enumerate(row):
        if grid[y][x] == '^' or grid[y][x] == '#':
            continue
        else:
            grid[y][x] = '#'  # Placing a new wall

        while True:
            caret_coord, out_of_grid = move(grid, caret_coord)
            if out_of_grid:
                break
            if (
                    grid[caret_coord[1]][caret_coord[0]],
                    caret_coord) in positions:
                # Loop !!!
                nb_possible_loops += 1
                break
            else:
                positions.add(
                    (grid[caret_coord[1]][caret_coord[0]], caret_coord)
                )

        # Restoring the grid
        grid[y][x] = '.'  # Removing the wall
        grid[caret_coord[1]][caret_coord[0]] = '.'  # Removing the caret
        grid[init_caret_coord[1]][init_caret_coord[0]] = '^'  # Replacing caret
        caret_coord = init_caret_coord
        positions = set([init_caret_coord])


print(nb_possible_loops)
