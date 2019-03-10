def mygen():
    n=1
    print("1st")
    yield n

    n=n+1
    print("2nd")
    yield n

    n=n+1
    print("3rd")
    yield n

for i in mygen():
    print(i)
