import sys

sys.setrecursionlimit(10 ** 6)  # 재귀 허용 깊이를 수동으로 늘려주는 코드


# 우리 병사 dfs 탐색
def dfs_W(x, y):
    # 주어진 범위를 벗어나는 경우에 즉시 종료
    if x <= -1 or x >= m or y <= -1 or y >= n:
        return False

    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == "W":
        
        # 병사 수를 추가
        cnt_W.append(1)
        
        # 임의에 문자열로 해당 노드 방문 처리
        graph[x][y] = "E"
        
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs_W(x - 1, y)
        dfs_W(x, y - 1)
        dfs_W(x + 1, y)
        dfs_W(x, y + 1)

        return True
    return False


# 적군 병사 dfs 탐색
def dfs_B(x, y):
    # 주어진 범위를 벗어나는 경우에 즉시 종료
    if x <= -1 or x >= m or y <= -1 or y >= n:
        return False

    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == "B":
        
        # 병사 수를 추가
        cnt_B.append(1)
        
        # 임의에 문자열로 해당 노드 방문 처리
        graph[x][y] = "E"
        
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs_B(x - 1, y)
        dfs_B(x, y - 1)
        dfs_B(x + 1, y)
        dfs_B(x, y + 1)

        return True
    return False


n, m = map(int, sys.stdin.readline().split())

# 각 노드가 연결된 정보를 표현
graph = [list(map(str, input())) for _ in range(m)]

# 우리 병사 수와 위력
cnt_W = []
res_W = []

# 적군 병사 수와 위력
cnt_B = []
res_B = []
for i in range(m):
    for j in range(n):
        if dfs_W(i, j):
            # 우리 병사 위력을 계산하여 추가
            res_W.append(len(cnt_W) ** 2)
            cnt_W = []

        elif dfs_B(i, j):
            # 적군 병사 위력을 계산하여 추가
            res_B.append(len(cnt_B) ** 2)
            cnt_B = []
            
# 각 병사의 위력의 합을 출력
print(sum(res_W), sum(res_B))


