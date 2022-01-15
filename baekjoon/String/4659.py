import sys

aeiou = ["a", "e", "i", "o", "u"] # 모음

# 반복문을 통해 패스워드를 확인
while True:
    word = list(map(str, sys.stdin.readline().strip()))
    flag = False # 규칙 판별
    
    # 패스워드 확인 종료
    if "".join(word) == "end":
        break
    
    # 반복문을 통해 모음이 하나라도 들어가 있는지 확인
    for k in word:
        if k in aeiou:
            flag = True
            break
    
    # 모음이 안들어가 있다면 not으로 출력
    if not flag:
        print("<{0}> is not acceptable.".format("".join(word)))
        continue
    
    temp1 = 0 # 모음
    temp2 = 0 # 자음
    target = "" # 이전 문자
    
    # 반복문을 통해 모음이 3개 혹은 자음이 3개 연속으로 나오는지 확인
    # + 같은 글자가 연속적으로 두번 나오는지 확인(ee와 oo는 제외)
    for i in word:
        if i in aeiou:
            temp1 += 1
            temp2 = 0
        else:
            temp1 = 0
            temp2 += 1

        if target == i:
            if target != "e":
                if target != "o":
                    flag = False
                    break
        else:
            target = i

        if temp1 == 3 or temp2 == 3:
            flag = False
            break

    if flag:
        print("<{0}> is acceptable.".format("".join(word)))
    else:
        print("<{0}> is not acceptable.".format("".join(word)))

