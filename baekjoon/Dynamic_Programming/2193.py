import sys

n = int(sys.stdin.readline())
dp = [0] * 91
dp[1] = 1 # 자릿수가 1일 때, 이친수의 개수 : 1
dp[2] = 1 # 자릿수가 2일 때, 이친수의 개수 : 1

# 피보나치 수 문제를 수행하듯 점화식을 구해 문제를 수행한다.
# 점화식 : (n > 2), f(n) = f(n - 2) + f(n - 1)
for i in range(2, n + 1):
    dp[i] = dp[i - 2] + dp[i - 1]

print(dp[n])
