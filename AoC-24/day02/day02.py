def valid_line(line):
    increasing = None
    for i in range(len(line)-1):
        drop = int(line[i])-int(line[i+1])
        if abs(drop) < 1 or abs(drop) > 3:
            return False
        elif drop < 0:
            if increasing == None:
                increasing = True
            if increasing == False:
                return False
        else:
            if increasing == None:
                increasing = False
            if increasing == True:
                return False
    return True

def star1(file):
    with open(file, 'r') as f:
        lines = f.readlines()

    safe = 0
    for line in lines:
        line = line.strip()
        line = line.split(' ')

        if valid_line(line):
            safe += 1

    return safe

def star2(file):
    with open(file, 'r') as f:
        lines = f.readlines()

    safe = 0
    for line in lines:
        line = line.strip()
        line = line.split(' ')

        if valid_line(line):
            safe += 1

        else:
            # bruteforce removing levels
            lines = []
            for i in range(len(line)):
                lines.append(line[:i] + line[i+1:])

            for line in lines:
                if valid_line(line):
                    safe += 1
                    break
    
    return safe

print(f"STAR 1: {star1('input.txt')}")
print(f"STAR 2: {star2('input.txt')}")