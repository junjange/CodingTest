import sys


n, s = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
target = 0
left = 0
right = 0
answer = 1e9

# 반복문을 통해 수열을 확인
while True:

    # left부터 right까지 수열의 합이 s를 넘는다면
    if target >= s:

        answer = min(answer, right - left) # 매 순간 최소 길이로 초기화
        target -= num[left] # 현재 수열의 시작 위치 값을 빼주고
        left += 1 # 현재 수열의 시작 위치를 한 계단 앞으로 이동

    # left부터 right까지 수열의 합이 s를 넘지 않는다면
    else:

        # 맨 끝 위치가 n과 같다면 반복을 멈춰준다. s를 넘는 수열을 만들 수 없기 때문 
        if right == n:
            break
        
        target += num[right] # 현재 수열의 마지막 위치 값을 더해주고
        right += 1 # 수열의 마지막 위치를 한 계단 앞으로 이동

# answer가 바뀌지 않았다면 0 출력 바뀌였다면 바뀐 값 출력
print(0) if answer == 1e9 else print(answer)
