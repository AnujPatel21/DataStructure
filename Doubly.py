class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class Doubly:
    def __init__(self):
        self.head = None

    def push(self,newval):
        newnode = Node(newval)
        newnode.next = self.head
        if self.head is not None:
            self.head.prev = newnode
        self.head = newnode

    def printval(self,node):
        while node is not None:
            print(node.data)
            node = node.next

    def append(self,newval):
        newnode = Node(newval)
        newnode.next = None
        if self.head is None:
            newnode.prev = None
            self.head = newnode
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = newnode
        newnode.prev = last

    def insert(self,prev_node,newval):
        if prev_node is None:
            return
        newnode = Node(newval)
        newnode.next = prev_node.next
        prev_node.next = newnode
        newnode.prev = prev_node
        if newnode.next is not None:
            newnode.next.prev = newnode

list = Doubly()
list.push(10)
list.push(20)
list.append(40)
list.push(30)
list.insert(list.head.next,50)
list.printval(list.head)
