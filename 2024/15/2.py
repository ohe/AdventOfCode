grid = []
movements = ""


def wide_transform(elem_list):
    wide_list = []

    mapper = {
        "#": ["#", "#"],
        "O": ["[", "]"],
        ".": [".", "."],
        "@": ["@", "."]
    }
    for elem in elem_list:
        wide_list.extend(mapper[elem])

    return wide_list


with open('./2024/15/input.txt', 'r') as f:
    while line := f.readline():
        line = line.strip()
        if line.startswith('#'):
            wide_line = wide_transform(list(line))
            grid.append(wide_line)
        else:
            movements += line


move_by = {'^': (0, -1), 'v': (0, 1), '<': (-1, 0), '>': (1, 0)}


class Point():
    def __init__(self, x, y) -> None:
        self.x: int = x
        self.y: int = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)


def get_adgacents(grid, pos, direction):
    edges = []
    adjacents = set()
    queue = [pos]
    while queue:
        current_pos = queue.pop(0)
        if current_pos in adjacents:
            continue
        adjacents.add(current_pos)
        next_pos = Point(
            current_pos.x + move_by[direction][0],
            current_pos.y + move_by[direction][1]
        )
        if grid[next_pos.y][next_pos.x] in ["#", "."]:
            edges.append(current_pos)
        elif grid[next_pos.y][next_pos.x] == "[":
            box_pos_1 = Point(next_pos.x, next_pos.y)
            box_pos_2 = Point(next_pos.x + 1, next_pos.y)
            queue.append(box_pos_1)
            queue.append(box_pos_2)
        elif grid[next_pos.y][next_pos.x] == "]":
            box_pos_1 = Point(next_pos.x - 1, next_pos.y)
            box_pos_2 = Point(next_pos.x, next_pos.y)
            queue.append(box_pos_2)
            queue.append(box_pos_1)
    adjacents.remove(pos)
    return edges, adjacents


def update_grid(grid, adjacents, direction):
    visits = []
    match direction:
        case "^":
            visits = sorted(adjacents, key=lambda x: x.y)
        case "v":
            visits = sorted(adjacents, key=lambda x: x.y, reverse=True)
        case "<":
            visits = sorted(adjacents, key=lambda x: x.x)
        case ">":
            visits = sorted(adjacents, key=lambda x: x.x, reverse=True)
    dx, dy = move_by[direction]
    for visit in visits:
        current_pos = visit
        next_pos = Point(visit.x + dx, visit.y + dy)
        grid[next_pos.y][next_pos.x] = grid[current_pos.y][current_pos.x]
        grid[current_pos.y][current_pos.x] = "."
    return grid


def move_robot(grid, pos: Point, direction):
    expeted_new_pos = Point(
        pos.x + move_by[direction][0],
        pos.y + move_by[direction][1]
    )

    if grid[expeted_new_pos.y][expeted_new_pos.x] == '#':
        return grid, pos

    if grid[expeted_new_pos.y][expeted_new_pos.x] == '.':
        grid[expeted_new_pos.y][expeted_new_pos.x] = '@'
        grid[pos.y][pos.x] = '.'
        return grid, expeted_new_pos

    else:  # Either [ or ]
        edges, adjacents = get_adgacents(grid, pos, direction)
        blocked = False
        dx, dy = move_by[direction]
        for cell in edges:
            next_pos = Point(cell.x + dx, cell.y + dy)
            if grid[next_pos.y][next_pos.x] == "#":
                blocked = True
        if blocked is False:
            grid = update_grid(grid, adjacents, direction)
            next_pos = Point(pos.x + dx, pos.y + dy)
            return grid, next_pos
        else:
            return grid, pos


# Look for initial robot position
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == "@":
            pos = Point(x, y)
            break


for movement in movements:
    grid, pos = move_robot(grid, pos, movement)

sum_ = 0
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == "[":
            sum_ += 100 * y + x
print(sum_)
