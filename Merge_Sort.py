def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list

    middle = len(unsorted_list) // 2
    left_half = unsorted_list[:middle]
    right_half = unsorted_list[middle:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    return list(merge(left_half,right_half))

def merge (left_half,right_half):
    result = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            result.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            result.append(right_half[0])
            right_half.remove(right_half[0])
    if len(left_half) == 0:
        result = result + right_half
    else:
        result = result + left_half
    return result

unsorted_list = [9,8,7,6,5,4,3,2,1]
print(merge_sort(unsorted_list))
