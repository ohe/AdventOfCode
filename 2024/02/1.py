levels_list = []
with open('./2024/02/input.txt') as f:
    while line := f.readline().strip():
        levels_list.append([int(e) for e in line.split(" ") if e])

nb_unsafe = 0
for levels in levels_list:
    is_level_all_increasing = all(
        levels[i] < levels[i + 1] for i in range(len(levels) - 1)
     )
    is_level_all_decreasing = all(
        levels[i] > levels[i + 1] for i in range(len(levels) - 1)
    )
    if is_level_all_decreasing:
        if not all(
            [4 > levels[i] - levels[i+1] > 0 for i in range(len(levels) - 1)]
        ):
            nb_unsafe += 1
    elif is_level_all_increasing:
        if not all(
            [4 > levels[i+1] - levels[i] > 0 for i in range(len(levels) - 1)]
        ):
            nb_unsafe += 1
    else:
        nb_unsafe += 1

print(len(levels_list) - nb_unsafe)
