n = int(input("Enter the number : "))
total = 0
while n > 0:
    dig = n % 10
    total = total + dig
    n = n // 10
print("sum : ", total)
