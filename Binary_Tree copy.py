from Queue import *
class Node:

    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else :
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else :
                    self.right.insert(data)
        else :
            self.data = data

    def printtree(self):
        if self.left:
            self.left.printtree()
        print(self.data)
        if self.right:
            self.right.printtree()

    def findvalue(self,data):
        if data < self.data:
            if self.left is None:
                print("Not Found")
                return
            return self.left.findvalue(data)
        elif data > self.data:
            if self.right is None:
                print("Not Found")
                return
            return self.right.findvalue(data)
        else :
            print("Data Found")
            return

    def preordertraversal(self,root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.preordertraversal(root.left)
            res = res + self.preordertraversal(root.right)
        return res

    def inordertraversal(self,root):
        res = []
        if root:
            res = res + self.inordertraversal(root.left)
            res.append(root.data)
            res = res + self.inordertraversal(root.right)
        return res

    def postordertraversal(self,root):
        res = []
        if root:
            res = res + self.postordertraversal(root.left)
            res = res + self.postordertraversal(root.right)
            res.append(root.data)
        return res

    def bfs(self):
        q = Queue()
        q.put(self)
        while not q.empty():
            current_node = q.get()
            print(current_node.data)
            if current_node.left:
                q.put(current_node.left)
            if current_node.right:
                q.put(current_node.right)

    def removenode(self,data):
        if data < self.data:
            if self.left is None:
                print("Not Found")
                return
            return self.left.findvalue(data)
        elif data > self.data:
            if self.right is None:
                print("Not Found")
                return
            return self.right.findvalue(data)
        else :
            self.clearnode()
            return

    def clearnode(self):
        self.data = None
        self.left = None
        self.right = None

root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
root.printtree()
root.findvalue(14)
print(root.preordertraversal(root))
print(root.inordertraversal(root))
print(root.postordertraversal(root))
root.bfs()
root.removenode(42)
root.printtree()
