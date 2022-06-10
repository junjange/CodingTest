import sys


n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[[0] * n for _ in range(n)] for _ in range(3)]
dp[0][0][1] = 1 # 파이프의 초기 위치

# 반복문을 통해 처음에 가로로 갈 수 있는 곳에 파이프를 이동
for i in range(2, n):
    if graph[0][i] == 0:
        dp[0][0][i] = dp[0][0][i - 1]

# 반복문을 통해 파이프 이동
for i in range(1, n):
    for j in range(2, n):
        
        # 파이프가 대각선으로 이동 가능한 경우
        if graph[i][j] == 0 and graph[i - 1][j] == 0 and graph[i][j - 1] == 0:
            dp[2][i][j] = sum(dp[k][i - 1][j - 1] for k in range(3)) 
        
        # 파이프가 가로/세로로 이동 가능한 경우
        if graph[i][j] == 0:
            dp[0][i][j] = dp[0][i][j - 1] + dp[2][i][j - 1]
            dp[1][i][j] = dp[1][i - 1][j] + dp[2][i - 1][j]

# 3가지 방향으로 파이프가 이동해 온 경우의 합을 출력
print(sum(dp[k][-1][-1] for k in range(3)))
