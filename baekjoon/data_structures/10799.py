import sys

n = list(map(str, sys.stdin.readline().strip()))

stack = []
res = 0

# 모든 괄호를 탐색한다.
for i in range(len(n)):

    if n[i] == "(":
        stack.append("(")

    # 이전 괄호가 ")"라면 막대기에 마지막 부분을 자른 것으로 +1을 해준다.
    elif n[i - 1] == ")":
        stack.pop()
        res += 1

    # 현재 괄호가 ")"라면 레이저의 앞에 막대기의 개수를 한번씩 자른 것으로 스택의 길이를 더해준다.
    else:
        stack.pop()
        res += len(stack)

print(res)

