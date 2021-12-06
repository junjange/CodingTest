import sys

k = int(sys.stdin.readline())
dp = [[0 for _ in range(2)] for _ in range(46)]
dp[1][0] = 0 
dp[1][1] = 1

# A : 이전 화면에 B의 개수
# B : 이전 화면에 A와 B의 개수
# f(a) = f(b - 1)
# f(b) = f(a - 1) + f(b - 1)
# 반복문을 통해 점화식을 수행
for i in range(2, k + 1):
    dp[i][0] = dp[i - 1][1]
    dp[i][1] = dp[i - 1][0] + dp[i - 1][1]

print(dp[k][0], dp[k][1])
