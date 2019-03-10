n = int(input("Enter any number : "))
rev = 0
temp = n
while n > 0 :
    dig = n % 10
    rev = rev * 10 + dig
    n = n // 10

if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
