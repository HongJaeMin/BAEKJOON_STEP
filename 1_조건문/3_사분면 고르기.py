X = int(input())
Y = int(input())
plus_X = 0 < X <= 1000
minus_X = -1000 <= X < 0
plus_Y = 0 < Y <= 1000
minus_Y = -1000 <= Y < 0
if plus_X and plus_Y:
    print(1)
elif minus_X and plus_Y:
    print(2)
elif minus_X and minus_Y:
    print(3)
elif plus_X and minus_Y:
    print(4)