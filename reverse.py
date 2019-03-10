def reversee(list1):
    result = []
    for i in range(len(list1), 0, -1):
        result.append(list1[i-1])
    return result

l = [1,2,3,4,5,6,7]
print(reversee(l))
