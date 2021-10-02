import sys

s = str(sys.stdin.readline().strip())
stack = []

# 입력받은 괄호를 반복문을 통해 확인한다.
for i in s:
    # i가 "(", "[" 일 경우 스택에 추가
    if i == "(" or i == "[":
        stack.append(i)

    else:
        if stack and i == ')':
            # 스택의 길이가 1보다 크고 스택 맨 뒤에 두번째 요소가 "("이고 스택 맨 뒤에 요소가 숫자일 경우
            # "()" 괄호 안에 들어 있는 숫자 이므로 (2 * x) 를 해준다.
            if len(stack) > 1 and stack[-2] == "(" and str(stack[-1]).isdigit():
                cnt = stack.pop() * 2 # 숫자 팝
                stack.pop() # "(" 팝
                stack.append(cnt)

            # 스택의 맨 뒤에 요소가 "("일 경우
            # "()" 괄호 이므로 2를 스택에 추가
            elif stack[-1] == '(':
                stack.pop() # "(" 팝
                stack.append(2)

            # 그 외의 문자열은 올바르지 못한 괄호
            else:
                stack.append("fall")
                break

        elif stack and i == ']':
            # 스택의 길이가 1보다 크고 스택 맨 뒤에 두번째 요소가 "["이고 스택 맨 뒤에 요소가 숫자일 경우
            # "[]" 괄호 안에 들어 있는 숫자 이므로 (3 * x) 를 해준다.
            if len(stack) > 1 and stack[-2] == "[" and str(stack[-1]).isdigit():
                cnt = stack.pop() * 3 # 숫자 팝
                stack.pop() # "[" 팝
                stack.append(cnt)

            # 스택의 맨 뒤에 요소가 "["일 경우
            # "[]" 괄호 이므로 3을 스택에 추가
            elif stack[-1] == '[':
                stack.pop()
                stack.append(3)

            # 그 외의 문자열은 올바르지 못한 괄호
            else:
                stack.append("fall")
                break

        # # 그 외의 문자열은 올바르지 못한 괄호
        else:
            stack.append("fall")
            break

    # 스택의 길이가 1보다 크고 스택의 맨 뒤 두번째 요소와 맨 뒤에 요소가 숫자일 경우 두 요소를 더해준다.
    if len(stack) > 1 and str(stack[-1]).isdigit() and str(stack[-2]).isdigit():
        stack.append(stack.pop() + stack.pop())

# 스택의 길이가 1이고 숫자일 경우 스택의 값을 출력
if len(stack) == 1 and str(stack[-1]).isdigit():
    print(*stack)
    
# 그 외에는 올바르지 못한 괄호 이므로 0을 출력
else:
    print(0)
