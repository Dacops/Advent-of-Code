def star1(file):
    with open(file, 'r') as f:
        lines = f.readlines()

    lab = []
    for line in lines:
        line = line.strip()
        lab.append(list(line))

    x, y = 0, 0
    for i in range(len(lab)):
        for j in range(len(lab[i])):
            if lab[i][j] == '^':
                y, x = i, j
                break

    direction = 'up'
    while True:
        if direction == 'up':
            if y-1 < 0:
                lab[y][x] = 'X'
                break
            if lab[y-1][x] == '#':
                direction = 'right'
            else:
                lab[y][x] = 'X'
                y -= 1

        elif direction == 'right':
            if x+1 >= len(lab[y]):
                lab[y][x] = 'X'
                break
            if lab[y][x+1] == '#':
                direction = 'down'
            else:
                lab[y][x] = 'X'
                x += 1

        elif direction == 'down':
            if y+1 >= len(lab):
                lab[y][x] = 'X'
                break
            if lab[y+1][x] == '#':
                direction = 'left'
            else:
                lab[y][x] = 'X'
                y += 1

        elif direction == 'left':
            if x-1 < 0:
                lab[y][x] = 'X'
                break
            if lab[y][x-1] == '#':
                direction = 'up'
            else:
                lab[y][x] = 'X'
                x -= 1

    steps = 0
    for l in lab:
        steps += l.count('X')
    return steps

def check_loops(lab, x, y, direction, nob):
    
    nlab = [list(l) for l in lab]
    nlab[nob[1]][nob[0]] = '#'
    times = 0
    while True:

        if times > 5774:
            return 1
        times += 1

        if direction == 'up':
            if y-1 < 0:
                return 0
            if nlab[y-1][x] == '#':
                direction = 'right'
            else:
                y -= 1

        elif direction == 'right':
            if x+1 >= len(nlab[y]):
                return 0
            if nlab[y][x+1] == '#':
                direction = 'down'
            else:
                x += 1

        elif direction == 'down':
            if y+1 >= len(nlab):
                return 0
            if nlab[y+1][x] == '#':
                direction = 'left'
            else:
                y += 1

        elif direction == 'left':
            if x-1 < 0:
                return 0
            if nlab[y][x-1] == '#':
                direction = 'up'
            else:
                x -= 1


def star2(file):
    with open(file, 'r') as f:
        lines = f.readlines()

    lab = []
    for line in lines:
        line = line.strip()
        lab.append(list(line))

    x, y = 0, 0
    for i in range(len(lab)):
        for j in range(len(lab[i])):
            if lab[i][j] == '^':
                y, x = i, j
                break

    direction, previous, visited = 'up', set(), set()
    visited.add((x, y))
    while True:
        if direction == 'up':
            if y-1 < 0:
                lab[y][x] = 'X'
                break
            if lab[y-1][x] == '#':
                direction = 'right'
            else:
                if (x, y-1) not in previous and (x, y-1) not in visited and check_loops(lab, x, y, direction, (x, y-1)):
                    previous.add((x, y-1))
                visited.add((x, y))
                lab[y][x] = 'X'
                y -= 1

        elif direction == 'right':
            if x+1 >= len(lab[y]):
                lab[y][x] = 'X'
                break
            if lab[y][x+1] == '#':
                direction = 'down'
            else:
                if (x+1, y) not in previous and (x+1, y) not in visited and check_loops(lab, x, y, direction, (x+1, y)):
                    previous.add((x+1, y))
                visited.add((x, y))
                lab[y][x] = 'X'
                x += 1

        elif direction == 'down':
            if y+1 >= len(lab):
                lab[y][x] = 'X'
                break
            if lab[y+1][x] == '#':
                direction = 'left'
            else:
                if (x, y+1) not in previous and (x, y+1) not in visited and check_loops(lab, x, y, direction, (x, y+1)):
                    previous.add((x, y+1))
                visited.add((x, y))
                lab[y][x] = 'X'
                y += 1

        elif direction == 'left':
            if x-1 < 0:
                lab[y][x] = 'X'
                break
            if lab[y][x-1] == '#':
                direction = 'up'
            else:
                if (x-1, y) not in previous and (x-1, y) not in visited and check_loops(lab, x, y, direction, (x-1, y)):
                    previous.add((x-1, y))
                visited.add((x, y))
                lab[y][x] = 'X'
                x -= 1

    return len(previous)

print(f"STAR 1: {star1('input.txt')}")
print(f"STAR 2: {star2('input.txt')}")