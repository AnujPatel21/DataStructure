
def findmissing(original_list):
    num_list= [i for i in range(original_list[0], original_list[-1]+ 1)]
    result = list(set(original_list) ^ set(num_list))
    return result

print(findmissing([1,2,3,5,6,7,9,11,12]))
