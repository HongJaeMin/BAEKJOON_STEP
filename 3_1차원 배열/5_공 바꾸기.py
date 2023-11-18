import sys

N, M = map(int, sys.stdin.readline().split())
L = [a for a in range(1, N+1)]
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    if 1 <= i <= j <= N:
        pass
    else:
        raise ValueError('i, j 다시 입력')
    L[i-1], L[j-1] = L[j-1], L[i-1]
for l in L:
    print(l, end=' ')