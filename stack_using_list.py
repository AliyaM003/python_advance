class Stack:
    def __init__(self):
        self.Stack=[]
    def push(self,item):
          self.Stack.append(item)
    def pop(self):
        if not self.is_empty():
            return self.Stack.pop()
        return "stack is empty"
    def peek(self):
        if not self.is_empty():
            return self.Stack[-1]
        return "stack is empty"
    def is_empty(self):
         return len(self.Stack)==0
    def size(self):
        return len(self.Stack)
        
s=Stack()
s.push(10)
s.push(20)
s.push(30)
print("top element:",s.peek())
print("popped element:",s.pop())
print("Stack size",s.size())

#OUTPUT
top element: 30
popped element: 30
Stack size 2
