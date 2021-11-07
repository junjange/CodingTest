import sys
sys.setrecursionlimit(10 ** 6)


# dfs 탐색
def dfs(x, y, c):
    visited[x][y] = True

    # 상/하/좌/우 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위 내에 있고 탐색하지 않았다면 탐색
        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny]:
                # 탐색하는 곳이 이전에 봤던 색이면 재귀적으로 탐색
                if c == graph[nx][ny]:
                    dfs(nx, ny, c)


n = int(sys.stdin.readline())

# 각 노드가 연결된 정보를 그래프로 표현
graph = [list(map(str, sys.stdin.readline().strip())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]  # 탐색 여부
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

cnt_2 = 0  # 적록색약인이 아닌 사람이 보는 그림의 구역

# 적록색약인이 아닌 사람이 보는 그림의 구역을 dfs 탐색을 통해 찾는다.
for i in range(n):
    for j in range(n):
        # 방문하지 않은 좌표이면 dfs로 넣어준다.
        if not visited[i][j]:
            dfs(i, j, graph[i][j])
            cnt_2 += 1

# G 색을 R로 변경
for i in range(n):
    for j in range(n):
        if graph[i][j] == "G":
            graph[i][j] = "R"

cnt_3 = 0  # 적록색약인이 보는 그림의 구역
visited = [[False] * n for _ in range(n)]  # 탐색 여부

# 적록색약인이 보는 그림의 구역을 dfs 탐색을 통해 찾는다.
for i in range(n):
    for j in range(n):
        # 방문하지 않은 좌표이면 dfs로 넣어준다.
        if not visited[i][j]:
            dfs(i, j, graph[i][j])
            cnt_3 += 1

print(cnt_2, cnt_3)
