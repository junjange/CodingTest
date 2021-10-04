import sys

t = int(sys.stdin.readline())

# 테스트 케이스만큼 반복
for _ in range(t):
    l = list(map(str, sys.stdin.readline().strip()))
    stack = []
    res = []

    # 반복문을 통해 강산이의 입력 순서를 확인
    for i in l:
        # 입력이 "-" 이고 res 리스트에 요소가 있으면 res 리스트를 팝한다.
        if i == "-":
            if res:
                res.pop()
        
        # 입력이 "<" 이고 res 리스트에 요소가 있으면 res 리스트를 팝하고 팝한 것을 stack 리스트에 추가
        elif i == "<":
            if res:
                stack.append(res.pop())
                
        # 입력이 ">" 이고 stack 리스트에 요소가 있으면 stack 리스트를 팝하고 팝한 것을 res 리스트에 추가
        elif i == ">":
            if stack:
                res.append(stack.pop())
        
        # 그 외 입력은 res 리스트에 추가
        else:
            res.append(i)
    
    # 반복문을 통해 모든 입력을 확인한 후에는 두개의 리스트를 합쳐준다.
    while stack:
        res.append(stack.pop())

    print("".join(res))
