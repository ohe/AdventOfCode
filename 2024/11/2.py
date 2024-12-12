CACHE = {}


def nb_new_stones(steps, stone):
    if (steps, stone) in CACHE:
        return CACHE[(steps, stone)]
    if steps == 0:
        return 1
    elif stone == 0:
        total = nb_new_stones(steps - 1, 1)
    elif len(str(stone)) % 2 == 0:
        n = len(str(stone))
        stone_1, stone_2 = int(str(stone)[:n // 2]), int(str(stone)[n // 2:])
        total = (
            nb_new_stones(steps - 1, stone_1) +
            nb_new_stones(steps - 1, stone_2)
        )
    else:
        total = nb_new_stones(steps - 1, 2024 * stone)
    CACHE[(steps, stone)] = total
    return total


with open("./2024/11/input.txt", "r") as f:
    stones = [int(e) for e in f.readline().strip().split()]


print(sum([nb_new_stones(75, stone) for stone in stones]))
