#creating numpy arrays using Numpy functions
import numpy as np
var1=np.eye(4)
print(var1)
print(var1.ndim)

#max and min
import numpy as np
x=np.array([1,5,3,7,9,10,20,1,0,46,99])
print(np.min(x))
print(np.max(x))

#OUTPUT1
[[1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 1. 0.]
 [0. 0. 0. 1.]]
2

#OUTPUT2
0
99
