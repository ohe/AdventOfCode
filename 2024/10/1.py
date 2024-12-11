grid = []
with open("./2024/10/input.txt", "r") as f:
    while line := f.readline().strip():
        grid.append([int(e) if e != '.' else e for e in line])


class Node(object):
    def __init__(self, parent=None, pos=None, value=None):
        self.parent = parent
        self.pos = pos
        self.value = value
        self.children = set()
        self.set_parent(parent)

    def set_parent(self, parent):
        if self.parent and self.parent is not parent:
            self.parent.children.remove(self)
        self.parent = parent

    def add_child(self, node):
        self.children.add(node)
        node.set_parent(self)


def locate_zeros(grid):
    """
    Returns the list of root Nodes
    """
    zeros = []
    for y, row in enumerate(grid):
        for x, elem in enumerate(row):
            if elem == 0:
                zeros.append((x, y))
    return [Node(pos=zero, value=0) for zero in zeros]


def get_adjacent(grid, x, y):
    """
    Returns a list of adjacent elements.
    Adjacent means up, down, left, right. Diagonal elements are not included.
    """
    adjacent = []
    if x > 0:
        adjacent.append((x - 1, y))  # left
    if x < len(grid[0]) - 1:
        adjacent.append((x + 1, y))  # right
    if y > 0:
        adjacent.append((x, y - 1))  # up
    if y < len(grid) - 1:
        adjacent.append((x, y + 1))  # down
    return adjacent


def crawl_node(grid, node):
    adjacents = [
        (x, y) for x, y in get_adjacent(
            grid, *node.pos
        ) if grid[y][x] == node.value + 1
    ]
    if not adjacents:
        return node
    else:
        for adjacent in adjacents:
            x, y = adjacent
            new_child = Node(parent=node, pos=(x, y), value=node.value + 1)
            node.add_child(new_child)
            crawl_node(grid, new_child)
    return node


root_nodes = locate_zeros(grid)
filled_nodes = [crawl_node(grid, node) for node in root_nodes]


# Traverse filled_nodes and look for each of them the unique trail ends
sum_ = 0
for node in filled_nodes:
    unique_positions = set()
    stack = [node]
    while stack:
        current = stack.pop()
        if current.value == 9:
            unique_positions.add(current.pos)
        stack.extend(current.children)
    sum_ += len(unique_positions)

print(sum_)
