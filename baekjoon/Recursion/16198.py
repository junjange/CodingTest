import sys


def back_tacking(x):
    global answer

    # 에너지를 모았다면 answer와 비교하여 초기화
    if len(w) == 2:
        answer = max(answer, x)
        return
    
    # 반복문을 통해 에너지 구슬을 확인
    for i in range(1, len(w) - 1):
        target = w[i - 1] * w[i + 1] # i번째 구슬을 제거했을 때 나오는 에너지
        
        # 백트래킹 
        v = w.pop(i) # 에너지 구슬 제거
        back_tacking(x + target) # 제거된 구슬로 에너지를 재귀적으로 탐색
        w.insert(i, v) # 제거한 에너지 구슬 추가


n = int(sys.stdin.readline())
w = list(map(int, sys.stdin.readline().split()))
answer = 0
back_tacking(0)
print(answer)


