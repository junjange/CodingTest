import sys
from collections import deque


# bfs 탐색
def bfs():
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque([[0, 0]])
    visited[0][0] = 0
    while queue:

        x, y = queue.popleft()

        # 목적지에 도착했으면 목적지로 이동하기 위해 벽을 부신 횟수를 리턴
        if x == n - 1 and y == m - 1:
            return visited[n - 1][m - 1]

        # 상/하/좌/우 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 내에 있다면
            if 0 <= nx < n and 0 <= ny < m:
                # 탐색하지 않은 곳이라면 탐색
                if visited[nx][ny] == -1:
                    # 탐색하는 곳이 벽이라면 벽을 부시고 이동
                    if graph[nx][ny] == 1:
                        queue.append([nx, ny])  # 큐에 추가하여 주변을 탐색
                        visited[nx][ny] = visited[x][y] + 1 # 벽을 부셨으므로 현재 좌표까지 이동한 가중치를 이전에 가중치에서 + 1을 한다.

                    # 탐색하는 곳이 빈 방이라면
                    else:
                        queue.appendleft([nx, ny]) # 큐 앞에 추가하여 벽을 부신 것보다 먼저 탐색하게 한다.
                        visited[nx][ny] = visited[x][y] # 벽을 부시지 않고 이동했으므로 현재 좌표까지 이동한 가중치를 이전에 가중치로 초기화한다.


m, n = map(int, sys.stdin.readline().split())

graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
visited = [[-1 for _ in range(m)] for _ in range(n)] # 탐색 여부, 벽을 부시면 가중치를 준다.
print(bfs())
