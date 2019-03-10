n = int(input("Enter a number : "))
a = []
for i in range(1,n+1):
    elem = int(input("Enter numbers : "))
    a.append(elem)
temp = a[0]
a[0] = a[-1]
a[-1] = temp
print(a)
