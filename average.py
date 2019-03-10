list1 = []
n = int(input("Enter size of list : "))
for i in range(0,n):
    elem = int(input("Enter numbers : "))
    list1.append(elem)
avg = sum(list1) // n
print avg
