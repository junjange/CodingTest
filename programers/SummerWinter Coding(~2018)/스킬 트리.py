
# 10:51 => 11:09

def solution(skill, skill_trees):
    answer = 0
    
    # 반복문을 통해 스킬 트리를 확인
    for i in skill_trees:
        temp = []
        
        # 반복문을 통해 스킬 확인
        for j in i:
            # 스킬이 선행 스킬이라면 temp에 저장, 이미 있다면 저장하지 않는다.
            if j in skill and j not in temp:
                temp.append(j)
        
        
        # temp와 skill를 비교 후 카운트
        if "".join(temp) == skill[:len(temp)]:
            answer += 1
            
        
        
    return answer
