import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[0 for _ in range(n)] for _ in range(n)]

# 우/하/좌/상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
x = n // 2 # 처음 x 좌표
y = n // 2 # 처음 y 좌표
num = 1
l = 0
graph[x][y] = 1
answer = []

# 반복문을 통해 달팽이를 움직인다.
while True:
    # 우/하/좌/상 이동
    for i in range(4):
        # 길이만큼 이동
        for _ in range(l):
            x += dx[i]
            y += dy[i]
            num += 1
            graph[x][y] = num

    # 달팽이가 움직였을 때 좌표가 0,0이라면 반복을 멈춤
    if x == y == 0:
        break

    # 왼쪽 모서리로 이동
    x -= 1
    y -= 1
    l += 2  # 달패이가 움직이는 직선 길이

for j in range(len(graph)):
    print(*graph[j])
    if m in graph[j]:
        mx = j + 1
        my = graph[j].index(m) + 1
        
print(mx, my)
