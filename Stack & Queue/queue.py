class Queue:
    def __init__(self):
        self.items =[] #jb bhi queue ka object banega to uske pass ek empty list hogi jisme hum apne elements ko store karenge

    def isEMpty(self):
        return len(self.items)==0 #ye function check karega ki queue empty hai ya nahi
    
    def insert(self,value):
        self.items.append(value)

    def delete(self):
        if (self.isEMpty()):
            print("Queue is empty")
        else:
            return self.items.pop(0) #ye function queue ke first element ko delete karega aur usko return karega
        

q=Queue()
q.insert(10)
q.insert(20) 
q.insert(30)
q.insert(40)

print(q.delete()) #10
print(q.delete()) #20
print(q.delete()) #30
print(q.delete()) #40
q.delete() #Queue is empty  