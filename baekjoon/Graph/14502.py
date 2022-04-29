import sys
from collections import deque
import copy


# 백 트래킹
def back_tracking(cnt):
    global answer
    
    # 벽을 3개 세웠다면 
    if cnt == 3:
        answer = max(answer, bfs())
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                back_tracking(cnt + 1) # 백 트래킹
                graph[i][j] = 0


# bfs 탐색
def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    tmp_graph = copy.deepcopy(graph) # graph 복사
    
    queue = deque()
    for i in range(n):
        for j in range(m):
            if tmp_graph[i][j] == 2: # 바이러스 위치 확인
                queue.append((i, j))
    
    while queue:
        x, y = queue.pop()
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < m and tmp_graph[nx][ny] == 0:
                tmp_graph[nx][ny] = 2
                queue.append([nx, ny])
    
    # 안전한 위치 확인
    safe_zone = 0
    for c in range(n):
        safe_zone += tmp_graph[c].count(0)

    return safe_zone


n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = 0
back_tracking(0)
print(answer)
