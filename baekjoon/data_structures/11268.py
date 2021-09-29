import sys
import heapq

n = int(sys.stdin.readline())
heap = []

# 연산의 개수만큼 반복하여 연산에 대한 정보를 입력받아 수행한다.
for i in range(n):
    x = int(sys.stdin.readline())

    # 연산의 정보가 0이라면 배열에서 절댓값이 가장 작은 값을 출력
    if x == 0:
        # 배열의 수가 있으면 절댓값이 가작 작은 값을 출력
        if heap:
            a, b = heapq.heappop(heap)
            print(b)
            
        # 배열의 수가 없으면 0 출력 
        else:
            print("0")
            
    # 연산의 정보가 0이 아니라면 배열에 x의 값을 넣는다.
    else:
        # 배열의 x 값을 넣을 때 절댓값을 우선순위로 하여 넣는다.
        heapq.heappush(heap, (abs(x), x))
