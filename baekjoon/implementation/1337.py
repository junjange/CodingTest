import sys


n = int(sys.stdin.readline())
m = sorted(int(sys.stdin.readline()) for _ in range(n))
answer = []

# 반복문을 통해 배열을 확인
for i in m:
    cnt = 0
    
    # 반복문을 통해 각 수에서 시작되는 연속적인 수가 배열에 있는지 확인
    for j in range(i, i + 5):
        # 연속적이지 않은 수를 카운트
        if j not in m:
            cnt += 1
    
    # 연속적이지 않은 수를 answer 추가
    answer.append(cnt)

print(min(answer))
