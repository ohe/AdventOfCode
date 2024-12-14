wide = 101
tall = 103

grid = [[0 for _ in range(wide)] for _ in range(tall)]

bots = {}
id_ = 0
with open('./2024/14/input.txt') as f:
    while line := f.readline():

        position, velocity = line.strip().split(" ")
        x, y = map(int, position[2:].split(","))
        vx, vy = map(int, velocity[2:].split(","))
        bots[(id_, (x, y))] = (vx, vy)
        id_ += 1

max_mult = 0
max_iter = 0
for nb_iterations in range(10000):
    grid = [[0 for _ in range(wide)] for _ in range(tall)]

    for id_, bot in bots.keys():
        final_pos = (
            (bot[0] + nb_iterations * bots[(id_, bot)][0]) % wide,
            (bot[1] + nb_iterations * bots[(id_, bot)][1]) % tall
        )
        grid[final_pos[1]][final_pos[0]] += 1

    mult = 1
    for y in range(tall):
        for x in range(wide):
            sum_ = 0
            if grid[y][x] >= 1:
                sum_ = grid[y][x]
                # suming the number of up down left right
                if x > 0:
                    sum_ += grid[y][x-1]
                if y > 0:
                    sum_ += grid[y-1][x]
                if x < wide - 1:
                    sum_ += grid[y][x+1]
                if y < tall - 1:
                    sum_ += grid[y+1][x]
            if sum_ > 1:
                mult *= sum_
    if mult > max_mult:
        for line in grid:
            print("".join(map(str, line)))
        max_mult = mult
        max_iter = nb_iterations

# The approach is to find the iteration
# where the grouping of bots is the highest
# it works !
print(max_mult, max_iter)
