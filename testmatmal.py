
# 1. read mt A from 'A.csv'
#import pandas as pd
#import csv

A = readm('A.csv')

b = readm('b.csv')



C= matmul(A,b)
print('----')
for row in C:
    print(row)
    print('----')
import numpy as numpy
D =np.dot(np.array(A),np.array(b))
print(D)

# 4.print C
