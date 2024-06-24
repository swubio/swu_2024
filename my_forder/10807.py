N = int(input())

data = list(map(int, input().split()))
p = int(input())  # 왜 여기는 N과 같이 쓰면 안되는지.

print(data.count(p))
