#!/usr/bin/python3

import decimal
from timeit import default_timer as timer
import math

start_time = timer()
for i in range(100000):
    u = math.sqrt(i * i)
print(timer() - start_time)

start_time = timer()
for i in range(100000):
    u = (i * i) ** .5
print(timer() - start_time)

start_time = timer()
for i in range(100000):
    u = pow(i * i, .5)
print(timer() - start_time)

decimal.getcontext().prec = 2
summ = 0
start_time = timer()
for i in range(1000000):
    summ += decimal.Decimal('0.11') + decimal.Decimal('0.1') + decimal.Decimal('0.1') - decimal.Decimal('0.3')
print(timer() - start_time,"\t", summ)

summ = 0
start_time = timer()
for i in range(1000000):
    summ += 0.1 + 0.1 + 0.1 - 0.3
print(timer() - start_time,"\t", summ)