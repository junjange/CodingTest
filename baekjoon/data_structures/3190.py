import sys
from collections import deque


def change(D, C):
    # 상(0) 우(1) 하(2) 좌(3)
    # 동쪽 회전: 상(0) -> 우(1) -> 하(2) -> 좌(3) -> 상(0) : +1 방향
    # 왼쪽 회전: 상(0) -> 좌(3) -> 하(2) -> 우(1) -> 상(0) : -1 방향
    if C == "L":
        D = (D - 1) % 4
    else:
        D = (D + 1) % 4
    return D


# bfs 탐색
def bfs():
    dy = [0, 1, 0, -1]
    dx = [-1, 0, 1, 0]
    x = 0
    y = 0
    queue = deque([[x, y]])
    time = 1 # 시간
    vector = 1 # 방향을 잡기 위해
    graph[x][y] = 2 # 현재 위치 탐색
    while queue:
        x += dx[vector]
        y += dy[vector]

        # 범위 내에 있고 몸에 부딪히지 않은 경우
        if 0 <= x < n and 0 <= y < n and graph[x][y] != 2:
            # 이동한 칸에 사과가 없으면 현재 위치의 꼬리를 제거하여 앞으로 이동시켜준다.
            if not graph[x][y] == 1:
                a, b = queue.popleft()
                graph[a][b] = 0

            # 앞으로 이동
            graph[x][y] = 2

            # 다음 탐색할 좌표를 큐에 추가한다.
            queue.append([x, y])

            # 현재 시간이 지난 후 방향 전환을 해야하는지 확인
            if time in vt.keys():
                # 방향 전환 함수를 통해 방향 전환
                vector = change(vector, vt[time])
            
            # 카운트
            time += 1

        # 범위를 벗어나거나 몸에 부딪힌 경우
        else:
            return time


n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
graph = [[0] * n for _ in range(n)] # 2차원 그래프로 표현

# 사과의 개수만큼 반복하여 사과의 위치를 찾는다.
for _ in range(k):
    x, c = map(int, sys.stdin.readline().split())
    graph[x - 1][c - 1] = 1 # 사과 저장

# 딕셔너리형으로 뱀의 방향 변환 정보를 받는다.
l = int(sys.stdin.readline())
vt = {}
for _ in range(l):
    x, c = map(str, sys.stdin.readline().split())
    vt[int(x)] = c

print(bfs())
