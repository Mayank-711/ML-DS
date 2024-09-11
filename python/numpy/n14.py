import numpy as np
a = np.array([[21,20,19,18,17],[16,15,14,13,12],[11,10,9,8,7],[6,5,4,3,2]])
sort = a[:,1].argsort()
a = a[sort]
print(a)