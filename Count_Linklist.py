class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printlist(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next

    def getCount(self):
        last = self.head
        count = 0
        while last:
            count = count + 1
            last = last.next
        return count

myList = LinkedList()
myList.head = Node("mon")
e2 = Node("tue")
e3 = Node("wed")
e4 = Node("thu")
myList.head.next = e2
e2.next = e3
e3.next = e4
myList.printlist()
print ("Count of nodes is :",myList.getCount())
