import numpy as np
a = np.random.randint(1,30,10,dtype=int)
b = a.argmax()
a[b]=0
print(a)