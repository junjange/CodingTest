import sys
from collections import deque


# bfs 탐색
def bfs():

    # 나이트가 갈 수 있는 8가지 방향 표현
    dx = [1, -1, -2, 2, -2, 2, 1, -1]
    dy = [-2, -2, -1, -1, 1, 1, 2, 2]

    # 시작점부터 탐색
    queue = deque([[stat_x, start_y]])

    while queue:

        x, y = queue.popleft()

        # 이동하려고 하는 칸에 도착했으면
        # 현재 칸까지 이동한 횟수 리턴
        if x == end_x and y == end_y:
            return graph[x][y]

        # 나이트가 갈 수 있는 방향 탐색
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 범위 내에 있고 탐색하지 않았다면 탐색
            if 0 <= nx < n and 0 <= ny < n:
                if not graph[nx][ny]:
                    queue.append([nx, ny])
                    graph[nx][ny] = graph[x][y] + 1 # 이동 횟수 초기화


t = int(sys.stdin.readline())

# 테스트 케이스만큼 반복
for _ in range(t):
    n = int(sys.stdin.readline())
    graph = [[0 for _ in range(n)] for _ in range(n)] # 이동하기까지 걸린 횟수
    stat_x, start_y = map(int, sys.stdin.readline().split())
    end_x, end_y = map(int, sys.stdin.readline().split())
    print(bfs())
