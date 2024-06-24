N = int(input())
data = input().split()
o = 0

for i in range(N):
    data_i = data[i]
    if data_i == "O":
        C = o + (1 * (i + 1))
    elif data_i == "X":
        P = C + 0
        print(C)

# 흠냠냠 머르겟네정말
