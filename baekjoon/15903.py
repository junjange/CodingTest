import sys
import heapq


n, m = map(int, sys.stdin.readline().split())
card = list(map(int, sys.stdin.readline().split()))
res = []

# 카드를 힙푸시하여 리스트에 넣는다.
[heapq.heappush(res, i) for i in card]

# m번 반복하여 카드 합체 놀이를 한다.
for i in range(m):

    # 카드 리스트에서 제일 작은 두 카드를 팝한다.
    x = heapq.heappop(res)
    y = heapq.heappop(res)
    
    # 제일 작은 두 카드를 더한다.
    total = x + y
    
    # 합친 카드를 다시 푸시하여 리스트에 넣는다.
    heapq.heappush(res, total)
    heapq.heappush(res, total)

# 리스트에 합을 출력한다.
print(sum(res))
