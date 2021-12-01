def counter(lst):
    count = 0
    for i in range(len(lst)-3):
        ant = int(lst[i])
        num = int(lst[i+3])
        if num > ant:
            count+=1
    return count

f = open('day1_INPUT.txt', 'r')
lst = f.readlines()
print(counter(lst))