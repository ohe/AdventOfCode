grid = []
with open('./2024/04/input.txt') as f:
    lines = f.readlines()
    for line in lines:
        grid.append([c for c in line.strip()])


xmas_count = 0
for j, line in enumerate(grid):
    for i, c in enumerate(line):
        if c == 'X':
            # Look for XMAS in all directions
            # Right
            try:
                if line[i+1:i+4] == ['M', 'A', 'S']:
                    xmas_count += 1
            except IndexError:
                pass
            # Left
            try:
                if i-3 >= 0 and line[i-3:i] == ['S', 'A', 'M']:
                    xmas_count += 1
            except IndexError:
                pass
            # Down
            try:
                if [grid[j+1][i], grid[j+2][i], grid[j+3][i]] == ['M', 'A', 'S']:
                    xmas_count += 1
            except IndexError:
                pass
            # Up
            try:
                if j-3 >= 0 and [grid[j-1][i], grid[j-2][i], grid[j-3][i]] == ['M', 'A', 'S']:
                    xmas_count += 1
            except IndexError:
                pass
            # Down right
            try:
                if [grid[j+1][i+1], grid[j+2][i+2], grid[j+3][i+3]] == ['M', 'A', 'S']:
                    xmas_count += 1
            except IndexError:
                pass
            # Down left
            try:
                if i - 3 >= 0 and [grid[j+1][i-1], grid[j+2][i-2], grid[j+3][i-3]] == ['M', 'A', 'S']:
                    xmas_count += 1
            except IndexError:
                pass
            # Up right
            try:
                if j-3 >= 0 and [grid[j-1][i+1], grid[j-2][i+2], grid[j-3][i+3]] == ['M', 'A', 'S']:
                    xmas_count += 1
            except IndexError:
                pass
            # Up left
            try:
                if j-3 >= 0 and i-3 >= 0 and [grid[j-1][i-1], grid[j-2][i-2], grid[j-3][i-3]] == ['M', 'A', 'S']:
                    xmas_count += 1
            except IndexError:
                pass

print(xmas_count)
