import sys
import heapq

n = int(input())
result = 0
card = []

# 카드 묶음의 크기를 힙큐를 통해 card 리스트에 넣는다.
for _ in range(n):
    heapq.heappush(card,int(sys.stdin.readline()))

# 카드 묶음이 하나이면 비교할 필요가 없기때문에 0을 출력한다.
if n == 1:
    print(0)
else:
    # 카드 묶음이 1보다 클때까지 반복한다.
    while len(card) > 1:
        print(card)
        print(result)
        temp_1 = heapq.heappop(card)  # 제일 작은 덱
        temp_2 = heapq.heappop(card)  # 두번째로 작은 덱
        result += temp_1 + temp_2  # 현재 비교 횟수를 더해줌
        heapq.heappush(card, temp_1 + temp_2)  # 더한 덱을 다시 넣어줌

    print(result)
