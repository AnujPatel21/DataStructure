def largest(list1):
    return(max(list1))

def smallest(list1):
    return(min(list1))

def large(list1):
    a = 1
    for i in list1:
        if a < i:
            a = i
    return(a)

def small(list1):
    a = 1
    for i in list1:
        if a >= i:
            a = i
    return(a)

l = [4,5,7,9,2,3]
print(largest(l))
print(smallest(l))
print(large(l))
print(small(l))
