import sys

# dfs, bfs 문제
cnt = []

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False

    if graph[x][y] == 1:
        cnt.append(1)
        graph[x][y] = 0
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x , y + 1)
        return True
    return False


n = int(sys.stdin.readline())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))


result = 0
result_list = []
for i in range(n):
    for j in range(n):

        if dfs(i, j) == True:
            result += 1
            result_list.append(len(cnt))
            cnt = []

result_list.sort()
print(result)
for i in result_list:
    print(i)