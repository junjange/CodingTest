import sys

w, n = map(int, sys.stdin.readline().split())
mp = [list(map(int, sys.stdin.readline().split())) for x in range(n)]

cnt = [0] * (n+1)

for i in range(n):
    cnt[mp[i][1]] += mp[i][0]

result = 0

for i in reversed(range(n+1)):
    if w < cnt[i]:
        result += w * i
        break
    result += i * cnt[i]
    w -= cnt[i]
print(result)


