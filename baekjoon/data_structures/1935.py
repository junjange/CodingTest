import sys

n = int(sys.stdin.readline())
c = list(map(str, sys.stdin.readline().strip()))
num = [float(sys.stdin.readline()) for i in range(n)]

stack = []

for i in c:
    # 대문자인지 확인
    if i.isupper():

        # nums[해당 문자의 아스키코드에 해당하는 index]
        stack.append(num[ord(i) - ord('A')])

    # 대문자가 아니라면 연산자를 통해 연산한다.
    else:
        # 스택에 맨 위에 두 문자를 팝한다.
        a = stack.pop()
        b = stack.pop()

        # 팝한 두 문자를 eval()함수를 통해 연산하고 다시 스택에 넣는다.
        stack.append(eval(str(b) + i + str(a)))
  
# 스텍에 쌓이 하나의 숫자를 소수 둘째 자리까지 출략한다.
print(format(stack[0], ".2f"))
