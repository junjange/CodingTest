import sys
sys.setrecursionlimit(10 ** 6)  # 재귀 허용 깊이를 수동으로 늘려주는 코드


def dfs(x, y):

    if -1 >= x or x >= r or -1 >= y or y >= c:
        return False

    if graph[x][y] != '#':

        if graph[x][y] == 'v':
            v.append(1)
        elif graph[x][y] == 'o':
            o.append(1)

        graph[x][y] = '#'

        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True
    return False


r, c = map(int, sys.stdin.readline().split())

graph = [list(map(str, sys.stdin.readline().strip())) for _ in range(r)]
o = []
v = []
sheep = 0
wolf = 0
for i in range(r):
    for j in range(c):
        if graph[i][j] != '#':
            dfs(i, j)
            if len(v) >= len(o):
                wolf += len(v)
            else:
                sheep += len(o)
            v = []
            o = []

print(sheep, wolf)


