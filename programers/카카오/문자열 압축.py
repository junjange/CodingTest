# 16:20 => 17:18
def solution(s):
    answer = len(s)
    
    # 반복문을 통해 문자열 압축 길이 변경
    for i in range(1, len(s) // 2 + 1):
        res = ""
        temp = s[:i] # 문자열 압축 길이
        cnt = 1
        
        # 반복문을 통해 문자열 확인
        for j in range(i, len(s) + i, i):
            # 문자열 압축
            if temp == s[j : j + i]:
                cnt += 1
            
            else:
                if cnt == 1:
                    res += temp
                else:
                    res += str(cnt) + temp
                    
                temp = s[j : j + i] # 문자열 압축 길이 초기화
                cnt = 1
        
        # 문자열 압축 길이 최소
        answer = min(answer, len(res))
            
    return answer
