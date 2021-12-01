import sys

n = int(sys.stdin.readline())

m = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp = [0] * (n + 1)
for i in range(n-1,-1,-1):
    if i + m[i][0] > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(m[i][1] + dp[i + m[i][0]], dp[i+1])

print(dp[0])
