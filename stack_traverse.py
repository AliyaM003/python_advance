def traverse_stack(stack):
    if not stack:
        return
    element=stack.pop()
    print("item poped")
    traverse_stack(stack)
    print(element)
stack=[1,2,3,4,5]
print("stack element:")
traverse_stack(stack)

#OUTPUT
stack element:
item poped
item poped
item poped
item poped
item poped
1
2
3
4
5
