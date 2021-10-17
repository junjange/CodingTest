import heapq
import sys

n = int(sys.stdin.readline())
heap = [-1000000000] * n # heap 리스트에 제일 작은 수를 미리 넣는다.
target = -1000000000 # 비교할 수 (제일 작은 수로 초기화)

for _ in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    # 각 행의 열의 크기를 비교한다.
    for i in row:
        # 타겟보다 큰 수이면 
        if target < i:
            heapq.heappush(heap, i) # 큰 수를 힙에 추가한다.
            target = heapq.heappop(heap) # 힙에서 제일 작은 수를 팝하고 그 수를 타겟으로 바꾼다.

# 힙에서 제일 작은 수가 n 번째로 작은 수
print(heapq.heappop(heap))

