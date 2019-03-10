def pairs(sum, list1):
    length = len(list1)
    result = []
    for i in range(length):
        for j in range(i+1,length):
            if list1[i] + list1[j] == sum:
                result.append((list1[i],list1[j]))
    return result

l = [1,2,3,4,6,7,8,9,11]
sum = 10
print(l)
print(pairs(sum,l))
