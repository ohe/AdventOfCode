from sympy import symbols, solve

equations = []
with open('./2024/13/input.txt') as f:
    while line := f.readline():
        line = line.strip()
        if line.startswith('Button A'):
            _, eq_part1 = line.split(':')
            eq_part1 = eq_part1.replace('Y+', 'a*').replace('X+', 'a*')
        if line.startswith('Button B'):
            _, eq_part2 = line.split(':')
            eq_part2 = eq_part2.replace('Y+', 'b*').replace('X+', 'b*')

        if line.startswith('Prize'):
            _, eq_part3 = line.split(':')
            x1, y1 = eq_part1.split(', ')
            x2, y2 = eq_part2.split(', ')
            x3, y3 = eq_part3.split(', ')

            _, x3 = x3.split('=')
            _, y3 = y3.split('=')

            eq = (x1 + ' + ' + x2 + '-' + x3, y1 + ' + ' + y2 + '-' + y3)
            equations.append(eq)


sum_ = 0
a, b = symbols(['a', 'b'])
for (eq1, eq2) in equations:
    eq1 = eval(eq1)
    eq2 = eval(eq2)
    print(eq1)
    sol = solve((eq1, eq2), [a, b])

    if sol[a].is_integer and sol[b].is_integer:
        prize_tokens = sol[a] * 3 + sol[b] * 1
        sum_ += prize_tokens

print(sum_)
