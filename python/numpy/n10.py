import numpy as np
a = np.linspace(1,10,10,dtype=int)
a[a%2!=0]= -1
print(a)