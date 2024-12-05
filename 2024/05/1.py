with open('./2024/05/input.txt') as f:
    lines = f.readlines()

updates = []
updates_order = {}
for line in lines:
    if '|' in line:
        a, b = map(int, line.split('|'))
        if a in updates_order:
            updates_order[a].append(b)
        else:
            updates_order[a] = [b]
    elif ',' in line:
        page_update = list(map(int, line.split(',')))
        updates.append(page_update)

good_updates = []
for update in updates:
    for ix in range(len(update) - 1):
        try:
            descendants = updates_order[update[ix]]
        except KeyError:
            break
        if update[ix + 1] not in descendants:
            break
    else:
        good_updates.append(update)

print(sum([update[(len(update) - 1)//2] for update in good_updates]))
