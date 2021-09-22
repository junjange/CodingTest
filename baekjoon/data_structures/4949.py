import sys

while True:
    c = str(sys.stdin.readline().rstrip())
    stack = []
    
    # 점 하나가 들어오면 반복문을 멈춰준다.
    if c == ".":
        break

    # 반복문을 통해 입력받은 문자열을 확인한다.
    for i in c:

        # '('와 '[' 를 스택에 추가한다.
        if i == '(' or i == "[":
            stack.append(i)

        # 입력받은 문자가 ')'라면
        elif i == ')':
            # 스택에 요소가 있고 스택의 마지막 요소가 '('라면 
            # 괄호가 균형이 맞으므로 스택 맨 뒤에 있는 '(' 요소를 팝해준다. 
            if stack and stack[-1] == '(':
                stack.pop()
                
            # 그게 아니라면 균형이 맞지 않으므로 스택에 요소를 하나 추가하고 반복을 멈춰준다. 
            else:
                stack.append(i)
                break
        # 입력받은 문자가 ']'라면
        elif i == ']':
            # 스택에 요소가 있고 스택의 마지막 요소가 '['라면 
            # 괄호가 균형이 맞으므로 스택 맨 뒤에 있는 '[' 요소를 팝해준다. 
            if stack and stack[-1] == '[':
                stack.pop()

            # 그게 아니라면 균형이 맞지 않으므로 스택에 요소를 하나 추가하고 반복을 멈춰준다. 
            else:
                stack.append(i)
                break

    # 스택 안에 요소가 있으면 no 를, 없으면 yes 를 출력한다.
    if stack:
        print("no")
    else:
        print("yes")
