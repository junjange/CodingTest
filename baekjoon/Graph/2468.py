import sys
sys.setrecursionlimit(10 ** 6)  # 재귀 허용 깊이를 수동으로 늘려주는 코드


# dfs 탐색
def dfs(x, y, k):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False

    # 비의 양보다 높은 건물이고 탐색하지 않았으면 탐색
    if graph[x][y] > k and visited[x][y] == False:

        visited[x][y] = True
        
        # 상/하/좌/우 재귀적으로 탐색
        dfs(x + 1, y, k)
        dfs(x - 1, y, k)
        dfs(x, y + 1, k)
        dfs(x, y - 1, k)

        return True
    return False


n = int(sys.stdin.readline())

# 각 노드가 연결된 정보를 표현
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
res = [] # 비의 양에 따른 안전한 영역의 리스트

# 비가 건물의 최대 높이까지 내린다고 가정하여 반복한다.
for k in range(101):
    
    # 탐색 여부
    visited = [[False] * n for _ in range(n)]
    
    # 안전한 영역의 건물의 수
    cnt = 0 
    for i in range(n):
        for j in range(n):
            if dfs(i, j, k):
                cnt += 1
    
    # 안전한 영역의 건물의 수를 리스트에 추가
    res.append(cnt)

    # 안전한 영역의 건물이 없다면 멈춘다.
    if cnt == 0:
        break
        
# 안전한 영역의 최대 개수를 출력
print(max(res))



