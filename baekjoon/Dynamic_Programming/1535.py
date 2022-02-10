import sys

n = int(sys.stdin.readline())
hp = list(map(int, sys.stdin.readline().split()))
joy = list(map(int, sys.stdin.readline().split()))
dp = [[0 for _ in range(101)] for _ in range(n + 1)]

# 반복문을 통해 각 체력내에 얻을 수 있는 기쁨을 확인
for i in range(1, n + 1):
    for j in range(1, 101):
        # 현재 체력이 hp[i - 1]보다 작다면
        # 현재 기쁨을 이전 기쁨으로 초기화한다.
        if j < hp[i - 1]:
            dp[i][j] = dp[i - 1][j]

        # 현재 체력이 hp[i - 1]보다 크거나 같다면
        # 현재 기쁨을 갱신한다.
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - hp[i - 1]] + joy[i - 1])
print(dp[n][99])
