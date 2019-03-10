def remove(list1):
    result = []
    for i in list1:
        if i not in result:
            result.append(i)
    return(result)

l = [1,2,2,3,4,5,6,6,7,8,9,9,10]
print(remove(l))
