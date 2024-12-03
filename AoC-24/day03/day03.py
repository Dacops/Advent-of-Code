import re

def star1(file):
    with open(file, 'r') as f:
        lines = f.readlines()

    pattern = r"mul\(\d{1,3},\d{1,3}\)"

    val, all_lines = 0, ""
    for line in lines:
        all_lines += line
    
    muls = re.findall(pattern, all_lines)
    for mul in muls:
        l,r = mul.strip('mul(').strip(')').split(',')
        val += int(l) * int(r)

    return val

def star2(file):
    with open(file, 'r') as f:
        lines = f.readlines()

    pattern = r"mul\(\d{1,3},\d{1,3}\)"

    val, all_lines = 0, ""
    for line in lines:
        all_lines += line

    do_and_donts = all_lines.split("don't")
    
    # default is do()
    muls_in_beggining = re.findall(pattern, do_and_donts[0])
    for mul in muls_in_beggining:
        l,r = mul.strip('mul(').strip(')').split(',')
        val += int(l) * int(r)

    for substring in do_and_donts[1:]:
        substring = substring.split('do()')
        for dos in substring[1:]:
            muls = re.findall(pattern, dos)
            for mul in muls:
                l,r = mul.strip('mul(').strip(')').split(',')
                val += int(l) * int(r)

    return val


print(f"STAR 1: {star1('input.txt')}")
print(f"STAR 2: {star2('input.txt')}")