import sys
sys.setrecursionlimit(10 ** 6)


# df 탐색
def dfs(x, y):
    
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if graph[x][y] == 1:

        # 그림 개수 카운트
        cnt.append(1)
        
        # 해당 노드 방문 처리
        graph[x][y] = 0

        # 상/하/좌/우 재귀적으로 탐색
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)

        return True
    return False


n, m = map(int, sys.stdin.readline().split())

# 각 노드의 연결된 정보를 표현
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

cnt = [] # 그림의 개수 카운트
res = [] # 각 구역의 연결된 그림의 크기

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            dfs(i, j)
            res.append(len(cnt))
            cnt = []

# 그림의 개수 출력
print(len(res))

# 그림의 개수가 있으면 제일 큰 값을 출력
# 그게 아니라면 0을 출력
if len(res):
    print(max(res))
else:
    print(0)

    
    
    
