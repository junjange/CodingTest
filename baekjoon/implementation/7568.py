import sys

n = int(sys.stdin.readline())
m = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = []
for x, y in m:
    cnt = 1
    for p, q in m:
        if x < p and y < q:
            cnt += 1

    answer.append(cnt)

print(*answer)
