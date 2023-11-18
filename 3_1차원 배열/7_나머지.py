L = []
for _ in range(10):
    A = int(input())
    L.append(A % 42)
L2 = list(set(L))
print(len(L2))