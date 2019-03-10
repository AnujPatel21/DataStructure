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


    def printNthFromLast(self, n):
        temp = self.head
        length = 0
        while temp is not None:
            temp = temp.next
            length += 1
        if n > length:
            print('Location is greater than the size of Linklist')
            return
        temp = self.head
        for i in range(0, length - n):
            temp = temp.next
        print(temp.data)

myList = LinkedList()
myList.head = Node("mon")
e2 = Node("tue")
e3 = Node("wed")
e4 = Node("thu")
myList.head.next = e2
e2.next = e3
e3.next = e4
myList.printlist()
myList.printNthFromLast(3)
