import sys

temp = list(map(str, sys.stdin.readline().strip()))
stack = [] # 커서 오른쪽에 있는 요소
n = int(sys.stdin.readline())
for i in range(n):
    # temp 맨 오른쪽에 있는 위치가 커서의 위치
    order = list(map(str, sys.stdin.readline().split()))

    # 커서를 왼쪽으로 한칸 옮김
    if order[0] == "L" and temp:
        stack.append(temp.pop())

    # 커서를 오른쪽으로 한칸 옮김
    elif order[0] == "D" and stack:
        temp.append(stack.pop())

    # 커서 왼쪽에 있는 문자를 삭제
    elif order[0] == "B" and temp:
        temp.pop()

    # 커서 왼쪽에 문자를 추가
    elif order[0] == "P":
        temp.append(order[1])

# 문자열과 커서 오른쪽에 위치해야할 요소를 출력
print("".join(temp + list(reversed(stack))))

