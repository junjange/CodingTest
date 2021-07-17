import sys
sys.setrecursionlimit(10**6) # 재귀 허용 깊이를 수동으로 늘려주는 코드


# dfs 탐색
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 1:
        # 해당 노드 방문 처리
        graph[x][y] = 0
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)

        return True
    return False


t = int(sys.stdin.readline())

# 테스트 케이스만큼 반복
for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())

    # 각 노드가 연결된 정보를 표현
    graph = [[0] * (m + 1) for i in range(n + 1)]

    # 2차원 리스트의 맵 정보를 입력 받는다.
    for i in range(k):
        a, b = map(int, sys.stdin.readline().split())
        graph[b][a] = 1

    cnt = 0
    # 현재 위치에서 DFS 수행
    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                cnt += 1

    print(cnt)
    
