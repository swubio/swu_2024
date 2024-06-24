A = int(input())

for i in range(A):
    p = "*" * (A - i)
    print(p.rjust(A))
