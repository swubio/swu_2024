A = int(input())
B = int(input())
C = int(input())
data = map(int, list(str(A * B * C)))

for i in range(10):
    print(data.count(str(i)), end="")
# ektlgoqhl
