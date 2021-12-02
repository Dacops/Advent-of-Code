def counter(lst):
    ant, count = None, 0
    for num in lst:
        num = int(num)
        if ant != None:
            if num > ant:
                count+=1
        ant = num
    return count

f = open('day1_INPUT.txt', 'r')
lst = f.readlines()
print(counter(lst))