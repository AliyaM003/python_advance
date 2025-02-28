from queue import LifoQueue
stack=LifoQueue()
stack.put(10)
stack.put(20)
stack.put(30)
stack.put(40)
stack.put(50)
print("top element:",stack.queue[-1])
print("popped element:",stack.get())
print("popped element:",stack.get())
print("stack size:",stack.qsize())

#OUTPUT
top element: 50
popped element: 50
popped element: 40
stack size: 3
