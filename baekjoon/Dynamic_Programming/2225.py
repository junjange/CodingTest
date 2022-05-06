import sys

n, k = map(int, sys.stdin.readline().split())
dp = [[0] * 201 for _ in range(201)]

# 점화식 : dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

# 초기 세팅
for x in range(201):
    # 1개 수로 x를 만드는 경우의 수
    dp[1][x] = 1 # 자기 자신뿐

    # 2개의 수로 x를 만드는 경우의 수
    dp[2][x] = x + 1


# 반복문을 통해 점화식 수행
for i in range(2, 201):
    # i개로 1을 만드는 경우의 수 i개
    dp[i][1] = i

    for j in range(2, 201):
        dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % 1000000000


print(dp[k][n])
