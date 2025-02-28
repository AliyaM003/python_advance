import numpy as np
var3=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(var3)
print(var3.ndim)

x1=var3.reshape(2,3,2)
print(x1)
print(x1.ndim)
var=x1.reshape(-1)
print(var)
print(var.ndim)

#Iterating numpy arrays....
import numpy as np
var1=np.array([[[1,2,3,4],[1,2,3,4]]])
for k in var1:
    for n in k:
        for m in n:
            print(m)

# COPY FUNCTION HAS ITS NEW ARRAY  
#VIIEW FUNCTION HAS IT ORIGINAL ARRAY

import numpy as np
var=np.array([1,2,3,4])
var1=var.copy()
var[1]=40
print(var)
print(var1)






#OUTPUT1
[ 1  2  3  4  5  6  7  8  9 10 11 12]
1
[[[ 1  2]
  [ 3  4]
  [ 5  6]]

 [[ 7  8]
  [ 9 10]
  [11 12]]]
3
[ 1  2  3  4  5  6  7  8  9 10 11 12]
#OUTPUT2
1
1
2
3
4
1
2
3
4
#OUTPUT3
[ 1 40  3  4]
[1 2 3 4]
#OUTPUT4
[ 1 40  3  4]
[ 1 40  3  4]
