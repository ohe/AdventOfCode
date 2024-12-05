import re


def mul(a, b):
    return a * b


with open('./2024/03/input.txt') as f:
    lines = ''.join(f.readlines())

lines = re.sub(r"don't\(\).*?($|do\(\))", '', lines, flags=re.DOTALL)
matches = re.findall(r'mul\(\d+,\d+\)', lines)
print(sum([eval(match) for match in matches]))
