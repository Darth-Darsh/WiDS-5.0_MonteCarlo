import numpy as np
import math
import random

N = 1000000
inside = 0

for i in range(N):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    d = np.sqrt(x**2 + y**2)
    if d <= 1:
        inside += 1

pi = (inside / N) * 4
print(f"Estimated value of Pi: {pi}")