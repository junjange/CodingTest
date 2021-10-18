import sys

n = int(sys.stdin.readline())
stack = [int(sys.stdin.readline()) for _ in range(n)]
top = stack.pop() # 제일 높은 막대기
cnt = 1 # 보이는 막대기의 수

# 반복문을 통해 막대기의 높이를 확인
for i in range(1, n):
    now = stack.pop() # 현재 막대기의 높이

    # 현재 막대기가 제일 높은 막대기보다 높으면
    if now > top:
        cnt += 1 # 카운트
        top = now # 제일 높은 막대기를 현재 막대기로 초기화

# 보이는 막대기의 수 출력
print(cnt)
