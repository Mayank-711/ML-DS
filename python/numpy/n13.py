import numpy as np
height = np.random.randint(130,170,20)
age = np.random.randint(16,22,20)
print(age[height>155],height[height>155])