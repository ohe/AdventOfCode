left_list = []
right_list = []

with open('./2024/01/input.txt') as f:
    while line := f.readline().strip():
        left, right = [int(e) for e in line.split(" ") if e]
        left_list.append(left)
        right_list.append(right)

left_list = sorted(left_list)
right_list = sorted(right_list)

sum_ = 0
for left, right in zip(left_list, right_list):
    sum_ += abs(left - right)

print(sum_)
