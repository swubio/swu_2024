A, B, C = input().split()
A, B, C = int(A), int(B), int(C)
print((int(A) + int(B)) % int(C))  # int를 따로따로 쓰지 않는 방법.
print(((A % C) + (B % C)) % C)
print((A * B) % C)
print(((A % C) * (B % C)) % C)
