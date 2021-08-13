import sys
from collections import deque # deque를 통해 시간복잡도를 줄였다.


def bfs(day):

    # 큐에 탐색해야 하는 노드 없을 때까지 실행
    while queue:

        day += 1  # 일수 증가

        # 큐에 있는 노드 수만큼 탐색
        for _ in range(len(queue)):

            a, b, c = queue.popleft()  # 큐에 있는(탐색해야 하는) 노드의 좌표

            # 6방향 확인
            for i in range(6):
                x = a + dx[i]
                y = b + dy[i]
                z = c + dz[i]

                # 아직 방문하지 않은 미로중에 토마토가 있는 경우
                if -1 < x < n and -1 < y < m and -1 < z < h and graph[z][x][y] == 0:

                    # 방문처리
                    graph[z][x][y] = 1

                    # 탐색할 곳을 추가
                    queue.append([x, y, z])

    for z in range(h):
        for x in range(n):
            for y in range(m):
                if graph[z][x][y] == 0:
                    return -1

    # 모두 익은 경우 일수 출력
    return day - 1


m, n, h = map(int, sys.stdin.readline().split())

# 3차원 미로
graph = [[list(map(int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]


# 좌/우/위/아래 방향 이동
dx = [0, 0, -1, 1, 0, 0]
dy = [-1, 1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

# 익은 토마토 확인
queue = deque([])
for z in range(h):
    for x in range(n):
        for y in range(m):
            if graph[z][x][y] == 1:
                queue.append([x, y, z])

print(bfs(0))


