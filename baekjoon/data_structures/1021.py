import sys

n, m = map(int, sys.stdin.readline().split())
queue = [i for i in range(1, n + 1)]
loc = list(map(int, sys.stdin.readline().split()))
cnt = 0

# 뽑아 내려고하는 수를 모두 뽑을 때까지 반복한다.
while loc:

    # 현재 뽑아야하는 수가 큐의 앞쪽에서 뽑는게 더 가까운지 뒤쪽에서 뽑는게 가까운지 비교
    # 앞쪽에서 뽑는게 더 깝다면
    if queue.index(loc[0]) < len(queue) - queue.index(loc[0]):
        # 앞쪽에서 뽑는게 더 가까운 경우 2번 연산을 수행하면서 뽑아야하는 원소의 위치를 찾는다.
        while True:
            # 현재 뽑을 수 있는 수가 뽑아야하는 수라면
            if queue[0] == loc[0]:
                del queue[0] # 큐에서 현재 원소를 제거
                del loc[0] # 뽑아야하는 원소 리스트에서도 뽑아야 하는 원소를 제거
                break
                
            # 2번 연산 수행
            else:
                queue.append(queue[0])
                del queue[0]
                cnt += 1
                
    # 뒤쪽에서 뽑는게 더 깝다면
    else:
        
        # 뒤쪽에서 뽑는게 더 가까운 경우 3번 연산을 수행하면서 뽑아야하는 원소의 위치를 찾는다.
        while True:
            # 현재 뽑을 수 있는 수가 뽑아야하는 수라면
            if queue[0] == loc[0]:
                del queue[0] # 큐에서 현재 원소를 제거
                del loc[0] # 뽑아야하는 원소 리스트에서도 뽑아야 하는 원소를 제거
                break
                
            # 3번 연산 수행
            else:
                queue.insert(0, queue[-1])
                del queue[-1]
                cnt += 1

print(cnt)

