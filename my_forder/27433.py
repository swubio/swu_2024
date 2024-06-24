N = int(input())


def fac(N):
    if N <= 1:
        return 1
    return N * fac(N - 1)


print(fac(N))


# def fac(N):
#     if N > 1:
#         for i in range(N):
#             c = N * (i + 1)
#             return c


# print(fac(N))

# for i in range(N):
#     t = int(i * N)
#     print(t)
