class Node:
    def __init__(self,value=None):
        self.data=value
        self.prev=None
        self.next=None

class DoublyLinkedList: 
    def __init__(self):
        self.head=None
    
    def insertAtEnd(self,value):
        temp=Node(value)
        if(self.head==None):
            self.head=temp
            return
        else:
            t=self.head
            while(t.next!=None):
                t=t.next
            t.next=temp
            temp.prev=t

    def insertAtBeginning(self,value):
        temp=Node(value)
        if(self.head==None):
            self.head=temp
            return
        else:
            temp.next=self.head
            self.head.prev=temp
            self.head=temp

    def insertAtPos(self,value,x):
        t=self.head
        while(t.next!=None):
            if(t.data==x):
                break
            else:
                t=t.next
        temp=Node(value)
        temp.next=t.next
        t.next.prev=temp
        t.next=temp
        temp.prev=t

    def deleteDLL(self,value): 
        if(self.head==None):
            print("DLL is empty")
            return
        t=self.head
        if(t.data==value):
            self.head=t.next
            self.head.prev=None
            return
        while(t.next!=None):
            if(t.data==value):
                break
            else:
                t=t.next
        if(t.data==value):
            t.prev.next=t.next
            if(t.next!=None):
                t.next.prev=t.prev
        else:
            print("Value not found")

    def printLL(self):
        t=self.head
        while(t.next!=None):
            print(t.data,end = " <--> ")
            t=t.next
        print(t.data)

obj=DoublyLinkedList()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtEnd(40)
obj.insertAtBeginning(5)
obj.insertAtPos(25,20)
obj.deleteDLL(5)
obj.printLL()