animals1 = {"dog", "cat", "elephant"}
animals2 = {"lion", "tiger", "cheetah"}

print("animals1:", animals1)
print("animals2:", animals2)

animals1.update({"cow"})  
animals2.update({"kangaroo"})
print("Updated animals1:", animals1)
print("Updated animals2:", animals2)

#OUTPUT
animals1: {'cat', 'elephant', 'dog'}
animals2: {'cheetah', 'lion', 'tiger'}
Updated animals1: {'cat', 'cow', 'elephant', 'dog'}      
Updated animals2: {'cheetah', 'lion', 'kangaroo', 'tiger'}
