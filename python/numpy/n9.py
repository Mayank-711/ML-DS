import numpy as np
a = np.arange(1,20,2,dtype=int)
print(a)
b = np.where(a%3==0)
print(a[b])