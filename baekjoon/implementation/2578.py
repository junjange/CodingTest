import sys


def solve(target, graph):
    for i in range(5):
        for j in range(5):
            if target == graph[i][j]:
                graph[i][j] = 0
                return


def check(graph):
    cnt = 0
    for i in range(5):
        temp = 0
        for j in range(5):
            if graph[i][j] == 0:
                temp += 1
        if temp == 5:
            cnt += 1
    for i in range(5):
        temp = 0
        for j in range(5):
            if graph[j][i] == 0:
                temp += 1
        if temp == 5:
            cnt += 1

    if graph[0][4] == graph[1][3] == graph[2][2] == graph[3][1] == graph[4][0] == 0:
        cnt += 1
    if graph[0][0] == graph[1][1] == graph[2][2] == graph[3][3] == graph[4][4] == 0:
        cnt += 1

    return cnt


bingo = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]
answer_bingo = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]


answer = 0
for i in range(5):
    for j in range(5):
        answer += 1
        solve(answer_bingo[i][j], bingo)
        if check(bingo) >= 3:
            print(answer)
            exit()

