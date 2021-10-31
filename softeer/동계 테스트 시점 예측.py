import sys
from collections import deque


# bfs 탐색
def bfs():
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque([[0, 0]])
    visited[0][0] = 1

    while queue:
        a, b = queue.popleft()

        # 상/하/좌/우 탐색
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]

            if 0 <= x < n and 0 <= y < m:
                # 탐색하는 곳이 얼음이면 방문 여부 카운트
                if graph[x][y] == 1:
                    visited[x][y] += 1

                # 얼음이 아니고 탐색하지 않았다면 탐색
                elif visited[x][y] == 0:
                    queue.append([x, y])
                    visited[x][y] = 1

    # 한시간이 지나면 얼음을 2번 이상 방문한 곳을 녹인다.
    for i in range(n):
        for j in range(m):
            if visited[i][j] >= 2:
                graph[i][j] = 0


n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
cnt = 0

# 모든 얼음이 녹을 때까지 반복한다.
while True:
    # 모든 얼음이 녹았다면 반복을 멈춘다.
    if graph.count(graph[0]) == n:
        break

    visited = [[0] * m for _ in range(n)] # 탐색 여부
    bfs() # bfs 탐색
    cnt += 1 # 시간 카운트

# 시간을 출력
print(cnt)
