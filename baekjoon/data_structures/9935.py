import sys

s = str(sys.stdin.readline().strip())
bomb = str(sys.stdin.readline().strip())
stack = []

# 반복문을 통해 문자열을 확인한다.
for i in s:
    # 스택에 문자를 추가한다.
    stack.append(i)

    # 스택의 마지막 요소와 폭발 문자열의 마지막 요소가 같고
    # 스택의 맨 뒤에 폭발 문자열 길이만큼 짜른 것의 문자열과 폭발 문자열이 같으면 
    # 스택의 맨 뒤에 폭발 문자열 길이만큼 짜른 것의 문자열을 제거한다. 
    if stack[-1] == bomb[-1] and "".join(stack[-len(bomb):]) == bomb:
        del stack[-len(bomb):]

# 스택이 남아있으면 남은 스택을 출력
if stack:
    print("".join(stack))
    
# 그렇지 않다면 "FRULA" 출력
else:
    print("FRULA")

