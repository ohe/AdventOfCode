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

error_updates = []
for update in updates:
    for ix in range(len(update) - 1):
        try:
            descendants = updates_order[update[ix]]
        except KeyError:
            error_updates.append(update)
            break
        if update[ix + 1] not in descendants:
            error_updates.append(update)
            break


def try_fix(update):
    for ix in range(len(update) - 1):
        try:
            descendants = updates_order[update[ix]]
        except KeyError:
            # swap ix and ix + 1 and recall try_fix
            update[ix], update[ix + 1] = update[ix + 1], update[ix]
            return try_fix(update)
        if update[ix + 1] not in descendants:
            # swap ix and ix + 1 and recall try_fix
            update[ix], update[ix + 1] = update[ix + 1], update[ix]
            return try_fix(update)
    return update


good_updates = [try_fix(update) for update in error_updates]
print(sum([update[(len(update) - 1)//2] for update in good_updates]))
