#!/usr/bin/env python3
import time
for i in range(200):
    print("0"*(3-len(str(i))),i,sep='')
    time.sleep(0.02)
    print('\u000c')
