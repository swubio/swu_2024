N = input()
num = int(N)
S = 0
if "7" in N:
    S = 1

if S == 0 and num % 7 != 0:
    print(0)
elif S == 0 and num % 7 == 0:
    print(1)
elif S == 1 and num % 7 != 0:
    print(2)
elif S == 1 and num % 7 == 0:
    print(3)


# if "7" in N:
#     if N % "7":
#         print("3")
#     else:
#         print("2")
# else:
#     if N % "7":
#         print("1")
#     else:
#         print("0")
# S = 0
# if "7" in N:
#     S = 1

# if S == 0 and N % 7 != 0:
#     print(0)
# elif S == 0 and num % 7 == 0:
#     print(1)
