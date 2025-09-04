#!/bin/python3

import math
import os
import random
import re
import sys



def simpleArraySum(ar):
    total = 0
    for i in ar:
      total += i
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))#rstrip() sağdaki boşlukları ve yeni satır karakterlerini siler
                                                #input().rstrip().split(): split() stringi boşluklara göre böler ve liste yapar.. map(int, ...)
                                                #map() listenin her elemanına int() fonksiyonunu uygularString'leri tam sayılara çevirir

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()