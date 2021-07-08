import sys
import heapq

n = int(sys.stdin.readline())
pd = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# 제일 빨리 강연하는 날부터 비교하기 위해 d 기준으로 오름차순 정렬한다.
pd.sort(key=lambda x: x[1])
heap = []

for p, d in pd:
    # 제일 빨리 하는 강연에 페이를 heap 리스트에 푸시한다.
    heapq.heappush(heap, p)

    # heap 리스트에 길이가 강연을 해야하는 날짜보다 크면 모든 강연을 못하므로 제일 작은 페이를 팝한다.
    # 반대로 작거나 같을경우는 강연을 할 수 있는 날이 되는 것이다.
    if len(heap) > d:
        heapq.heappop(heap)

# 힙안에 들어있는 페이를 모두 더한다.
print(sum(heap))
