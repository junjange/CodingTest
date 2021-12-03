import sys

n = int(sys.stdin.readline())
dp = [0] * 1000001

dp[1] = 1 # 1
dp[2] = 2 # 00, 11
dp[3] = 3 # 100, 001, 111,
# dp[4] = 5 # 0011, 1100, 1001, 0000, 1111
# dp[5] = 8 # 00001, 00100, 10000, 11100, 00111, 11001, 10011, 11111
# dp[6] = 13 # 000011, 001100, 110000, 100001, 100100, 001001, 001111, 110011, 111100, 111001, 100111, 111111, 000000

# 반복문을 통해 점화식을 표현
# 점화식 : f(n) = f(n - 1) + f(n - 2)
for i in range(4, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 15746

print(dp[n])
