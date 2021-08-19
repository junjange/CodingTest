import sys
from collections import deque


def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque(temp)

    while queue:

        num, a, b, cnt = queue.popleft()

        if cnt == s:
            # return graph[x - 1][y - 1] 왜 이건 안되는지 모르겠다.
            break

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
                graph[nx][ny] = num
                queue.append([num, nx, ny, cnt + 1])

    return graph[x - 1][y - 1]


n, k = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
s, x, y = map(int, sys.stdin.readline().split())
temp = []

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            temp.append([graph[i][j], i, j, 0])

temp.sort()

print(bfs())



