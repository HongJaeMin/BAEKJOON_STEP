import sys

N, M = map(int, sys.stdin.readline().split())
L = [0 for _ in range(N)]
for _ in range(M): 
    i, j, k = map(int, sys.stdin.readline().split())
    if 1 <= i <= j <= N and 1 <= k <= N:
        pass
    else:
        raise ValueError('i, j, k값 다시 입력')
    for place in range(i-1, j):
        L[place] = k
for val in L:
    print(val, end=' ')