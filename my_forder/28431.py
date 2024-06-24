list = []

for i in range(5):
    n = int(input())
    if n in list:
        list.remove(n)
    else:
        list.append(n)

print(list[0])
