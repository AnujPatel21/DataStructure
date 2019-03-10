class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linklist:
    def __init__(self):
        self.head = None

    def middle(self):
        list1 = []
        curr = self.head
        while curr is not None:
            list1.append(curr.data)
            curr = curr.next
        return list1[len(list1)//2]

    def printlist(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next



myList = Linklist()
myList.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
myList.head.next = e2
e2.next = e3
myList.printlist()
print(myList.middle())
