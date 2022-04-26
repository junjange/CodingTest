# 01:12 => 01:27

def solution(record):
    answer = []
    temp = []
    uid = {}
    
    # 반복문을 통해 입력 값을 확인
    for i in record:
        i = i.split(" ")
        
        # 입력 값이 Enter일 경우 uid 값의 닉네임 추가, temp에 상태와 uid 값 추가 
        if i[0] == "Enter":
            uid[i[1]] = i[2]
            temp.append([0, i[1]])
        
        # 입력 값이 Leave 경우 temp에 상태와 uid 값 추가
        elif i[0] == "Leave":
            temp.append([1, i[1]])
            
        # 입력 값이 Change일 경우 uid 값의 닉네임 변경
        else:
            uid[i[1]] = i[2]
            
    
    # 반복문을 통해 상태와 uid의 닉네임을 answer에 추가
    for i in temp:
        state, id = i[0], i[1]
        
        if state == 0:
            answer.append(uid[i[1]] + "님이 들어왔습니다.")
        else:
            answer.append(uid[i[1]] + "님이 나갔습니다.")
        
    
    
    return answer
