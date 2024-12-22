def star1(file):
    with open(file, 'r') as f:
        lines = f.readlines()

    for i in range(len(lines)):
        lines[i] = lines[i].strip()

    xmas = 0
    # horizontal scans
    for i in range(len(lines)):
        for j in range(len(lines[0])-3):
            if lines[i][j:j+4] == "XMAS" or lines[i][j:j+4] == "SAMX":
                xmas += 1


    for i in range(len(lines)-3):
        # vertical scans
        for j in range(len(lines[0])):
            if lines[i][j] == 'X' and lines[i+1][j] == 'M' and lines[i+2][j] == 'A' and lines[i+3][j] == 'S' or \
                lines[i][j] == 'S' and lines[i+1][j] == 'A' and lines[i+2][j] == 'M' and lines[i+3][j] == 'X':
                xmas += 1

        # diagonal scans
        for j in range(len(lines[0])-3):
            if lines[i][j] == 'X' and lines[i+1][j+1] == 'M' and lines[i+2][j+2] == 'A' and lines[i+3][j+3] == 'S' or \
                lines[i][j] == 'S' and lines[i+1][j+1] == 'A' and lines[i+2][j+2] == 'M' and lines[i+3][j+3] == 'X':
                xmas += 1

            if lines[i][j+3] == 'X' and lines[i+1][j+2] == 'M' and lines[i+2][j+1] == 'A' and lines[i+3][j] == 'S' or \
                lines[i][j+3] == 'S' and lines[i+1][j+2] == 'A' and lines[i+2][j+1] == 'M' and lines[i+3][j] == 'X':
                xmas += 1

    return xmas


def star2(file):
    with open(file, 'r') as f:
        lines = f.readlines()

    for i in range(len(lines)):
        lines[i] = lines[i].strip()

    xmas = 0
    for i in range(len(lines)-2):
        for j in range(len(lines[0])-2):
            if ((lines[i][j] == 'M' and lines[i+2][j+2] == 'S') or (lines[i][j] == 'S' and lines[i+2][j+2] == 'M')) and \
                ((lines[i][j+2] == 'M' and lines[i+2][j] == 'S') or (lines[i][j+2] == 'S' and lines[i+2][j] == 'M')) and \
                lines[i+1][j+1] == 'A':
                xmas += 1
    
    return xmas



print(f"STAR 1: {star1('input.txt')}")
print(f"STAR 2: {star2('input.txt')}")