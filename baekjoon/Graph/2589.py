# pypy3 통과.. python3 시간초과..

import sys
from collections import deque


def bfs(a, b):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque([[a, b]])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < l and 0 <= ny < w:
                if not visited[nx][ny] and graph[nx][ny] == "L":
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append([nx, ny])

    temp = 0
    for k in range(l):
        temp = max(temp, max(visited[k]))

    return temp


l, w = map(int, sys.stdin.readline().split())
graph = [list(map(str, sys.stdin.readline().strip())) for _ in range(l)]

answer = []
for i in range(l):
    for j in range(w):
        if graph[i][j] == "L":
            visited = [[0 for _ in range(w)] for _ in range(l)]
            visited[i][j] = 1
            answer.append(bfs(i, j))

print(max(answer) - 1)
