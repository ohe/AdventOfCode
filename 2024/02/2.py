levels_list = []
with open('./2024/02/input.txt') as f:
    while line := f.readline().strip():
        levels_list.append([int(e) for e in line.split(" ") if e])


def is_safe(levels):
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
            return False
        else:
            return True
    elif is_level_all_increasing:
        if not all(
            [4 > levels[i+1] - levels[i] > 0 for i in range(len(levels) - 1)]
        ):
            return False
        else:
            return True
    else:
        return False


nb_safe = 0
for levels in levels_list:
    safe = is_safe(levels)
    if not safe:
        for i in range(len(levels)):
            temp = levels.copy()
            temp.pop(i)
            safe_temp = is_safe(temp)
            if safe_temp:
                nb_safe += 1
                break
    else:
        nb_safe += 1

print(nb_safe)
