def solution(lottos, win_nums):
    answer = [lottos.count(0), 6]
    rank = [6, 6, 5, 4, 3, 2, 1]
    
    cnt = 0
    for i in lottos:
        if i in win_nums:
            answer[0] += 1
        else:
            answer[1] -= 1
    
    answer = [rank[answer[0]], rank[answer[1]]]
            
    return answer
