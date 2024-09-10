import numpy as np
a = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]])
a1 = a[2,:3]
print(a1)
a2 = a[1:4,3]
print(a2)
a3 = a[2:4,:5]
print(a3)
a4 = a[1:3,1:3]
print(a4)