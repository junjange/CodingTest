import sys

n = int(sys.stdin.readline())
top = list(map(int, sys.stdin.readline().split()))
stack = [] # 비교할 탑의 스택
res = [0] * n

# 반복문을 통해 탑의 높이를 확인
for i in range(n):
    # 스택에 탑이 있는지 확인
    if stack:
        while True:
            # 비교해야하는 탑의 높이와 스택에 마지막 탑의 높이를 비교
            # 스택에 마지막 탑의 높이가 더 클 때
            if top[i] <= stack[-1][0]:

                # 현재 탑의 레이저 신호를 수신해야하는 탑이 스택에 마지막 탑이 된다.
                # 스택에 마지막 탑의 위치를 결과 리스트에 + 1 해주어 초기화
                res[i] = stack[-1][1] + 1
                stack.append([top[i], i]) # 현재 비교한 탑의 높이를 추가하고 반복을 멈춘다.
                break

            # 스택에 마지막 탑의 높이가 작다면 마지막 탑을 팝한다.
            # 현재 탑의 높이보다 작은 스택에 마지막 탑은 수신할 수 없기 때문에 팝
            else:
                stack.pop()
            
            # 스택에 탑이 없을 경우 스택에 현재 높이의 탑을 추가하고 반복을 멈춘다.
            if not stack:
                stack.append([top[i], i])
                break

    # 스택에 탑이 없으면 현재 비교해야하는 탑의 높이와 순서를 스택에 추가
    else:
        stack.append([top[i], i])
        
print(*res)
