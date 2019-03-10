n = int(input("Enter a number : "))
a = []
for i in range(1,n+1):
    elem = int(input("Enter numbers : "))
    a.append(elem)
print("Second largest",a[n-2])
