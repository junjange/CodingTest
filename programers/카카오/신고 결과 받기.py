def solution(id_list, report, k):
    id_dict = {x: 0 for x in id_list} 
    answer = [0] * len(id_list)

    # 중복을 제거한 report를 반복 
    for i in set(report):
        id_dict[i.split()[1]] += 1 # 신고 받은 사람의 카운트

    # 중복을 제거한 report를 반복 
    for j in set(report):
        if id_dict[j.split()[1]] >= k: # 신고 받은 사람이 k번 이상 받은 경우
            answer[id_list.idex(j.split[0])] += 1  # 신고 한 사람을 카운트

    return answer

