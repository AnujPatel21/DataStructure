def bubble(myList):
    for i in range(0,len(myList)-1):
        for j in range(0,len(myList)-1-i):
            if myList[j] > myList[j+1]:
                myList[j],myList[j+1] = myList[j+1],myList[j]
    return myList

myList = [1,4,3,2]
print(myList)
print(bubble(myList))
