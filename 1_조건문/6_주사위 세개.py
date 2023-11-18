X, Y, Z = map(int, input().split())
if X == Y == Z:
    print(10000 + X * 1000)
elif X == Y or X == Z or Y == Z:
    if X == Y or X == Z:
        print(1000 + X * 100)
    else:
        print(1000 + Y * 100)
else:
    print(max(X, Y, Z) * 100)