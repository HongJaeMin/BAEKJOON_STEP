X = int(input())
N = int(input())
a_list = []
b_list = []
ab_list = []
for i in range(N):
    a, b = map(int, input().split())
    a_list.append(a)
    b_list.append(b)
    ab_list.append(a_list[i] * b_list[i])
if X == sum(ab_list):
    print('Yes')
else:
    print('No')