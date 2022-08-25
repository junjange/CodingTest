import sys


def solve(start):
    global cnt
    quack = 'quack'
    j = 0
    first = True

    # 반복문을 통해 탐색 시작 지점부터 울음소리의 끝 지점까지 울음소리 확인
    for i in range(start, len(duck)):

        # 울음 소리가 quack이고 탐색하지 않았다면
        if duck[i] == quack[j] and not visited[i]:
            visited[i] = True
            if duck[i] == 'k':
                if first:
                    cnt += 1
                    first = False
                j = 0
                continue
            j += 1


duck = list(map(str, sys.stdin.readline().rstrip("\n")))
visited = [False] * len(duck)
cnt = 0
if len(duck) % 5 != 0:
    print(-1)
    exit()


# 반복문을 통해 오리의 울음소리를 확인
for i in range(len(duck)):
    # 울음소리에 시작이 q이고 탐색하지 않은 자리라면
    if duck[i] == 'q' and not visited[i]:
        solve(i)

if not all(visited) or cnt == 0:
    print(-1)
else:
    print(cnt)
