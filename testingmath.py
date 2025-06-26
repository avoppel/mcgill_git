# very cool python script

import numpy as np
import math

num = int(input("Enter a number: "))
arr = np.zeros(num)

for i in range(num):
	arr[i] = math.sqrt(i)