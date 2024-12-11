TEST_STRING = "2333133121414131402"

array = []

with open("./2024/09/input.txt", "r") as f:
    line = f.readline().strip()


file_idx = 0
total_length = 0
for i, char in enumerate(line):
    length = int(char)
    if length == 0:
        continue
    if i % 2 == 0:

        array.append(
            (
                str(file_idx),
                total_length,
                total_length + length - 1,
                length
            )
        )
        file_idx += 1
    else:
        array.append(
            (
                ".",
                total_length,
                total_length + length - 1,
                length
            )
        )
    total_length += length

array_copy = array.copy()

first_dot = [i for i, e in enumerate(array_copy) if e[0] == "."][0]
reversed_file_idx = list(
    reversed(
        [e for e in array_copy[first_dot:] if e[0] != "."]
    )
)


def iterate(array_copy, reversed_file_idx):
    stable = False
    while not stable:
        for i, elem in enumerate(array_copy):
            if elem[0] == ".":
                dot_length = elem[3]
                for ri, reversed_elem in enumerate(reversed_file_idx):
                    if reversed_elem[1] < elem[1]:
                        continue
                    reversed_length = reversed_elem[3]
                    if reversed_length == dot_length:
                        array_copy_idx = array_copy.index(reversed_elem)
                        array_copy[array_copy_idx] = ('.',) + reversed_elem[1:]

                        reversed_elem = (
                            reversed_elem[0],
                            elem[1],
                            elem[1] + reversed_length - 1,
                            reversed_length
                        )
                        array_copy[i] = reversed_elem
                        reversed_file_idx.pop(ri)
                        stable = False
                        break
                    if reversed_length < dot_length:
                        array_copy_idx = array_copy.index(reversed_elem)
                        array_copy[array_copy_idx] = ('.',) + reversed_elem[1:]

                        new_array_elem = (
                            '.',
                            elem[1] + reversed_length,
                            elem[1] + dot_length - 1,
                            dot_length - reversed_length
                        )
                        reversed_elem = (
                            reversed_elem[0],
                            elem[1],
                            elem[1] + reversed_length - 1,
                            reversed_length
                        )
                        array_copy[i] = reversed_elem
                        array_copy.insert(i + 1, new_array_elem)
                        reversed_file_idx.pop(ri)
                        stable = False
                        break

        else:
            stable = True
    return array_copy


array_result = iterate(array_copy, reversed_file_idx)
array_result = [[[e[0]]*e[3]] for e in array_result]

# Double flatten
array_result = sum(sum(array_result, []), [])

print(sum([i * int(x) for i, x in enumerate(array_result) if x != "."]))
