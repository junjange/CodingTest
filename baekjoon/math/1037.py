import sys

n = int(sys.stdin.readline())
m = list(map(int, sys.stdin.readline().split()))

# 약수중에서 제일 작은 수와 제일 큰 수를 곱하면 어떤 수를 나눴는지 알 수 있다.
res = max(m) * min(m)
print(res)
