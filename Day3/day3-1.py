def binary(lst):
    gamma, epsilon = '', ''
    for i in range(len(lst[0])-1):
        counter = {'0':0, '1':0}
        for line in lst:
            counter[line[i]]+=1
        if counter['0']>counter['1']:
            gamma,epsilon=gamma+'0',epsilon+'1'
        else:
            gamma,epsilon=gamma+'1',epsilon+'0'
    return int(gamma,2)*int(epsilon,2)


f = open('day3_INPUT.txt', 'r')
lst = f.readlines()
print(binary(lst))