abc = input()
x, y, z = input()

abc = int(abc)
x, y, z = int(x), int(y), int(z)

print(abc * z)
print(abc * y)
print(abc * x)
print(abc * (x * 100 + y * 10 + z))
