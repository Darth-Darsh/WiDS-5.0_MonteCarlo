import numpy as np
import math
import random
import matplotlib.pyplot as plt

def e_estimate(N):
    x = np.random.uniform(1, 2, int(N))
    y = np.random.uniform(0, 1, int(N))
    inside_mask = y <= 1/x
    count = np.sum(inside_mask)
    area = count / N
    e = 2**(1/area)
    return e

e = e_estimate(1000000)

print(f"Estimated value of e: {e}")

percent_error = abs((e - math.e) / math.e) * 100
print(f"Percent error: {percent_error}%")