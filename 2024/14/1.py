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

nb_iterations = 100
for id_, bot in bots.keys():
    final_pos = (
        (bot[0] + nb_iterations * bots[(id_, bot)][0]) % wide,
        (bot[1] + nb_iterations * bots[(id_, bot)][1]) % tall
    )
    grid[final_pos[1]][final_pos[0]] += 1


q1_sum = 0
for y in range(tall//2):
    for x in range(wide//2):
        q1_sum += grid[y][x]
print(q1_sum)

q3_sum = 0
for y in range(tall//2 + 1, tall):
    for x in range(wide//2):
        q3_sum += grid[y][x]
print(q3_sum)

q2_sum = 0
for y in range(tall//2):
    for x in range(wide//2 + 1, wide):
        q2_sum += grid[y][x]
print(q2_sum)

q4_sum = 0
for y in range(tall//2 + 1, tall):
    for x in range(wide//2 + 1, wide):
        q4_sum += grid[y][x]
print(q4_sum)

print(q1_sum * q3_sum * q4_sum * q2_sum)
