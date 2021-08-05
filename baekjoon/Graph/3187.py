import sys
sys.setrecursionlimit(10 ** 6)  # 재귀 허용 깊이를 수동으로 늘려주는 코드


# dfs 탐색
def dfs(x, y):
    if x <= -1 or x >= r or y <= -1 or y >= c:
        return False

    if graph[x][y] != "#":
        
        # 각 구역의 모든 문자열을 추가
        battle.append(graph[x][y])
        
        # 해당 노드 방문 처리
        graph[x][y] = "#"
        
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)

        return True
    return False


r, c = map(int, sys.stdin.readline().split())

# 각 노드가 연결된 정보를 표현
graph = [list(map(str, input())) for _ in range(r)]

# 각 구역에서 누가 살아남았는지 비교하기 위한 리스트
battle = []

# 각 구역에서 승리한 늑대와 양
res_v = []
res_k = []

for i in range(r):
    for j in range(c):
        # 울타리가 아니라면 탐색
        if graph[i][j] != "#":
            dfs(i, j)

            # 각 구역마다 양과 늑대 중 누가 살아남는지 비교
            if battle.count('v') < battle.count('k'):
                res_k.append(battle.count('k'))
            else:
                res_v.append(battle.count('v'))

            # 새로운 구역을 위해 비운다.
            battle = []

# 각 구역에서 승리한 양과 늑대의 합을 출력
print(sum(res_k), sum(res_v))



