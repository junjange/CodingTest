import math

def solution(n, words):
    answer = []
    temp = []
    
    # 반복문을 통해 단어 확인
    for i in words:
        # 규칙에 어긋나면 멈춘다.
        if (len(temp) > 0 and temp[-1][-1] != i[0]) or i in temp:
            break
        
        temp.append(i)
    

    if temp == words:
        answer = [0,0]
    else:
        
        c = (len(temp) % n) + 1 # 번호
        d = math.ceil((len(temp) + 1) / n) # 차례
        answer = [c, d]
        
    return answer
