import sys
sys.setrecursionlimit(10 ** 6)


def dfs(x, y):
    if x <= -1 or x >= h or y <= -1 or y >= w:
        return False

    if graph[x][y] == "#":
        graph[x][y] = "."
        cnt.append(1)
        dfs(x + 1, y)
        dfs(x - 1 , y)
        dfs(x, y + 1)
        dfs(x, y - 1)

        return True
    return False


t = int(sys.stdin.readline())
res = []
temp = []
for _ in range(t):
    cnt = []
    h, w = map(int, sys.stdin.readline().split())
    graph = [list(map(str, sys.stdin.readline().strip())) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if graph[i][j] == "#":
                dfs(i, j)
                temp.append(len(cnt))
                cnt = []

    print(len(temp))
    temp = []


    
    
