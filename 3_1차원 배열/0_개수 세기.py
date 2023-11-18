import sys

N = int(input())
L = list(map(int, sys.stdin.readline().split()))
if len(L) > N:
    raise ValueError('입력한 정수의 개수가 N보다 큼')
v = int(input())
print(L.count(v))