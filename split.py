import numpy as np
var=np.array([1,2,3,4,5,6,7,8])
x=np.array_split(var,3)
print(x)

#OUTPUT
[array([1, 2, 3]), array([4, 5, 6]), array([7, 8])]
