def parse_input(file):
    with open(file, 'r') as f:
        lines = f.readlines()

    change = 0
    updates, after = [], {}
    for line in lines:
        if line == '\n':
            change = 1
            continue

        if not change:
            line = line.strip()
            line = line.split('|')
            if line[1] in after:
                after[line[1]].append(line[0])
            else:
                after[line[1]] = [line[0]]

        else:
            line = line.strip()
            line = line.split(',')
            updates.append(line)

    return updates, after

def star1(file):
    updates, after = parse_input(file)
    value = 0
    for update in updates:
        mid_page = int(update[len(update)//2])
        value += mid_page
        for i in range(len(update)):
            if update[len(update)-(1+i)] in after and bool(set(after[update[len(update)-(1+i)]]) & set(update[len(update)-i:len(update)])):
                value -= mid_page
                break
    return value

def update_order(update, after):
    for i in range(len(update)):
        if update[len(update)-(1+i)] in after and (set(after[update[len(update)-(1+i)]]) & set(update[len(update)-i:len(update)])):
            curr = update[len(update)-(1+i)]
            target = (set(after[curr]) & set(update[len(update)-i:len(update)]))
            for j in range(len(update)):
                trade_with = target & set([update[len(update)-(1+j)]])
                if trade_with:
                    update[len(update)-(1+j)] = curr
                    update[len(update)-(1+i)] = trade_with.pop()
                    return (True, update, after)
    return (False, update, after)

def star2(file):
    updates, after = parse_input(file)
    
    value = 0
    for i in range(len(updates)):
        updated, count = True, 0
        while updated:
            updated, updates[i], after = update_order(updates[i], after)
            count += 1

        if count > 1:
            value += int(updates[i][len(updates[i])//2])
    
    return value


print(f"STAR 1: {star1('input.txt')}")
print(f"STAR 2: {star2('input.txt')}")