class Stack:
    def __init__(self):
        self.s=[]
    def length(self):
        return len(self.s)
    
    # We can use Append or Insert to add element in stack
    #Append is O(1) and Insert is O(n) appends add at the end of the list and insert adds at the beginning of the list (Reverse order)
    def push(self,value):
        self.s.insert(0,value)
    
    def peek(self):
        if len(self.s)==0:
            raise Exception("Stack is empty")
        else:
            return self.s[0]
        
    def pop(self):
        if len(self.s)==0:
            raise Exception("Stack is empty")
        else:
            return self.s.pop(0) # zero index is the top of the stack because we are inserting at the beginning of the list
        

stk=Stack()
stk.push(10)
stk.push(20)
stk.push(30)
print(stk.peek()) # 30
print(stk.pop()) # 30
print(stk.pop()) # 20
print(stk.peek()) # 10
