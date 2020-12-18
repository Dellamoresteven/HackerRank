#!/bin/python3

import math
import os
import random
import re
import sys

def insertionSort(arr):
    n = len(arr)
    a,b = arr[:n//2], arr[n//2:]
    print(a,b)
    count = 0
    count += count_inversions(a)
    count += count_inversions(b)
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] > b[j]:
                print("first: ", a[i], b[j])
                count += 1
    return count


def count_inversions(l):
    n = 0
    for i,x in enumerate(l):
        for j in range(i+1, len(l)):
            if x > l[j]:
                n += 1
    return n

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = insertionSort(arr)

        fptr.write(str(result) + '\n')

    fptr.close()

