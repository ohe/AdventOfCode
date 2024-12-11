array = []
with open("./2024/09/input.txt", "r") as f:
    line = f.readline().strip()


result_str = ""
file_idx = 0
for i, char in enumerate(line):
    length = int(char)
    if i % 2 == 0:
        for idx in range(length):
            array.append(str(file_idx))
        file_idx += 1
    else:
        for idx in range(length):
            array.append(".")

dot_idx = [idx for idx, elem in enumerate(array) if elem == "."]
reversed_file_id_idx_reversed = list(
    reversed(
        [(idx, elem) for idx, elem in enumerate(array) if elem != "."]
    )
)

array_result = array.copy()
for i, array_idx in enumerate(dot_idx):
    reversed_idx, reversed_elem = reversed_file_id_idx_reversed[i]
    array_result[array_idx] = reversed_elem
    array_result[reversed_idx] = "."
    if all([e == '.' for e in array_result[array_result.index('.'):]]):
        break

print(sum([i * int(x) for i, x in enumerate(array_result) if x != "."]))
