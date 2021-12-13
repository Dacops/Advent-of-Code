def function(file):
    with open(file,'r') as f:
        lst=f.readlines()
    for l in lst: l.rstrip()




print(function('C:\\Users\\david\\OneDrive\\Desktop\\GitHub\\AoC_21\\Day14\\day14_INPUT.txt'))