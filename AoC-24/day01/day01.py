def star1(file):
    with open(file, 'r') as f:
        vals = f.readlines()

    left, right = [], []
    for pair in vals:
        pair = pair.strip()
        pair = pair.split('   ')
        left.append(pair[0])
        right.append(pair[1])

    left.sort()
    right.sort()

    val = 0
    for vals in zip(left, right):
        val += abs(int(vals[0]) - int(vals[1]))

    return val

def star2(file):
    with open(file, 'r') as f:
        vals = f.readlines()

    left, right = [], {}
    for pair in vals:
        pair = pair.strip()
        pair = pair.split('   ')
        left.append(pair[0])
        
        if pair[1] not in right:
            right[pair[1]] = 1
        else:
            right[pair[1]] += 1

    val = 0
    for vals in left:
        if vals in right:
            val += int(vals) * right[vals]

    return val

print(f"STAR 1: {star1('input.txt')}")
print(f"STAR 2: {star2('input.txt')}")