# Author: Ryan (AMDG) 11/2/21

import time
import math

t0 = time.perf_counter
t1 = time.perf_counter

t0 = math.pow(2, 2)
t1 = 2 ** 2

print(time.process_time(t0))
print(time.process_time(t1))
