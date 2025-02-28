l1 = ((2), 1, 9, 15, 21)
print("l1:", l1)

def findgreaterelements(lst):  
    first_element = lst[0] 
    greater_elements = [x for x in lst if x > first_element] 
    return greater_elements

result = findgreaterelements(l1)  
print("Greater elements:", result)  

#OUTPUT
l1: (2, 1, 9, 15, 21)
Greater elements: [9, 15, 21]
