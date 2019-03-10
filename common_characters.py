a = raw_input("Enter string 1 : ")
b = raw_input("Enter string 2 : ")
c = list(set(a) & set(b))
for i in c:
    print(i)
