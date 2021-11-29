import sys

n = int(sys.stdin.readline())
dp = [0] * 1001
dp[1] = 1
dp[2] = 3

# 반복문을 통해 점화식을 코드로 수행
# n = 1일때 1가지, n = 2일때 3가지, n = 3일때 5가지, n = 4일때 11가지
# f(n) = (f(n - 2) * 2) + f(n - 1)
for i in range(3, n + 1):
    dp[i] = (dp[i - 2] * 2) + dp[i - 1]
print(dp[n] % 10007)
