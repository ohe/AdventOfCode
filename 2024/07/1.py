equations = []
with open('2024/07/input.txt') as f:
    while line := f.readline():
        result, parts = [e.strip() for e in line.split(':')]
        parts = map(int, parts.split(' '))
        equations.append((int(result), list(parts)))


def combinations(available_operators=['+', '*'], n=2):
    if n == 1:
        return available_operators
    return [op + c for op in available_operators for c in combinations(
        available_operators, n - 1)
    ]


calibrations = 0
for equation in equations:
    print(processing := equations.index(equation) + 1, '/', len(equations))
    result, parts = equation
    for combination in combinations(n=len(parts) - 1):
        test_result = parts[0]
        for ix, op in enumerate(combination):
            if op == '+':
                test_result += parts[ix + 1]
            elif op == '*':
                test_result *= parts[ix + 1]
        if test_result == result:
            calibrations += result
            break

print("-->", calibrations)
