import sys


n = int(sys.stdin.readline())
stack = []
res = []
cnt = 1
temp = 0

# 반복문을 통해 정수를 입력받는다.
for i in range(n):

    num = int(sys.stdin.readline())

    # 입력받은 정수보다 스택에 들어갈 정수가 클때까지 반복
    while num >= cnt:
        # 입력받은 정수가 스택에 들어갈 정수보다 크다면 스택에 정수를 추가한다.
        stack.append(cnt)
        res.append("+")
        cnt += 1 # 스택에 들어갈 정수를 +1 한다.

    # 스택에 마지막 요소가 입력받은 정수와 같다면
    if stack[-1] == num:
        # 스택에 있는 요소를 팝한다.
        stack.pop()
        res.append("-")

    # 스택에 마지막 요소가 입력받은 정수와 같지 않다면 입력된 수열을 만들 수 없다.
    else:
        temp = 1
        break

if temp:
    print("NO")
else:
    for i in res:
        print(i)

