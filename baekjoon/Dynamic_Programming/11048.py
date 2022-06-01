import sys

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

# 반복문을 통해 미로를 확인
for i in range(n):
    for j in range(m):
        # 현재 좌표에 올 수 있는 모든 경우의 수의 최댓값과 현재 좌표에 사탕 수를 더한다.
        dp[i][j] = max(dp[i][j], dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + graph[i][j]

print(dp[n-1][m-1])
