import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque()
for i in range(n):
    order = list(map(str, sys.stdin.readline().split()))

    if order[0] == "push_front":
        queue.appendleft(order[1])

    elif order[0] == "push_back":
        queue.append(order[1])

    elif order[0] == "pop_front":
        if queue:
            print(queue.popleft())
        else:
            print(-1)

    elif order[0] == "pop_back":
        if queue:
            print(queue.pop())
        else:
            print(-1)

    elif order[0] == "size":
        print(len(queue))

    elif order[0] == "empty":
        if queue:
            print(0)
        else:
            print(1)
            
    elif order[0] == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)

    elif order[0] == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)



