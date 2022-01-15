import sys


inx = 1
# 반복문을 통해 문자열을 확인
while True:
    word = list(map(str, sys.stdin.readline().strip()))

    # 문자열이 "-"가 한 개 이상일 경우 반복문을 멈춘다.
    if word.count("-") >= 1:
        break

    cnt = 0
    stack = [word[0]] 
    # 반복문을 통해 안정적인 문자열을 찾는다.
    for i in range(1, len(word)):
        
        if stack:
            # 안정적인 문자열이라면 pop 한다.
            if stack[-1] == '{' and word[i] == '}':
                stack.pop()
                continue
                
        # 문자열을 계속해서 추가
        stack.append(word[i])
    
    # 안정적인 문자열을 제외한 문자열을 안정적인 문자열로 바꿔준다.
    for j in range(0, len(stack), 2):
        if stack[j] == "}":
            cnt += 1

        if stack[j + 1] == "{":
            cnt += 1

    print("{0}. {1}".format(inx, cnt))
    inx += 1
