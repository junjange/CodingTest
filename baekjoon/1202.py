import sys
import heapq

n, k = map(int,sys.stdin.readline().split())
heap = []
for _ in range(n):
    heapq.heappush(heap, list(map(int, sys.stdin.readline().split())))

c = [int(sys.stdin.readline()) for x in range(k)]
# 무게가 작은 가방부터 보석을 넣기위해 오름차순 정렬
c.sort()
# 현재 가방보다 작은 모든 보석들을 넣을 곳
bag = []
# 최대 가격
cnt = 0

for i in c:
    # 가방의 무게보다 작거나 같은 보석이 있는지 확인
    # heap[0][0]보다 크거나 같은 i 사이에 값이 heap 안에 있으면 true
    # 이때, heap[0][0]보다 크거나 같은 i 사이에 값중 heap 안에 있는 값을 하나씩 꺼내어 확인한다.
    while heap and i >= heap[0][0]:
        # 가방에 담을 수 있는 보석중 최대 가격순으로 bag에 넣는다.
        heapq.heappush(bag, -heapq.heappop(heap)[1]) # 최대힙

    # bag에 넣을 수 있는 보석이 있는 경우
    if bag:
        # 최대힙의 부호가 음수이기때문에 -로 연산하여 양수를 만든다.
        # 현재 최대 가격인 보석을 카운트
        cnt -= heapq.heappop(bag)
    # 남은 보석이 없는 경우 끝낸다.
    elif not heap:
        break

print(cnt)
