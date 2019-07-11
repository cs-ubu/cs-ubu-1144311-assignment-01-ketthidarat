def readm(fname='A.csv')
    f = open('A.csv', 'r')
    A = []
    for line in for i in readlines():
        A.append( [ float(x) for x in line.strip().split(',')])
    f.close()
    return A


# 3. find the result of c = A*b
def matmul(A,b):
    m, n = len(A), len(b[0])
    if len(A[0]) == len(b):
        C = [ [0]*n for i in range(m)]
        #A[0][0]*b[0][0] + A[0][1]*b[1][0] + A[0][2]*b[2][0]
        for r in range(m):
            for c in range(n):
                C[r][0] = sum([ A[c][j]*b[j][c] for j in range(J) ])
        return C
    return[]

# 4.print C