left_list = []
right_list = []

with open('./2024/01/input.txt') as f:
    while line := f.readline().strip():
        left, right = [int(e) for e in line.split() if e]
        left_list.append(left)
        right_list.append(right)

right_list_counter = {}
for right in right_list:
    if right in right_list_counter:
        right_list_counter[right] += 1
    else:
        right_list_counter[right] = 1

similarity = 0
for left in left_list:
    similarity += left * right_list_counter.get(left, 0)

print(similarity)
