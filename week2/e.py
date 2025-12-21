import numpy as np
import math
import random
import matplotlib.pyplot as plt

def e_estimate(N):
    x = np.random.uniform(0, 1, int(N))
    y = np.random.uniform(0, 3, int(N))
    inside_mask = y <= np.exp(x)
    count = np.sum(inside_mask)
    return 1 + (3 * count / N)

e = e_estimate(1000000)

print(f"Estimated value of e: {e}")

percent_error = abs((e - math.e) / math.e) * 100
print(f"Percent error: {percent_error}%")