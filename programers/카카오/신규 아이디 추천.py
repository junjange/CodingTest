# 21:20

def solution(new_id):
    answer = ''
    l = len(new_id)
    
    # 반복문을 통해 id를 확인
    for i in range(l):
        
        # 1단계
        if new_id[i].isupper():
            answer += new_id[i].lower()
        
        # 3단계
        elif len(answer) > 0 and answer[-1] == "." and new_id[i] == ".":
            continue
            
        # 2단계
        elif new_id[i] == "-" or new_id[i] == "_" or new_id[i].isdigit() or new_id[i] == "." or new_id[i].islower():
            answer += new_id[i]
        
        # 4단계
        if len(answer) > 0 and answer[0] == ".":
            answer = ""
            
    
    # 6단계
    answer = answer[0:15]

    if len(answer) > 0:
        # 4단계
        if answer[-1] == ".":
            answer = answer[:len(answer) - 1]
        
        # 7단계
        while len(answer) < 3:
            answer += answer[-1]
    else:
        # 5단계
        answer = "aaa"   
                
    return answer
