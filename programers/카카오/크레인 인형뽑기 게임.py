def solution(board, moves):
    answer = 0
    pick_up = []
    # 반복문을 통해 크레인의 위치를 이동
    for move in moves:
        # 크레인이 뽑을 수 있는 인형을 확인
        for i in range(len(board)):
            if board[i][move-1] != 0:
                pick_up.append(board[i][move-1])
                board[i][move-1] = 0
                
                if len(pick_up) >= 2:
                    if pick_up[-1] == pick_up[-2]:
                        pick_up.pop()
                        pick_up.pop()
                        answer += 2
                break
                
    return answer
