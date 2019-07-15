
# 1. read mt A from 'A.csv'
#import pandas as pd
#import csv
from matmul import readm, matmul
#1.read matrix A from
A = 'A.csv'

#2.read matrix b from 'b.csv'
b = 'b.csv'

print(matmul(readm(A),readm(b)))