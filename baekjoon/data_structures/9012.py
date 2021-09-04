import sys


t = int(sys.stdin.readline())

for i in range(t):
    stack = list(map(str, sys.stdin.readline().strip()))

    # 리스트에 아무것도 없을 때까지 반복
    while stack:

        # 리스트에 첫 번째 문자가 "(" 이며 리스트에 ")" 문자가 있으면 괄호를 제거
        if stack[0] == "(" and stack.count(")"):
            stack.remove(stack[0])

            for j in range(len(stack)):

                if stack[j] == ")":
                    stack.remove(stack[j])
                    break

        # 조건이 맞지 않으면 반복문을 멈춘다.
        else:
            break

    # 리스트가 비워 있으면 "YES" 문자가 있으면 "NO"
    if stack:
        print("NO")
    else:
        print("YES")



        
