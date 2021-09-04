import sys


n = int(sys.stdin.readline())
stack = []

# 반복문을 통해 명령을 수행
for i in range(n):
    # 리스트 형식으로 명령을 받는다.
    order = list(map(str, sys.stdin.readline().split()))

    if order[0] == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
            
    elif order[0] == "size":
        print(len(stack))

    elif order[0] == "empty":
        if stack:
            print(0)
        else:
            print(1)
            
    elif order[0] == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)
    
    else:
        stack.append(order[1])
