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

    def reverse_list(self):
        prev = None
        current = self.head
        while current.next is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev



myList = LinkedList()
myList.head = Node("mon")
e2 = Node("tue")
e3 = Node("wed")
myList.head.next = e2
e2.next = e3
myList.printlist()
myList.reverse_list()
myList.printlist()
