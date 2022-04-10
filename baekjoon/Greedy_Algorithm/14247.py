import sys

n = int(sys.stdin.readline())
answer = sum(list(map(int, sys.stdin.readline().split())))
a = sorted(list(map(int, sys.stdin.readline().split())))
for i in range(n):
    answer += a[i] * i
print(answer)
