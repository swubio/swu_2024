A = int(input())
R, S = input().split()
R = int(R)
S = str(S)
# S_list = len(str(S))

for i in range(len(S)):
    print(R * S[i], end="")
# print(str(S)[R] * int(R))
