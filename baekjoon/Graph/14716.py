import sys
sys.setrecursionlimit(10 ** 6)  # 재귀 허용 깊이를 수동으로 늘려주는 코드


# dfs 탐색
def dfs(x, y):

    if x <= -1 or x >= m or y <= -1 or y >= n:
        return False

    # 탐색하지 않았다면 탐색
    if graph[x][y] == 1:

        # 탐색 확인
        graph[x][y] = 0

        # 상/하/좌/우/대각선을 재귀적으로 탐색
        dfs(x + 1, y) # 오른쪽
        dfs(x + 1, y + 1) # 오른쪽 위 대각선
        dfs(x + 1, y - 1) # 오른쪽 아래 대각선
        dfs(x - 1, y) # 왼쪽
        dfs(x - 1, y + 1) # 왼쪽 위 대각선
        dfs(x - 1, y - 1) # 왼쪽 아래 대각선
        dfs(x, y + 1) # 위
        dfs(x, y - 1) # 아래

        return True
    return False


m, n = map(int, sys.stdin.readline().split())

# 2차원 리스트를 표현
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

# 글자 개수 체크
cnt = 0

for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            dfs(i, j)

            # 글자 개수 카운트
            cnt += 1

print(cnt)

