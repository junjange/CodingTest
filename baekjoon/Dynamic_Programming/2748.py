import sys


n = int(sys.stdin.readline())
dp = [0] * (n + 1)

dp[0] = 0 # 0번째 피보나치 수 : 0
dp[1] = 1 # 1번째 피보나치 수 : 1

# 반복문을 통해 n번째 피보나치 수를 구한다.
for i in range(2, n + 1):
    dp[i] = dp[i - 2] + dp[i - 1]

print(dp[n])
