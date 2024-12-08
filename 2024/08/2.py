def combinations(iterable, r=2):
    pool = tuple(iterable)
    n = len(pool)

    if r > n:
        return

    def generate_combinations(indices, start):
        if len(indices) == r:
            yield tuple(pool[i] for i in indices)
        else:
            for i in range(start, n):
                indices.append(i)
                yield from generate_combinations(indices, i + 1)
                indices.pop()

    yield from generate_combinations([], 0)


with open("./2024/08/input.txt") as f:
    grid = [[c for c in line.strip()] for line in f.readlines()]


def get_antennas_coordinates(grid):
    antennas = {}
    for j, line in enumerate(grid):
        for i, c in enumerate(line):
            grid_char = grid[i][j]
            if grid_char == ".":
                continue
            if grid_char in antennas:
                antennas[grid_char].add((i, j))
            else:
                antennas[grid_char] = {(i, j)}
    return antennas


# Conting antinodes in the grid
antinodes_count = 0
antinodes_overlap = 0
antinodes = set()

for antenna_id, coords in get_antennas_coordinates(grid).items():
    print("working on antenna", antenna_id)
    combs = combinations(coords, 2)
    for antenna_1, antenna_2 in combs:
        # XXX: this 1000 is just a random number, is there a better way?
        for n in range(1, 1000):
            antinode_1 = (
                antenna_1[0] + n * (antenna_1[0] - antenna_2[0]),
                antenna_1[1] + n * (antenna_1[1] - antenna_2[1])
            )
            antinode_2 = (
                antenna_2[0] + n * (antenna_2[0] - antenna_1[0]),
                antenna_2[1] + n * (antenna_2[1] - antenna_1[1])
            )
            antinodes.add(antenna_1)
            antinodes.add(antenna_2)
            antinodes.add(antinode_1)
            antinodes.add(antinode_2)


# Updating grid with antinodes
for antinode in antinodes:
    if antinode[0] < 0 or antinode[1] < 0:
        continue
    try:
        if grid[antinode[0]][antinode[1]] == ".":
            grid[antinode[0]][antinode[1]] = "#"
        else:
            antinodes_overlap += 1
    except IndexError:
        # Out of bounds
        continue

for line in grid:
    antinodes_count += line.count("#")

print("Antinodes count:", antinodes_count + antinodes_overlap)
