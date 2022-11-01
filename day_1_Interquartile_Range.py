#!/bin/python3

import math
import os
import random
import re
import sys
import statistics

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#

def interQuartile(values, freqs):
  # Print your answer to 1 decimal place within this function
    s=list()
    len_s=len(values)
    for i in range(len_s):
        s+=[values[i]]*freqs[i]
    s.sort()
    middle=sum(freqs)//2
    if middle%2==0:
        Low=s[:middle]
        Upper=s[middle:]
    else:
        Low=s[:middle-1]
        Upper=s[middle+1:]
    Q1= statistics.median(Low)
    Q3= statistics.median(Upper)
    print(round((Q3-Q1),1))
if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)

#   Using Numpy and Statistics
# from statistics import median
# from numpy import repeat

# def interQuartile(values, freqs):
#     m = repeat(values,freqs)
#     m.sort()
#     lm = round(len(m)/2)
#      # Print your answer to 1 decimal place within this function
#     print(round(median(m[-lm+1:])-median(m[:lm]),1))


#Longer Version
#CODE 2
# def quartiles(arr, level):
#     arr = sorted(arr) if level==0 else arr
#     odd = True if len(arr)%2!=0 else False
#     idx_q2 = ((len(arr)+1)/2)-1
#     res = []
#     level+=1
#     if level==2:
#         if odd:
#             return arr[int(idx_q2)]
#         else:
#             return (arr[int(idx_q2)]+arr[int(math.ceil(idx_q2))])/2
#     else:
#         if odd:
#             res.append(quartiles(arr[:int(idx_q2)], level))
#             res.append(arr[int(idx_q2)])
#             res.append(quartiles(arr[int(idx_q2+1):], level))
#         else:
#             res.append(quartiles(arr[:int(math.ceil(idx_q2))], level))
#             res.append(quartiles(arr, level))
#             res.append(quartiles(arr[int(math.ceil(idx_q2)):], level))
#     return res

# def interQuartile(values, freqs):
#     # Print your answer to 1 decimal place within this function
#     data = [d for s in [[v]*f for v,f in zip(values,freqs)] for d in s]
#     res = quartiles(data, 0)
#     print(f"{res[-1]-res[0]:.1f}")
   
