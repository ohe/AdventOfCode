grid = []
with open('./2024/04/input.txt') as f:
    lines = f.readlines()
    for line in lines:
        grid.append([c for c in line.strip()])


xmas_count = 0
for j, line in enumerate(grid):
    for i, c in enumerate(line):
        if c == 'A':
            # Look for X-MAS pattern
            # M.S
            # .A.
            # M.S
            try:
                if i-1 >= 0 and j-1 >= 0 and grid[j-1][i-1] == 'M' and grid[j-1][i+1] == 'S' and grid[j+1][i-1] == 'M' and grid[j+1][i+1] == 'S':
                    xmas_count += 1
            except IndexError:
                pass
            # S.M
            # .A.
            # S.M
            try:
                if i-1 >= 0 and j-1 >= 0 and grid[j-1][i-1] == 'S' and grid[j-1][i+1] == 'M' and grid[j+1][i-1] == 'S' and grid[j+1][i+1] == 'M':
                    xmas_count += 1
            except IndexError:
                pass
            # M.M
            # .A.
            # S.S
            try:
                if i-1 >= 0 and j-1 >= 0 and grid[j-1][i-1] == 'M' and grid[j-1][i+1] == 'M' and grid[j+1][i-1] == 'S' and grid[j+1][i+1] == 'S':
                    xmas_count += 1
            except IndexError:
                pass
            # S.S
            # .A.
            # M.M
            try:
                if i-1 >= 0 and j-1 >= 0 and grid[j-1][i-1] == 'S' and grid[j-1][i+1] == 'S' and grid[j+1][i-1] == 'M' and grid[j+1][i+1] == 'M':
                    xmas_count += 1
            except IndexError:
                pass


print(xmas_count)
