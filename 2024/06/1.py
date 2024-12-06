caret_direction = {
    '^': (0, -1),
    '>': (1, 0),
    'v': (0, 1),
    '<': (-1, 0)
}


def move(grid, caret_pos):
    caret = grid[caret_pos[1]][caret_pos[0]]
    out_of_grid = False
    dir = caret_direction[caret]

    if caret_pos[1] + dir[1] < 0 or caret_pos[0] + dir[0] < 0:
        out_of_grid = True
        return caret_pos, out_of_grid

    try:
        if grid[caret_pos[1] + dir[1]][caret_pos[0] + dir[0]] == '#':
            grid[caret_pos[1]][caret_pos[0]] = next(turn(caret))
        else:
            grid[caret_pos[1]][caret_pos[0]] = 'o'
            grid[caret_pos[1] + dir[1]][caret_pos[0] + dir[0]] = caret
            caret_pos = (caret_pos[0] + dir[0], caret_pos[1] + dir[1])
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

# Look at caret position
for y, row in enumerate(grid):
    for x, col in enumerate(row):
        if col == '^':
            caret_coord = (x, y)
            break

# Move caret
positions = set([caret_coord])
while True:
    caret_coord, out_of_grid = move(grid, caret_coord)
    if out_of_grid:
        break
    positions.add(caret_coord)


print(len(positions))
