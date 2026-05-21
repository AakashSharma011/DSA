class Node:
    def __init__(self,info,next_node=None):
        self.data = info
        self.next = next_node

class SinglyLinkedList:
    def __init__(self,head=None):
        self.head = head

# when we want to insert a node at the end of the already crea list 
    def insertAtEnd(self,value):
        temp=Node(value)
        if(self.head!=None):
            t1=self.head
            while(t1.next!=None):
                t1=t1.next
            t1.next=temp
        else:
            self.head=temp

    # when we want to insert a node at the beginning of the already crea list
    def insertAtBeg(self,value):
        temp=Node(value)
        temp.next=self.head
        self.head=temp

    # when we want to insert a node at the given position of the already crea list
    def insertAtPos(self,value,x):
        if self.head is None:
            print("List is empty")
            return
        t1=self.head
        while t1 is not None:
            if t1.data == x:
                temp = Node(value)
                temp.next = t1.next
                t1.next = temp
                return
            t1 = t1.next
        print("Value not found in list")

# when we want to delete a node at the given position of the already crea list
    def deleteAtPos(self,value):
        t1=self.head
        prev=t1
        if(t1.data==value):
            self.head=t1.next
        while(t1.next!=None):
            if(t1.data==value):
                prev.next=t1.next
                break
            else:
                prev=t1
                t1=t1.next
            if(t1.data==value):
                prev.next=None

            
    #For printing the list
    def printLL(self):
        t1=self.head
        while(t1.next!=None):
            print(t1.data)
            t1=t1.next
        print(t1.data)


obj=SinglyLinkedList()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtBeg(5)
obj.insertAtPos(15,10)
obj.deleteAtPos(20)
obj.printLL()