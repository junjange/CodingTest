import sys
sys.setrecursionlimit(10 ** 6)  # 재귀 허용 깊이를 수동으로 늘려주는 코드


# dfs 탐색
def dfs(x, y):
    if x <= -1 or x >= m or y <= -1 or y >= n:
        return False

    # 탐색하지 않은 공간이면 탐색
    if graph[x][y] == 0:
        graph[x][y] = 1
        cnt.append(1)

        # 상/하/좌/우 재궈적으로 탐색
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True
    return False


m, n, k = map(int, sys.stdin.readline().split())

# 직사각형을 1로 포현한다.
graph = [[0] * n for _ in range(m)]
for k in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1

cnt = [] # 빈 공간 개수 카운트
res = [] # 빈 영역의 크기


for i in range(m):
    for j in range(n):
        if dfs(i, j):
            
            # 빈 공간 개수로 빈영역의 크기를 구한다.
            res.append(len(cnt))
            cnt = []

# 오름차순으로 정렬 후 영역의 개수와 영역의 크기를 순서대로 출력
res.sort()
print(len(res))
for i in res:
    print(i, end=" ")

