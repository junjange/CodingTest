import sys
from collections import deque


# bfs 탐색
def bfs(v):
    queue = deque()
    queue.append([v])

    while queue:
        target = queue.popleft()

        temp = target[0]

        if temp == 1:

            return target

        if temp % 3 == 0:
            queue.append([temp // 3] + target)

        if temp % 2 == 0:
            queue.append([temp // 2] + target)

        queue.append([temp - 1] + target)


n = int(sys.stdin.readline())
res = bfs(n)

print(len(res) - 1)
print(*res[::-1])


