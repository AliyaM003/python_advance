class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)
    def pop(self):
        if self.stack:
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            return self.stack.pop()
        return "Stack is empty"
    def get_min(self):
        return self.min_stack[-1] if self.min_stack else "Stack is empty"


ms = MinStack()
ms.push(3)
ms.push(1)
ms.push(9)
print(ms.get_min())  
ms.pop()
print(ms.get_min())  

#OUTPUT
1
1

