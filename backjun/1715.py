import sys
import heapq

n = int(input())
a=0
card =[]
for _ in range(n):
    heapq.heappush(card,int(sys.stdin.readline()))

if n == 1:
    print(0)
else:
    while len(card) >1:
        temp_1 = heapq.heappop(card)  # 제일 작은 덱
        temp_2 = heapq.heappop(card)  # 두번째로 작은 덱
        a += temp_1 + temp_2  # 현재 비교 횟수를 더해줌
        heapq.heappush(card, temp_1 + temp_2)  # 더한 덱을 다시 넣어줌

    print(a)
