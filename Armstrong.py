n = int(input("Enter a number : "))
total = 0
temp = n
while n > 0:
    dig = n % 10
    total = total + dig*dig*dig
    n = n // 10
if temp == total:
    print("Armstrong")
else:
    print("Not Armstrong")
