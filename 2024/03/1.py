import re

with open('./2024/03/input.txt') as f:
    lines = '\n'.join(f.readlines())

matches = re.findall(r'mul\(\d+,\d+\)', lines)

def mul(a, b):
    return a * b

print(sum([eval(match) for match in matches]))