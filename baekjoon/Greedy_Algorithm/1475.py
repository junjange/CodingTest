import sys
n = list(map(int, sys.stdin.readline().strip()))
cnt = 0

# 반복문을 통해 필요한 세트를 찾는다.
while n:
    num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] # 플라스틱 숫자 세트
    temp = []
    
    # 반복문을 통해 필요한 숫자를 확인
    for i in n:
        # 필요한 숫자가 플라스틱 숫자 세트에 있으면 
        if i in num:
            temp.append(i)
            num.remove(i)
        
        # 필요한 숫자가 플라스틱 숫자 세트에 없지만 6과 9의 경우인 경우 처리
        else:
            if i == 6 and 9 in num:
                temp.append(i)
                num.remove(9)
            elif i == 9 and 6 in num:
                temp.append(i)
                num.remove(6)
    
    # 필요한 숫자를 챙긴다.
    for j in temp:
        n.remove(j)
    
    # 카운트
    cnt += 1

print(cnt)

