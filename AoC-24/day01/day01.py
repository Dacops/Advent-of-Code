def star1(file):
    with open(file, 'r') as f:
        lines = f.readlines()

    left, right = [], []
    for pair in lines:
        pair = pair.strip()
        pair = pair.split('   ')
        left.append(pair[0])
        right.append(pair[1])

    left.sort()
    right.sort()

    val = 0
    for l,r in zip(left, right):
        val += abs(int(l) - int(r))

    return val

def star2(file):
    with open(file, 'r') as f:
        lines = f.readlines()

    left, right = [], {}
    for pair in lines:
        pair = pair.strip()
        pair = pair.split('   ')
        left.append(pair[0])
        
        if pair[1] not in right:
            right[pair[1]] = 1
        else:
            right[pair[1]] += 1

    val = 0
    for lines in left:
        if lines in right:
            val += int(lines) * right[lines]

    return val

print(f"STAR 1: {star1('input.txt')}")
print(f"STAR 2: {star2('input.txt')}")