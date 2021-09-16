import sys

k = int(sys.stdin.readline())
stack = []

# 정수 개수만큼 반복한다.
for i in range(k):

    # 쓴 돈의 수를 입력 받는다.
    num = int(sys.stdin.readline())

    # 잘못된 수를 불렀다면 스택에서 팝해준다.
    if num == 0:
        stack.pop()
        
    # 정확한 수를 불렀다면 스택에 쓴 돈의 수를 추가한다.
    else:
        stack.append(num)

# 스택의 합을 출력한다.
print(sum(stack))
