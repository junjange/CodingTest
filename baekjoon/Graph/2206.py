import sys
from collections import deque


# bfs 탐색
def bfs():
    queue = deque([[0, 0, 0]])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visited[0][0][0] = 1 # 첫 번째칸에 벽을 부실 수 있는 상태에 칸의 이동 횟수

    while queue:
        x, y, z = queue.popleft()

        # (n, m)의 위치까지 이동했다면 리턴
        if x == n - 1 and y == m - 1:
            return visited[x][y][z]

        # 상/하/좌/우 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 내에 있으면
            if 0 <= nx < n and 0 <= ny < m:
                # 벽을 만나고 벽을 부실 수 있는 상태라면
                if graph[nx][ny] == 1 and z == 0:
                    visited[nx][ny][z + 1] = visited[x][y][z] + 1
                    queue.append([nx, ny, z + 1])

                # 이동할 수 있는 곳이고 현재 상태로 처음 이동 하는 곳이라면
                elif graph[nx][ny] == 0 and visited[nx][ny][z] == 0:
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    queue.append([nx, ny, z])

    # (n, m)의 위치까지 이동을 못했다면 -1 리턴
    return -1


n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().strip())) for i in range(n)]
# 3차원 배열
# x == 행
# y == 열
# z == 벽을 부실 수 있는지에 대한 상태(부실 수 있다 : 0, 부실 수 없다: 1)
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

print(bfs())
