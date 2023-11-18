student = [_ for _ in range(1, 31)]
number = []
for _ in range(28):
    n = int(input())
    number.append(n)
L = [*(set(student) - set(number))]
print(f'{min(L)}\n{max(L)}')