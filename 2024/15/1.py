grid = []
movements = ""
with open('./2024/15/input.txt', 'r') as f:
    while line := f.readline():
        line = line.strip()
        if line.startswith('#'):
            grid.append(list(line))
        else:
            movements += line


move_by = {'^': (0, -1), 'v': (0, 1), '<': (-1, 0), '>': (1, 0)}


def move_robot(grid, pos, direction):
    new_grid = grid.copy()

    pos_diff_x, pos_diff_y = move_by[direction]

    new_expected_robot_pos = (pos[0] + pos_diff_x, pos[1] + pos_diff_y)
    new_item = grid[new_expected_robot_pos[1]][new_expected_robot_pos[0]]
    if new_item == '#':
        return new_grid, pos
    if new_item == '.':
        new_grid[new_expected_robot_pos[1]][new_expected_robot_pos[0]] = '@'
        new_grid[pos[1]][pos[0]] = '.'
        return new_grid, new_expected_robot_pos
    if new_item == 'O':
        # Look in line if a "." is found before reaching a wall "#"
        if direction == '^':
            array_direction = {}
            pos_init = pos
            while True:
                grid_value = grid[pos_init[1]][pos_init[0]]
                if grid_value == "#":
                    break
                else:
                    array_direction[pos_init] = grid_value
                    if grid_value == ".":
                        break
                pos_init = (pos_init[0], pos_init[1] - 1)
        if direction == '>':
            array_direction = {}
            pos_init = pos
            while True:
                grid_value = grid[pos_init[1]][pos_init[0]]
                if grid_value == "#":
                    break
                else:
                    array_direction[pos_init] = grid_value
                    if grid_value == ".":
                        break
                pos_init = (pos_init[0] + 1, pos_init[1])
        if direction == '<':
            array_direction = {}
            pos_init = pos
            while True:
                grid_value = grid[pos_init[1]][pos_init[0]]
                if grid_value == "#":
                    break
                else:
                    array_direction[pos_init] = grid_value
                    if grid_value == ".":
                        break
                pos_init = (pos_init[0] - 1, pos_init[1])
        if direction == 'v':
            array_direction = {}
            pos_init = pos
            while True:
                grid_value = grid[pos_init[1]][pos_init[0]]
                if grid_value == "#":
                    break
                else:
                    array_direction[pos_init] = grid_value
                    if grid_value == ".":
                        break
                pos_init = (pos_init[0], pos_init[1] + 1)

        if "." in array_direction.values():
            positions = [key for key in array_direction.keys()]
            values = [value for value in array_direction.values()]
            values.pop(-1)
            values = ['.'] + values
            for key, value in zip(positions, values):
                new_grid[key[1]][key[0]] = value

        for y in range(len(new_grid)):
            for x in range(len(new_grid[y])):
                if new_grid[y][x] == "@":
                    new_pos = (x, y)
                    break

    return new_grid, new_pos


# Look for initial robot position
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == "@":
            pos = (x, y)
            break

for movement in movements:
    grid, pos = move_robot(grid, pos, movement)

sum_ = 0
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == "O":
            sum_ += 100 * y + x
print(sum_)
