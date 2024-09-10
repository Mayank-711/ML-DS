import numpy as np
a = [1,2,3,4,5]
np_arr = np.array(a,dtype=float)
b =[1,2,3]
b_narray = np.array(b,dtype=int)
b_narray = b_narray.fill(2)
b_ones = np.ones(4)
b_zeros = np.zeros(5)
b_full = np.full(5,10)
b_empty = np.empty([2,2],dtype=int)
print(np_arr,b_narray,b_ones,b_zeros,b_full,b_empty)