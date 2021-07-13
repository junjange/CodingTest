import sys

n, m = map(int, sys.stdin.readline().split())

# 2차원 미로
graph = []
for i in range(n):
    graph.append(list(sys.stdin.readline()))

# 좌/우/위/아래 방향 이동
dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]

# 0,0 부터 탐색
queue = [(0, 0)]
graph[0][0] = 1

# bfs 탐색
while queue:
    # 큐에서 원소를 팝하여 원소의 위치를 탐색
    a, b = queue.pop(0)

    # 4방향 확인
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]

        # 미로에서 이동할 수 있는 칸일 경우
        if 0 <= x < n and 0 <= y < m and graph[x][y] == '1':
            # 걸음 수를 더해준다.
            graph[x][y] = graph[a][b] + 1

            # 탐색할 곳을 추가한다.
            queue.append((x, y))

print(graph[n-1][m-1])
