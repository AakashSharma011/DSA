class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Insert at the beginning of the circular linked list
    def insertAtBeg(self, value):
        new_node = Node(value)
        if not self.head:
            new_node.next = new_node
            self.head = new_node
            return
        
        # Traverse to the last node
        curr = self.head
        while curr.next != self.head:
            curr = curr.next
            
        new_node.next = self.head
        curr.next = new_node
        self.head = new_node

    # Insert at the end of the circular linked list
    def insertAtEnd(self, value):
        new_node = Node(value)
        if not self.head:
            new_node.next = new_node
            self.head = new_node
            return
        
        # Traverse to the last node
        curr = self.head
        while curr.next != self.head:
            curr = curr.next
            
        curr.next = new_node
        new_node.next = self.head

    # Delete a node by its value
    def deleteNode(self, value):
        if not self.head:
            print("List is empty")
            return

        curr = self.head
        prev = None

        # Check if the node to be deleted is the head
        if curr.data == value:
            # If there's only one node in the list
            if curr.next == self.head:
                self.head = None
                return
            
            # Find the last node to update its next pointer
            last = self.head
            while last.next != self.head:
                last = last.next
            last.next = self.head.next
            self.head = self.head.next
            return

        # Search for the node to delete
        while curr.next != self.head:
            prev = curr
            curr = curr.next
            if curr.data == value:
                prev.next = curr.next
                return

        print("Value not found in the list")

    # Print the circular linked list elements
    def printLL(self):
        if not self.head:
            print("List is empty")
            return
        
        curr = self.head
        elements = []
        while True:
            elements.append(str(curr.data))
            curr = curr.next
            if curr == self.head:
                break
        print(" -> ".join(elements) + " -> (Head)")

# Demonstration
if __name__ == "__main__":
    cll = CircularLinkedList()
    print("Inserting 10, 20, 30 at end:")
    cll.insertAtEnd(10)
    cll.insertAtEnd(20)
    cll.insertAtEnd(30)
    cll.printLL()

    print("Inserting 5 at beginning:")
    cll.insertAtBeg(5)
    cll.printLL()

    print("Deleting 20:")
    cll.deleteNode(20)
    cll.printLL()

    print("Deleting 5 (Head):")
    cll.deleteNode(5)
    cll.printLL()
