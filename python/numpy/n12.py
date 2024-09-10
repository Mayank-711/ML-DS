import numpy as np
a = np.linspace(1,10,10,dtype=int)
print(a)
a[(a>=3) & (a<=8)]= -a[(a >= 3) & (a <= 8)]
print(a)