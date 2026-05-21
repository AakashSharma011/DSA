class Deque:
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return len(self.items)==0
    
    def insertAtLast(self,value):
        self.items.append(value)

    def insertAtFront(self,value):
        self.items.insert(0,value)
    
    def deleteAtFront(self):
        if(self.isEmpty()):
            print("Deque us empty")
        else:
            return self.items.pop(0)

    def deleteAtEnd(self):
        if(self.isEmpty()):
            print("Deque is empty")
        else:
            return self.items.pop()

de=Deque()
de.insertAtLast(10)
de.insertAtLast(20)
de.insertAtFront(5)
print(de.deleteAtFront())
print(de.deleteAtEnd())
