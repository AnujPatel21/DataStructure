class node:
    def __init__(self, data):
        self.data = data
        self.nextval = None

class Linklist:
    def __init__(self):
        self.headval = None

    def printlist(self):
        printval = self.headval
        while printval is not None:
            print(printval.data)
            printval = printval.nextval

    def AtBegin(self,newdata):
        newnode = node(newdata)
        newnode.nextval = self.headval
        self.headval = newnode

    def AtEnd(self,newdata):
        newnode = node(newdata)
        if self.headval is None:
            self.headval = newnode
            return
        lastval = self.headval
        while (lastval.nextval):
            lastval = lastval.nextval
        lastval.nextval = newnode

    def InBet(self,middle,newdata):
        newnode = node(newdata)
        if middle is None:
            print("Value does not exist")
            return
        newnode.nextval = middle.nextval
        middle.nextval = newnode

    def RemoveNode(self, Removekey):
        HeadVal = self.headval

        if (HeadVal is not None):
            if (HeadVal.data == Removekey):
                self.headval = HeadVal.nextval
                HeadVal = None
                return

        while (HeadVal is not None):
            if HeadVal.data == Removekey:
                break
            prev = HeadVal
            HeadVal = HeadVal.nextval

        if (HeadVal == None):
            return

        prev.nextval = HeadVal.nextval

        HeadVal = None


list1 = Linklist()
list1.headval = node("Mon")
e2 = node("Tue")
e3 = node("Wed")
list1.headval.nextval = e2
e2.nextval = e3
list1.AtBegin("Sun")
list1.AtEnd("Thur")
list1.InBet("list1.headval.nextval.nextval","Sat")
list1.printlist()
list1.RemoveNode("Sat")
print()
list1.printlist()
