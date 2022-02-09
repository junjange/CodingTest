import sys

n = int(sys.stdin.readline())
storage_list = [0] * 1001
max_h = 0 # 최대 높이
max_h_l = 0 # 최대 높이의 위치
end_idx = 0 # 마지막 위치

# 반복문을 통해 최대 높이를 구한다.
for _ in range(n):
    l, h = map(int, input().split())
    storage_list[l] = h # l 위치에 h 높이의 박스

    # 현재 높이가 최대 높이보다 크다면
    if max_h < h:
        max_h = h # 최대 높이 초기화
        max_h_l = l # 최대 높이의 위치 초기화

    # 마지막 인덱스 확인
    end_idx = max(end_idx, l)

answer = 0
stack = []

# 왼쪽부터 벽을 확인
# 반복문에 조건을 보게되면 
# 최대 높이의 위치 + 1까지 반복하여 최대 높이까지 더해주는 것을 확인할 수 있다.
for i in range(0, max_h_l+1):
    
    # 저장된 상자가 없으면
    if not stack:
        # 현재 위치에 상자를 추가
        stack.append(storage_list[i])
        # 현재 위치에 상자를 창고 넓이에 더한다.
        answer += stack[-1]
        
    # 저장된 상자가 있으면
    else:
        # 창고에 마지막 상자의 높이와 현재 위치에 상자에 높이를 비교
        if stack[-1] < storage_list[i]:
            # 현재 위치에 상자에 높이가 더 높다면 
            # 창고에 마지막 상자의 높이를 현재 상자의 높이로 초기화
            stack.pop()
            stack.append(storage_list[i])
        
        # 창고의 넓이에 창고에 마지막 상자의 높이를 더한다.
        answer += stack[-1]

stack = []
# 오른쪽부터 벽을 확인
# 왼쪽부터 확인하는 것과 같고 
# 다른점은 최대 높이의 벽을 창고의 넓이에 더하지 않는다는 것이다.
for i in range(end_idx, max_h_l, -1):
    if not stack:
        stack.append(storage_list[i])
        answer += stack[-1]
    else:
        if stack[-1] < storage_list[i]:
            stack.pop()
            stack.append(storage_list[i])
        answer += stack[-1]

print(answer)
