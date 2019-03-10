def findduplicate(original_list):
    sizee = len(original_list)
    result = []
    for i in range(sizee):
        k = i + 1
        for j in range(k,sizee):
            if original_list[i] == original_list[j] and original_list[i] not in result:
                result.append(original_list[i])
    return(result)
l = [1,2,2,3,4,5,1,6,7,8, 7]
print(l)
print(findduplicate(l))
