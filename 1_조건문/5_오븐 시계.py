A, B = map(int, input().split())
C = int(input())
B += C
if B >= 60:
    A = (A + B // 60) % 24
    B %= 60
print(A, B)