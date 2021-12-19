import sys


n = int(sys.stdin.readline())
cnt = 0

# 반복문을 통해 단어를 확인
for _ in range(n):
    word = list(map(str, sys.stdin.readline().strip()))
    stack = [word[0]] # 스택을 이용하여 문제를 수행
    flag = True # 그룹 단어의 유무

    # 반복문을 통해 스택에 있는 문자와 비교하는 문자를 확인
    for i in range(1, len(word)):

        # 스택에 담겨있는 문자가 현재 비교하고 있는 문자와 다르고 스택에 현재 비교하고 있는 문자가 있다면
        # 그룹 단어가 될 수 없다.
        if stack[i - 1] != word[i]:
            if word[i] in stack:
                flag = False
                break
        # 스택에 현재 비교한 문자를 추가한다.
        stack.append(word[i])
    
    # 그룹 단어의 유무에 따라 카운트
    if flag:
        cnt += 1
        
print(cnt)
