# A = int(input())
# B = input()
# L = []
# for i in [2, 1, 0]:
#     if i == 2:
#         result = A * int(B[i])
#         L.append(result)
#         print(result)
#     elif i == 1:
#         result = A * int(B[i])
#         L.append(int(str(result)+'0'))
#         print(result)
#     else:
#         result = A * int(B[i])
#         L.append(int(str(result)+'00'))
#         print(result)
# print(sum(L))

A = int(input())
B = input()
for i in [2, 1, 0]:
    print(A * int(B[i]))
print(A * int(B))