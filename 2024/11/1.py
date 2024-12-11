def blink(stones):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            new_stones.extend([int(str(stone)[:len(str(stone))//2]), int(str(stone)[len(str(stone))//2:])])
        else:
            new_stones.append(stone * 2024)
    return new_stones

with open("./2024/11/input.txt", "r") as f:
    stones = [int(e) for e in f.readline().strip().split()]

nb_blink = 25
for x in range(nb_blink):
    stones = blink(stones)
print(len(stones))