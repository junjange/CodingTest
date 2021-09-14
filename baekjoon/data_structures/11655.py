s = str(input())
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # 대문자 알파벳
lower = "abcdefghijklmnopqrstuvwxyz" # 소문자 알파벳
res = ""

# 입력받은 문자열을 반복문을 통해 확인
for i in s:
    
    # 대문자인지 확인
    if i.isupper():
        for j in range(len(upper)):
            # 해당 알파벳 위치 찾기
            if i == upper[j]:
                # 범위를 넘어가지 않으면 13을 더해준다.
                if j + 13 < 26:
                    res += upper[j + 13]
                    
                # 범위가 넘어가면 13을 빼준다.
                else:
                    res += upper[j - 13]
    # 소문자인지 확인
    elif i.islower():
        for j in range(len(lower)):
            # 해당 알파벳 위치 찾기
            if i == lower[j]:
                
                # 범위를 넘어가지 않으면 13을 더해준다.
                if j + 13 < 26:
                    res += lower[j + 13]
                    
                # 범위가 넘어가면 13을 빼준다.
                else:
                    res += lower[j - 13]
    
    # 그 외 문자는 그대로 추가한다.
    else:
        res += i

print(res)
